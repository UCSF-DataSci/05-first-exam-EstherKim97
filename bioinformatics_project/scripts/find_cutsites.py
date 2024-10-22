import os
import re
import sys

def find_cutsites(file_path, cutsite_seq):

    # open FASTA file
    with open(file_path, "r") as FASTA_file:
        sequence = FASTA_file.read()
        sequence = sequence.replace(" ", "").replace("\n", "")

    # replace | from the restriction enzyme cutsite
    cutsite = cutsite_seq.replace("|", "")

    # search for cut sites
    cutsites_found = []
    cutsites_apart = []

    cutsites_found = list(re.finditer(cutsite, sequence))

    # look for cut site pairs of 80,000 - 120,000 base pairs apart
    total_cutsites = len(cutsites_found)
    for pos1 in range(total_cutsites):
        for pos2 in range(pos1+1, total_cutsites):
            distance = cutsites_found[pos2].start() - cutsites_found[pos1].start()
            if 80000 <= distance <=120000:
                cutsites_apart.append((cutsites_found[pos1].start(), cutsites_found[pos2].start()))

    
    return cutsites_found, cutsites_apart

if __name__ == "__main__":
    current_dir = os.getcwd()
    fasta_file = sys.argv[1]
    fasta_file_path = os.path.join(current_dir, "..", fasta_file)

    cutsite_seq = sys.argv[2]

    cutsites_found, cutsites_apart = find_cutsites(fasta_file_path, cutsite_seq)

    print(f"Analyzing cut site: {cutsite_seq} \nTotal cut sites found: {len(cutsites_found)} \nCut site pairs 80-120 kbp apart: {len(cutsites_apart)} \nFirst 5 pairs: \n")
    for i in range(min(5, len(cutsites_apart))):
        pos1 = cutsites_apart[i][0]
        pos2 = cutsites_apart[i][1]
        print(f"{i}. {pos1} - {pos2}")

    with open("cutsite_summary.txt", "w") as summary:
        summary.write("Analyzing cut site: {cutsite_seq} \nTotal cut sites found: {len(get_cutsites)} \nCut site pairs 80-120 kbp apart: {len(get_cutsites_part)} \nFirst 5 pairs: \n")
        for i in range(min(5, len(cutsites_apart))):
            pos1 = cutsites_apart[i][0]
            pos2 = cutsites_apart[i][1]
            summary.write(f"{i}. {pos1} - {pos2}")