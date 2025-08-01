import os
import pandas as pd

from config_loader import ConfigLoader
from data_loader import DataLoader


def get_loader():
    """Instantiate DataLoader using the project configuration."""
    repo_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(repo_dir, "conf", "config.yaml")
    loader = ConfigLoader(config_path=config_path)
    cfg = loader.get_config()
    excel_path = loader.resolve_path(cfg.data.excel_path)
    return DataLoader(excel_path, cfg.data.sheets), cfg


def test_load_configured_sheets():
    dataloader, cfg = get_loader()
    loaded = dataloader.load()

    # Verify that all configured sheets are loaded
    assert set(loaded.keys()) == set(cfg.data.sheets)

    # Validate each sheet's shape matches a fresh read
    with pd.ExcelFile(dataloader.excel_path) as xl:
        for sheet in cfg.data.sheets:
            df_expected = pd.read_excel(xl, sheet_name=sheet)
            df_loaded = loaded[sheet]
            assert df_loaded.shape == df_expected.shape

