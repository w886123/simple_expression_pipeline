import sys
import os
if len(sys.argv) != 3:
    print("usage: python3 classify_expr_diff.py <input_file> <output_file>")
    sys.exit()
infile = sys.argv[1]
outfile = sys.argv[2]
if not os.path.exists(infile):
    print("error: input file not found:", infile)
    sys.exit()
lines = open(infile, "r").readlines()
header = lines[0]
out = open(outfile, "w")
out.write("gene\tnormal\ttumor\tdiff\tdirection\n")
for line in lines[1:]:
    parts = line.strip().split("\t")
    gene = parts[0]
    normal = int(parts[1])
    tumor = int(parts[2])
    diff = int(parts[3])
    if diff > 0:
        direction = "up"
    elif diff < 0:
        direction = "down"
    else:
        direction = "no_change"
    print(gene, diff, direction)
    out.write(gene + "\t" + str(normal) + "\t" + str(tumor) + "\t" + str(diff) + "\t" + direction + "\n")
out.close()
print("saved to", outfile)
