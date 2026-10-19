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
