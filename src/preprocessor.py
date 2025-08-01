from __future__ import annotations

from typing import Dict, List

import pandas as pd


class Preprocessor:
    """Utility class for preprocessing datasets."""

    def __init__(self, data: Dict[str, pd.DataFrame]) -> None:
        self.data = data

    def extract_unique_values(self) -> Dict[str, Dict[str, List[str]]]:
        """Return all unique values for each column of every sheet."""
        mapping: Dict[str, Dict[str, List[str]]] = {}
        for sheet, df in self.data.items():
            col_map: Dict[str, List[str]] = {}
            for col in df.columns:
                uniques = df[col].dropna().astype(str).unique().tolist()
                col_map[col] = uniques
            mapping[sheet] = col_map
        return mapping
