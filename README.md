# Data Pipeline Project

A small Python data pipeline that extracts, transforms, and combines sales data from two different companies — one stored as JSON, the other as CSV — into a single, unified CSV dataset.

> This project was built as a hands-on exercise based on the **"Pipeline de dados"** course from **Alura**. The core logic was extended and adapted while working through the course material.

## What it does

1. **Extract** — reads raw sales data from two sources with different formats and schemas:
   - Company A: JSON file (`data_raw/dados_empresaA.json`)
   - Company B: CSV file (`data_raw/dados_empresaB.csv`)
2. **Transform** — maps Company B's original column names to match Company A's schema, using a `key_mapping` dictionary, so both datasets share the same field names before being merged.
3. **Combine & Load** — merges both datasets into a single list of records and writes the result to `data_processed/dados_combinados.csv`, filling in `"Not available"` for any field missing in a given record (e.g., Company A has no sale-date field, so that column is empty for its rows).

## Project structure

```
pipeline_dados/
├── data_raw/                          # original source files (JSON + CSV)
├── data_processed/                    # output of the pipeline (combined CSV)
├── notebooks/                         # exploratory analysis notebooks
├── scripts/
│   ├── data_processing.py             # the Data class (core logic)
│   ├── fusion_enterprises_fev.py      # earlier, non-optimized version
│   └── fusion_enterprises_fev_test.py # final, optimized pipeline — calls Data's methods directly
├── requirements.txt
├── .gitignore
└── venv/                              # virtual environment (not tracked in git)
```

The `scripts/` folder holds two versions of the pipeline script. The `_test` file is the **final, optimized version** — it builds the pipeline purely by calling the methods already defined in `data_processing.py`, instead of duplicating logic.

## The `Data` class

All the core logic lives in `data_processing.py`, inside a single `Data` class:

| Method | Type | Purpose |
|---|---|---|
| `__init__` | instance | loads and stores the raw data on object creation |
| `__reading_json` / `__reading_csv` | private instance | read a file according to its type |
| `__reading_data` | private instance | dispatches to the right reader based on `file_type` |
| `__get_cols` | private static | extracts the list of column names from a dataset |
| `treating_data` | instance | remaps a dataset's keys using a `key_mapping` dict |
| `combining_and_saving_data` | static | merges two datasets and writes the final CSV |

Methods that are only ever used internally by the class are marked private (`__method_name`), following Python's naming convention for internal-use members.

## Setup

```bash
# clone the repo
git clone https://github.com/deboramendes27/data_pipeline_course.git
cd data_pipeline_course

# create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python scripts/fusion_enterprises_fev_test.py
```

This reads both source files from `data_raw/`, applies the transformation, and writes the combined dataset to `data_processed/dados_combinados.csv`.

## Notes

- `requirements.txt` was generated with `pip freeze` from the project's virtual environment.
- `venv/`, raw/processed data, and notebook checkpoints are excluded from version control via `.gitignore`.
