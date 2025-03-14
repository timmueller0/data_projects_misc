# Optimizing DataFrames and Processing in Chunks

In this project, we'll practice with chunked dataframes and optimize a dataframe's memory usage. We'll work with financial lending data from [Lending Club](https://www.lendingclub.com/), a marketplace for personal loans that matches borrowers with investors. You can read more about the marketplace [on its website](https://www.lendingclub.com/help/personal-loan-faq).

The Lending Club's website lists approved loans. Qualified investors can view the borrower's credit score, the purpose of the loan, and other details in the loan applications. Once a lender is ready to back a loan, it selects the amount of money it wants to lend. When the loan amount the borrower requested is fully funded, the borrower receives the money, minus the origination fee that Lending Club charges.

We'll work with a dataset of loans approved from 2007-2011. Although Lending Club no longer hosts the data, a comprehensive view of the data is available on Kaggle [here](https://www.kaggle.com/datasets/wordsforthewise/lending-club/data). The `desc` column has been removed to make the system run faster.

If we read in the entire dataset, it consumes about 67 megabytes of memory. Let's imagine that we only have 10 megabytes of memory available throughout this project, so that everything needs to be processed in chunks. We'll start by reading in and checking the first five lines. 

## Data Files

This project includes the following data files:

`loans_2007.csv`: Loan dataset. [Lending Club dataset on Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club/data). 

## Instructions

Download or clone this repository.
Ensure that the data files are located in the `Data/` directory.
Open the Jupyter Notebook `Guided_project_23 - Building Fast Queries on a CSV.ipynb` and run the cells to reproduce the analysis.

## Project Notebook

You can also directly view or run the analysis in the [Jupyter Notebook](https://github.com/timmueller0/data_projects_misc/blob/main/projects/guided_project_25_optimizing_dataframes_and_processing_in_chunks/Guided_project_25%20-%20Optimizing%20DataFrames%20and%20Processing%20in%20Chunks.ipynb)
