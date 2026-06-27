import sys
import os
if len(sys.argv) != 3:
    print("usage: python3 sort_direction_count.py <input_file> <output_file>")
    sys.exit()
infile = sys.argv[1]
outfile = sys.argv[2]
if not os.path.exists(infile):
    print("error: input file not found:", infile)
    sys.exit()
lines = open(infile, "r").readlines()
counts = {}
for line in lines[1:]:
    parts = line.strip().split("\t")
    direction = parts[0]
    count = int(parts[1])
    counts[direction] = count
sorted_directions = sorted(counts, key=counts.get, reverse=True)
out = open(outfile, "w")
out.write("direction\tcount\n")
for direction in sorted_directions:
    print(direction, counts[direction])
    out.write(direction + "\t" + str(counts[direction]) + "\n")
out.close()
print("saved to", outfile)
