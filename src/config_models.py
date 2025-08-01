from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class DataConfig(BaseModel):
    """Configuration for dataset loading."""

    excel_path: str = Field(..., description="Path to the Excel workbook")
    sheets: List[str] = Field(..., description="List of sheet names to load")


class ConfigSchema(BaseModel):
    """Root configuration schema."""

    data: DataConfig

