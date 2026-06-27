set -e
set -o pipefail
if [ "$#" -ne 3 ]; then
    echo "usage: bash run_expr_pipeline_full.sh <input_file> <prefix> <outdir>"
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
logfile="${outdir}/${prefix}_pipeline.log"
echo "log file: $logfile"
echo "step1-5: run expression pipeline"
bash scripts/run_expr_pipeline_outdir.sh "$infile" "$prefix" "$outdir" 2>&1 | tee "$logfile"
echo "step6: check output files" | tee -a "$logfile"
bash scripts/check_pipeline_outputs.sh "$prefix" "$outdir" 2>&1 | tee -a "$logfile"
echo "pipeline finished with QC"
echo "final results: ${outdir}/${prefix}_direction_percent.tsv" | tee -a "$logfile"
