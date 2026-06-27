set -e
if [ "$#" -ne 2 ]; then
    echo "usage: bash check_pipeline_outputs.sh <prefix> <outdir>"
    exit 1
fi
prefix=$1
outdir=$2
files="${prefix}_expr_diff.tsv ${prefix}_expr_direction.tsv ${prefix}_direction.tsv ${prefix}_direction_sorted.tsv ${prefix}_direction_percent.tsv ${prefix}_pipeline.log"
for file in $files; do
    path="${outdir}/${file}"
    if [ ! -s "$path" ]; then
        echo "error:missing or empty file: $path"
        exit 1
    fi
    echo "ok: $path"
done
echo "all output files are ok"
