# duke-biostat-707

Course repository for BIOSTAT 707 at Duke University.

## Checkpoint 1

With Pixi installed, place the 4,000 original PhysioNet Challenge 2012 Set 
A `.txt` records in `data/set-a/` and `Outcomes-a.txt` in `data/`. From the 
repository root, run `pixi run --locked checkpoint1`. This executes the R 
analysis in `checkpoint1.qmd` and produces `output/checkpoint1.html` (the 
report with tables and figures), `output/set-a_long.csv` (time-stamped 
measurement rows), and `output/set-a_wide.csv` (one row per admission with 
two 24-hour summary windows and outcomes). The raw data and derived CSV files 
are ignored by Git; the HTML report is the only file under `output/` intended for a final commit.

## Checkpoint 2

Checkpoint 2 uses Python in Quarto and the same Set A files. Reproduce it from
the repository root with `pixi run --locked checkpoint2`. It builds one
modeling row per ICU stay, performs nested five-fold cross-validation for three
models, compares them with SAPS-I and SOFA, and writes the report to
`output/checkpoint2.html`. It also creates the ignored derived files
`output/cp2_modeling_table.csv`, `output/cp2_oof_predictions.csv`,
`output/cp2_cv_results.csv`, and `output/cp2_final_model.joblib` for Checkpoint 3.
The complete locked run took approximately 8.4 minutes on this laptop.


## Checkpoint 3

Checkpoint 3 uses Python in Quarto and the saved CP2 model, modeling table,
CV results, and HTML report in `output/`. Keep the same Set A files and place
Set B and Set C records in `data/set-b/` and `data/set-c/` (or the corresponding
`.tar.gz` archives), with `Outcomes-b.txt` and `Outcomes-c.txt` in `data/`.
Reproduce it from the repository root with `pixi run --locked checkpoint3`.
The task automatically uses the separate locked environment in
`cp3-environment/`, with scikit-learn 1.6.1. It evaluates the frozen model
without retraining on Set B or Set C, covering discrimination, calibration,
clinical usefulness, subgroups, predictor interpretation, and confident
mistakes. The report is written to `output/checkpoint3.html`; additional
predictions, metric tables, figures, and verification results are saved under
`output/checkpoint3/` and ignored by Git. The analysis took approximately
0.6 minutes in the checked run, excluding environment installation and HTML
rendering.
