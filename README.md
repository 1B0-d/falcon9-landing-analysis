# Falcon 9 landing analysis

This educational project analyzes IBM Applied Data Science Capstone course exports to explore factors associated with Falcon 9 first-stage landing success. It includes reproducible SQL summaries and a machine-learning notebook. The results are descriptive and are not operational predictions.

## Contents

- `sql_methodology.py` imports the historical CSV into an in-memory SQLite database and runs the queries used in the report. `sql_methodology_results.txt` records a run from 13 November 2026.
- `SpaceX_Machine_Learning_Prediction_Lab.ipynb` compares logistic regression, SVM, decision tree, and k-nearest neighbors on the course data. Its code downloads IBM's course exports using the URLs in the notebook.
- `data/` contains the course CSV snapshots used in the local analysis. IBM and course contributors retain their rights to the source material.

## Run the SQL analysis

Install Python 3 and pandas, then run `python sql_methodology.py` from this directory. The CSV has 101 records and four distinct site labels. The NASA customer filter uses a substring match, which can include records listing multiple customers.

## Run the notebook

Install Jupyter, pandas, numpy, scikit-learn, and matplotlib. Open the notebook in Jupyter and run the cells in order. Network access is required for its IBM-hosted datasets. The educational notebook reproduces the course workflow, which fits the scaler before the train/test split; this leaks information from the holdout. A production evaluation should fit preprocessing within training folds instead.

The model dataset has 90 launches with an 18-record holdout. The notebook's model feature file has 83 columns; an independent one-hot encoding of the specified 12 fields in `dataset_part_2.csv` produces 80 columns. These describe different feature inputs and should not be conflated.

## Sources and scope

Data: IBM Skills Network Applied Data Science Capstone course exports, including `dataset_part_2.csv`, `dataset_part_3.csv`, `Spacex.csv`, and `spacex_launch_dash.csv`. The work uses these course-provided snapshots; it does not claim to have newly collected SpaceX API or web-scraping data. The interactive dashboard extract and the SQL and model tables have different row counts and labels.

This repository contains the available SQL and machine-learning materials; it does not include notebooks for every lab and should not be represented as a complete archive of the original course work.
