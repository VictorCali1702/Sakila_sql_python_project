# Sakila_sql_python_project
SQL analysis project using the Sakila MySQL database. Queries executed using python, results saved to CSV and visualized.

# 🎬 Sakila SQL Project

A portfolio project using the **Sakila sample database** to practice SQL queries through Python, MySQL, Pandas and Jupyter Notebook.  
This project demonstrates SQL skills ranging from simple SELECTs to advanced joins, groupings, and aggregations.

---

## 📁 Project Structure
sakila-sql-project/
├── data/               # sakila-schema.sql and sakila-data.sql
├── scripts/            # Optional Python scripts (deprecated in favor of Jupyter)
├── notebooks/          # Main notebook with SQL queries and analysis
├── reports/            # CSV files with query outputs
├── screenshots/        # Screenshots of query results
└── README.md

---

## 🛠️ Technologies Used

- **MySQL Workbench** – for managing the database
- **Python** – for connecting and querying
- **pymysql** – Python library for MySQL connection
- **pandas** – for clean result handling and export
- **Jupyter Notebook** – for running queries and documentation
- **GitHub** – version control and portfolio hosting

---

## ✅ Completed Queries

| # | Query Description | SQL Concepts | Tables Used |
|--:|-------------------|--------------|-------------|
| 1 | List all movie titles | `SELECT` | `film` |
| 2 | Get unique film categories | `DISTINCT` | `category` |
| 3 | Count number of films in each category | `JOIN`, `GROUP BY` | `film`, `film_category`, `category` |
| 4 | Display actors with last name starting with "S" | `LIKE`, `WHERE` | `actor` |
| 5 | Show movie titles and their main actors | `JOIN`, `SELECT` | `film`, `film_actor`, `actor` |
| 6 | Find "Comedy" films longer than 100 minutes | `JOIN`, `WHERE` | `film`, `film_category`, `category` |

Each query:
- Was written and executed in Jupyter Notebook ✅  
- Has its result exported to `.csv` in `/reports` 📄  
- Has an optional screenshot saved in `/screenshots` 🖼️  

---

## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/sakila-sql-project.git
   cd sakila-sql-project

2.	Import sakila-schema.sql and sakila-data.sql into MySQL (via Workbench or CLI).
3.	Install required Python libraries:
   pip install pandas pymysql
4.	Launch Jupyter Notebook and run notebooks/analysis_report.ipynb.


🚀 Upcoming Features
	•	Advanced queries: top customers, rentals by month, most rented categories
	•	Grouped aggregations and subqueries
	•	Data visualization with pandas/plotly/matplotlib
	•	Export full report as PDF/HTML
	•	Interactive dashboard using Streamlit (optional)


📎 Repository Link



🙋 About Me

Wiktor Naczk
📍 Python & SQL & Data Analyst and Data Science Enthusiast
🚀 Building open-source data projects for my portfolio
📫 Reach me via LinkedIn or GitHub
https://www.linkedin.com/in/wiktor-naczk-696954349?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app



