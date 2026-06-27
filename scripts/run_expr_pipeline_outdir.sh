#!/bin/bash
set -e
if [ "$#" -ne 3 ]; then
    echo "usgae: bash run_expr_pipeline_outdir.sh <input_file> <prefix> <outdir>"
    exit 1
fi
infile=$1
prefix=$2
outdir=$3
if [ ! -f "$infile" ]; then
    echo "error: input file not found: $infile"
    exit 1
fi
mkdir -p "$outdir"
echo "input file: $infile"
echo "prefix: $prefix"
echo "output dir: $outdir"
echo "step1: calculate expression difference"
python3 scripts/cacl_expr_diff.py "$infile" "${outdir}/${prefix}_expr_diff.tsv"
echo "step2: classify direction"
python3 scripts/classify_expr_diff.py "${outdir}/${prefix}_expr_diff.tsv" "${outdir}/${prefix}_expr_direction.tsv"
echo "step3: count direction"
python3 scripts/count_direction.py "${outdir}/${prefix}_expr_direction.tsv" "${outdir}/${prefix}_direction.tsv"
echo "step4: sort direction count"
python3 scripts/sort_direction_count.py "${outdir}/${prefix}_direction.tsv" "${outdir}/${prefix}_direction_sorted.tsv"
echo "step5: add percent"
python3 scripts/add_direction_percent.py "${outdir}/${prefix}_direction_sorted.tsv" "${outdir}/${prefix}_direction_percent.tsv"
echo "pipeline finished"
echo "final result: ${outdir}/${prefix}_direction_percent.tsv"
