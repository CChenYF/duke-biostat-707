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
