from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict

from log_utils import get_logger

try:
    import argostranslate.package
    import argostranslate.translate
except ImportError:  # pragma: no cover - package optional
    argostranslate = None


class Translator:
    """Translate text using Argos Translate if available."""

    def __init__(self, from_code: str = "zh", to_code: str = "en") -> None:
        self.from_code = from_code
        self.to_code = to_code
        self.logger = get_logger(self.__class__.__name__)
        if argostranslate:
            try:
                self._ensure_package()
            except Exception as exc:  # pragma: no cover - network dependency
                self.logger.warning("Failed to install translation package: %s", exc)
        else:
            self.logger.warning(
                "argostranslate not installed; translations will return original text"
            )

    @staticmethod
    def available() -> bool:
        """Return True if argostranslate library is available."""
        return argostranslate is not None

    def _ensure_package(self) -> None:
        """Ensure the language package is installed."""
        argostranslate.package.update_package_index()
        packages = argostranslate.package.get_available_packages()
        pkg = next(
            (
                p
                for p in packages
                if p.from_code == self.from_code and p.to_code == self.to_code
            ),
            None,
        )
        if pkg:
            argostranslate.package.install_from_path(pkg.download())

    def translate(self, text: str) -> str:
        """Translate a single string."""
        if argostranslate:
            return argostranslate.translate.translate(
                text, self.from_code, self.to_code
            )
        return text

    def translate_mapping(
        self, mapping: Dict[str, Dict[str, list[str]]], max_workers: int = 8
    ) -> Dict[str, Dict[str, Dict[str, str]]]:
        """Translate all values in the mapping concurrently."""
        result: Dict[str, Dict[str, Dict[str, str]]] = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {}
            for sheet, cols in mapping.items():
                sheet_res: Dict[str, Dict[str, str]] = {}
                result[sheet] = sheet_res
                for col, values in cols.items():
                    col_map: Dict[str, str] = {}
                    sheet_res[col] = col_map
                    for value in values:
                        future = executor.submit(self.translate, value)
                        futures[future] = (sheet, col, value)
            for future in as_completed(futures):
                sheet, col, value = futures[future]
                translated = future.result()
                result[sheet][col][value] = translated
        return result

    def save_mapping(self, mapping: Dict, path: str) -> None:
        """Save mapping dictionary to a JSON file."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
