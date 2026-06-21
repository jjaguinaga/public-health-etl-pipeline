# Public Health ETL Pipeline — COVID-19 Vaccine Effectiveness Analysis

**An end-to-end ETL pipeline analyzing COVID-19 case and death rates by vaccination status and age group, using CDC public health data.**

---

## Motivation

This project was built to settle an ongoing debate with people who claim COVID-19 vaccines do nothing to protect against the virus, or worse, that they cause death. Rather than relying on opinion or anecdote, this project pulls real CDC data, builds a clean and reliable database, and lets the numbers answer the question directly.

---

## What This Project Does

This pipeline extracts CDC data comparing COVID-19 outcomes (cases and deaths) between vaccinated and unvaccinated populations, broken down by age group and tracked over time. It cleans and validates the data, stores it in a relational database, and produces SQL views that allow analysts to explore vaccine effectiveness from multiple angles.

---

## Key Findings

- **Vaccines were protective against death in every single age group.** The `cases_deaths_by_age` view shows a negative IRR difference across all seven age groups, meaning the vaccine's protective effect against death was consistently stronger than its protective effect against simply testing positive.
- **Effectiveness trends improved as vaccination rates increased.** The `irr_trend_by_month` view shows that as more of the population became vaccinated over time, both case and death rates dropped across age groups.

---

## Architecture

```
CDC Public API
↓
extract.py  →  MongoDB (raw data storage)
↓
transform.py  →  Pandas (data cleaning & validation)
↓
load.py    →  PostgreSQL (data warehouse)
↓
SQL Views   →  Analytics layer for vaccine effectiveness insights
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core pipeline logic |
| Pandas | Data cleaning and transformation |
| MongoDB | Raw data storage |
| PostgreSQL | Data warehouse |
| SQLAlchemy | Database connection and loading |
| CDC Public API | Data source |

---

## Project Structure

```
public-health-etl-pipeline/
├── data/
├── notebooks/
├── sql/
│   └── views.sql
├── extract.py
├── transform.py
├── load.py
├── pipeline.py
└── README.md
```

---

## How to Run

1. Install dependencies:
```bash
   pip install pandas pymongo sqlalchemy psycopg2-binary requests
```
2. Make sure MongoDB and PostgreSQL are running locally
3. Create the PostgreSQL database:
```sql
   CREATE DATABASE covid_vaccine_project;
```
4. Run the full pipeline:
```bash
   python3 pipeline.py
```
5. Run the SQL views found in `sql/views.sql` against the `covid_vaccine_project` database

---

## Data Source

[CDC: Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status](https://data.cdc.gov/Public-Health-Surveillance/Rates-of-COVID-19-Cases-or-Deaths-by-Age-Group-an)