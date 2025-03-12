# Analyzing Startup Fundraising Deals from Crunchbase

In this project, we'll practice using some of the techniques we learned to analyze startup investments from Crunchbase.com.
Every year, thousands of startup companies raise financing from investors. Each time a startup raises money, we refer to the event as a fundraising round. Crunchbase is a website that crowdsources information on the fundraising rounds of many startups. The Crunchbase user community submits, edits, and maintains most of the information in Crunchbase.
In return, Crunchbase makes the data available through a web application and a fee-based API. Before Crunchbase switched to the paid API model, multiple groups went to the site and released the data online. Since the information on the startups and their fundraising rounds is always changing, the dataset we'll be using isn't completely up to date.
The dataset of investments we'll be exploring from October 2013. You can download it from [GitHub](https://github.com/datahoarder/crunchbase-october-2013/blob/master/crunchbase-investments.csv).

We'll practice working with different memory constraints. In this step, let's assume we only have 10 megabytes of available memory. While `crunchbase-investments.csv` consumes 10.3 megabytes of disk space, we know that pandas typically requires significantly more space in memory than the file does on disk (especially when there are multiple string columns). The exact memory usage can vary depending on the pandas version, data types, and specific operations, but it's often several times larger than the original file size.

We'll process the data in chunks of 5000 rows and learn about each colum's missing value counts, memory foortprint, the total memory footprint of all chunks combined. We will also drop columns not needed for the analysis.

## Data Files

This project includes the following data files:

`crunchbase-investments.csv`: Crunchbase dataset. [Download from Kaggle](https://github.com/datahoarder/crunchbase-october-2013/blob/master/crunchbase-investments.csv). 

## Instructions

Download or clone this repository.
Ensure that the data files are located in the `Data/` directory.
Open the Jupyter Notebook `Guided Project 26 -Analyzing Startup Fundraising Deals from Crunchbase.ipynb` and run the cells to reproduce the analysis.

## Project Notebook

You can also directly view or run the analysis in the [Jupyter Notebook](https://github.com/timmueller0/data_projects_misc/blob/main/projects/guided_project_26_analyzing_startup_fundraising_deals_from_crunchbase/Guided%20Project%2026%20-Analyzing%20Startup%20Fundraising%20Deals%20from%20Crunchbase.ipynb)
