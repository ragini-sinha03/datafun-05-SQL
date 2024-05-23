import sqlite3
import pandas as pd
from pathlib import Path

def create_database(db_path):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the employee table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')

    # Commit the changes
    conn.commit()
    print("Employee table created successfully.")
    return conn

def insert_employees(conn):
    cursor = conn.cursor()

    # Insert employee records
    employees = [
        ('Alice Johnson', 30, 'HR', 'Manager', 60000),
        ('Bob Smith', 24, 'Engineering', 'Software Engineer', 80000),
        ('Charlie Brown', 28, 'Sales', 'Sales Representative', 55000),
        ('Diana Prince', 35, 'Marketing', 'Marketing Manager', 70000),
        ('Ethan Hunt', 32, 'Operations', 'Operations Manager', 75000),
        ('Fiona Glenanne', 29, 'Finance', 'Accountant', 65000),
        ('George Miller', 40, 'Engineering', 'Senior Developer', 90000),
        ('Hannah Montana', 27, 'HR', 'HR Specialist', 50000),
        ('Ian McKellen', 38, 'Engineering', 'DevOps Engineer', 85000),
        ('Jessica Jones', 31, 'Marketing', 'Content Strategist', 62000),
        ('Kyle Reese', 26, 'Sales', 'Sales Manager', 58000),
        ('Laura Palmer', 34, 'Finance', 'Financial Analyst', 72000)
    ]

    cursor.executemany('''
        INSERT INTO employee (name, age, department, position, salary)
        VALUES (?, ?, ?, ?, ?)
    ''', employees)

    # Commit the changes
    conn.commit()
    print("Employee records inserted successfully.")

def read_employees(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Read the employee table into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM employee", conn)

    # Close the connection
    conn.close()

    return df

if __name__ == "__main__":
    # Define the database path
    db_path = Path("company.db")

    # Create the database and table
    conn = create_database(db_path)

    # Insert employee records
    insert_employees(conn)

    # Close the connection
    conn.close()

    # Read and print the employee table using pandas
    df = read_employees(db_path)
    print(df)
