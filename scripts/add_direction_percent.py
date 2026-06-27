import sys
import os
if len(sys.argv) != 3:
    print("uasge: python3 add_direction_percent.py <input_file> <output_file>")
    sys.exit()
infile = sys.argv[1]
outfile = sys.argv[2]
if not os.path.exists(infile):
    print("error: input file not found:", infile)
    sys.exit()
lines = open(infile, "r").readlines()
total = 0
for line in lines[1:]:
    parts = line.strip().split("\t")
    count = int(parts[1])
    total = total + count
out = open(outfile, "w")
out.write("direction\tcount\tpercent\n")
for line in lines[1:]:
    parts = line.strip().split("\t")
    direction = parts[0]
    count = int(parts[1])
    percent = count / total *100
    print(direction, count, percent)
    out.write(direction + "\t" + str(count) + "\t" + str(round(percent, 2)) + "\n")
out.close()
print("total genes =", total)
print("saved to", outfile)
