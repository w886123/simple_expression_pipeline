# simple Expression Direction Pipeline

## Project goal

This project analyzes a small gene expression table.
It calculates tumor-normal expression difference, classifies genes as up, down, or no_change, counts each category, calculates percentages, saves results, writes a log file, and checks output files.

## Input file

The input file is a tab-separated table with three columns:

gene normal tumor
TP53 10 30
EGFR 20 50
BRCA1 40 20
MYC 15 15

## How to run

Run this command from the project root directory:

bash scripts/run_expr_pipeline_full.sh data/expr_text.tsv test9 results

Arguments:

1. data/expr_text.tsv: input expression table
2. test9: output file prefix
3. results: output directory

## Output files

The pipeline creates these output files:

results/test9_expr_diff.tsv
results/test9_expr_direction.tsv
results/test9_direction.tsv
results/test9_direction_sorted.tsv
results/test9_direction_percent.tsv
results/test9_pipeline.log

## Final result file is:

results/test9_direction_percent.tsv

Example result:

direction count percent
up 2 50.0
down 1 25.0
no_change 1 25.0

This means two genes are up-regulated, 1 gene is down-regulated, and 1 gene has no expression change.

## Quality control

The pipeline automatically checks whether all expected output files exist and are not empty.

## Project workflow

data/expr_text.tsv
  -> calculate expression difference
  -> classify expression direction
  -> count up/down/no_change
  -> calculate percentage
  -> save final result and log file
  -> check output files

## Project structure

simple_expression_pipeline/
  README.md
  data/
    expr_text.tsv
  scripts/
    cacl_expr_diff.py
    classify_expr_diff.py
    count_direction.py
    sort_direction_count.py
    add_direction_percent.py
    run_expr_pipeline_outdir.sh
    run_expr_pipeline_full.sh
    check_pipeline_outputs.sh
  results/
    test9_direction_percent.tsv
    test9_pipeline.log

## Version control

This project uses Git to track code and documentation changes.

## Github repository

This project is available on Github
https://github.com/w886123/simple_expression_pipeline
