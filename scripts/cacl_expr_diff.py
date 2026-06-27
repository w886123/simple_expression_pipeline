import sys
import os
if len(sys.argv) != 3:
    print("usage: python3 calc_expr_diff.py <input_file> <output_file>")
    sys.exit()
infile = sys.argv[1]
outfile = sys.argv[2]
if not os.path.exists(infile):
    print("error: input file not found:", infile)
    sys.exit()
lines = open(infile, "r").readlines()
header = lines[0]
out = open(outfile, "w")
out.write("gene\tnormal\ttumor\tdiff\n")
for line in lines[1:]:
    parts = line.strip().split("\t")
    gene = parts[0]
    normal = int(parts[1])
    tumor = int(parts[2])
    diff = tumor - normal
    print(gene, normal, tumor, diff)
    out.write(gene + "\t" + str(normal) + "\t" + str(tumor) + "\t" + str(diff) + "\n")
out.close()
print("saved to", outfile)
