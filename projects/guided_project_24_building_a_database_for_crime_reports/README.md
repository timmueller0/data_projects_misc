#  Building a database for crime reports

In this project, we will build a database for storing data related to crimes that occurred in Boston. We will use Postgres, and in the process we will
- create a database and manage database roles
- create database schemas and tables with the proper datatypes
- load data from CSV files into database tables.

We use the dataset `boston.csv` which has seven columns:
1. `incident_number` (ID of the crime)
2. `offense_code` (numeric identifier code, offense)
3. `description` (description of the incident)
4. `date` (date in YY-MM-DD format)
5. `day_of_the_week` (weekday)
6. `lat` (location, latitude)
7. (`lon`) (location, longitude)

The goal of this guided project is to create a database named `crimes_db` with a table – `boston_crimes` – with appropriate datatypes for storing the data from the `boston.csv` file. We will be creating the table inside a schema named `crimes`. We will also create the `readonly` and `readwrite` groups with the appropriate privileges. Finally, we will also need to create one user for each of these groups. 

## Data Files
The project used a database (including datafiles) made available by [Dataquest.io](https://www.dataquest.io/). The code in the Jupyter notebook shows how to connect to that database. 

## Instructions

Download or clone this repository.
Ensure that the data files are located in the Data/ directory.
Open the Jupyter Notebook `Guided_project_24 -Building a database for crime reports.ipynb` and run the cells to reproduce the analysis.

## Project Notebook

You can also directly view or run the analysis in the [Jupyter Notebook](https://github.com/timmueller0/data_projects_misc/blob/main/projects/guided_project_23_building_fast_queries_on_a_csv/Guided_project_23%20-%20Building%20Fast%20Queries%20on%20a%20CSV.ipynb)

