#  Earthquake ETL Pipeline

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline that ingests global earthquake data from the USGS API, transforms it into a clean and structured format, and loads it into a PostgreSQL database. Visualizations are then generated for exploratory data analysis.

---

##  Project Structure

```
earthquake_etl/
├── data/                  # Stores raw and visual output files
├── src/                   # ETL scripts
│   ├── extract.py         # Data extraction from USGS API
│   ├── transform.py       # Data cleaning, feature engineering, normalization
│   ├── load.py            # Data loading into PostgreSQL + verification query
│   └── visualization.py       # Generates charts using Matplotlib & Seaborn
├── main.py                # Orchestrates the ETL pipeline
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

---

## How to Run (with Docker)

1. **Build and run everything**:
   ```bash
   docker-compose up --build
   ```

2. **Access your PostgreSQL DB**:
   - Host: `localhost`
   - Port: `5432`
   - User: `postgres`
   - Password: `password`
   - Database: `earthquakes`

3. **ETL Output**:
   - Table: `earthquakes`
   - Visuals: `data/magnitude_distribution.png`, `data/monthly_earthquakes.png`

---

## Features Implemented

- Extract data from USGS Earthquake API
- Transform:
  - Convert timestamps
  - Handle missing data
  - Feature engineer: `region`, `magnitude category`, `year/month/day`
  - Normalize: depth using min-max scaling
  - Aggregate: earthquake count per region
- Load into PostgreSQL
- Verify insert count with SQL
- Generate visualizations

---

## Tools Used

- Python (pandas, requests, sqlalchemy)
- PostgreSQL (via Docker)
- Matplotlib & Seaborn for visualization
- Docker & Docker Compose for containerization

---

## Visual Output Samples

- `data/magnitude_distribution.png`: Histogram of earthquake magnitudes
- `data/monthly_earthquakes.png`: Time series plot of earthquake frequency

---

## Future Enhancements

- Add orchestration via Kestra or Apache Airflow
- Add dashboard via Looker Studio
- Deploy ETL container in cloud

---

##  Author

Suyog Dahal • ETL Project done for CIS 660 – Applied Computer Science Grand Valley State Univeristy, April 2025
