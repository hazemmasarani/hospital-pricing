```
hospital-pricing/
│
├── data/
│   ├── raw/               # Original downloaded files (CSV, JSON, XML, Excel)
│   ├── hospital.db        # SQLite database storing processed data
│
├── notebooks/             # Jupyter notebooks for EDA or testing
│   ├── exploration.ipynb
│   └── EDA.ipynb
│
├── src/                   # Source code
│   ├── __init__.py
│   ├── config.py          # Global variables and configuration
│   ├── downloader.py      # Code to fetch hospital pricing files
│   ├── parser.py          # Code to parse different file formats
│   ├── reconciler.py      # Logic for reconciling different schemas
│   ├── database.py        # Optional: store data in SQLite/Postgres
│   ├── analyzer.py        # Price analysis, statistics, trends
│   └── utils.py           # Shared utility functions
│
├── run_pipeline.py        # Orchestrates full ETL process
│
├── requirements.txt       # Dependencies
├── README.md              # Project description
└── .gitignore
```

## Project Overview

This project scrapes and processes hospital pricing files published under the Hospital Price Transparency Act. It enables structured analysis of medical procedures and their costs across institutions.

### Main Features

- **ETL Pipeline:** Downloads, parses, cleans, reconciles, and analyzes hospital pricing data.
- **Multi-format Support:** Handles CSV, JSON, XML, and Excel files.
- **Database Integration:** Stores processed data in SQLite (`hospital.db`).
- **Exploratory Analysis:** Jupyter notebooks for data exploration and SQL-based EDA.

### How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the ETL pipeline:
    ```
    python run_pipeline.py
    ```
3. Explore data and analysis in the `notebooks/` directory.

### File/Directory Details

- **data/raw/**: Downloaded hospital pricing files.
- **data/hospital.db**: SQLite database with processed data.
- **src/**: Source code for ETL steps.
- **notebooks/**: Jupyter notebooks for exploration and analysis.
- **run_pipeline.py**: Main script to run the full ETL workflow.

### Extending

- Add more hospital sources by updating `src/downloader.py`.
- Support new file formats by extending `src/parser.py`.
- Enhance analysis in `src/analyzer.py` or notebooks.

### References

- [Mount Sinai Price Transparency](https://www.mountsinai.org/about/patient-information/billing/price-transparency)
- [Johns Hopkins Hospital Pricing](https://www.hopkinsmedicine.org/patient-care/billing-insurance/price-transparency/)

---

For questions or contributions, please open an issue or submit a pull request.
