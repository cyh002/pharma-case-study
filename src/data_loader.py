"""Utilities for loading datasets from Excel workbooks."""

from __future__ import annotations

from typing import Dict

import pandas as pd


class DataLoader:
    """Load multiple sheets from an Excel workbook."""

    def __init__(self, excel_path: str, sheets: list[str]) -> None:
        self.excel_path = excel_path
        self.sheets = sheets

    def load(self) -> Dict[str, pd.DataFrame]:
        """Load all configured sheets.

        Returns
        -------
        Dict[str, pd.DataFrame]
            Mapping of sheet name to loaded :class:`~pandas.DataFrame`.
        """

        data = pd.read_excel(self.excel_path, sheet_name=self.sheets)
        # `pandas.read_excel` returns a DataFrame when a single sheet is passed,
        # but a dict when a list is provided. Ensure we always return a dict.
        if isinstance(data, pd.DataFrame):
            return {self.sheets[0]: data}
        return data
