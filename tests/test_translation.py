import os
import pytest

from config_loader import ConfigLoader
from data_loader import DataLoader
from preprocessor import Preprocessor
from translation import Translator


def load_data():
    repo_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(repo_dir, "conf", "config.yaml")
    loader = ConfigLoader(config_path=config_path)
    cfg = loader.get_config()
    excel_path = loader.resolve_path(cfg.data.excel_path)
    dataloader = DataLoader(excel_path, cfg.data.sheets)
    return dataloader.load()


@pytest.mark.skipif(not Translator.available(), reason="argostranslate not installed")
def test_translation_shapes(tmp_path):
    data = load_data()
    preproc = Preprocessor(data)
    unique_map = preproc.extract_unique_values()

    translator = Translator(
        os.getenv("ARGOS_FROM_CODE", "zh"), os.getenv("ARGOS_TO_CODE", "en")
    )
    translated = translator.translate_mapping(unique_map)
    output = tmp_path / "mapping.json"
    translator.save_mapping(translated, output)

    for sheet, cols in unique_map.items():
        assert sheet in translated
        for col, values in cols.items():
            assert col in translated[sheet]
            assert len(values) == len(translated[sheet][col])

