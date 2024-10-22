import sys

# Function that returns the complement of a DNA sequence
def complement(sequence):
    sequence2 = ""

    for base in sequence:
        if base == "A":
            sequence2 += "T"
        elif base == "T":
            sequence2 += "A"
        elif base == "C":
            sequence2 += "G"
        else:
            sequence2 += "C"
    return sequence2


# Function that returns the reverse of a sequence 
def reverse(sequence):
    reverse_seq = sequence[::-1]
    return reverse_seq


# Function that returns the reverse complement of a DNA sequence
def reverse_complement(sequence):
    sequence2 = ""

    for base in sequence:
        if base == "A":
            sequence2 += "T"
        elif base == "T":
            sequence2 += "A"
        elif base == "C":
            sequence2 += "G"
        else:
            sequence2 += "C"

    reverse_complement_seq = sequence2[::-1]
    return reverse_complement_seq


# Main Function
if __name__ == "__main__":
    sequence = sys.argv[1]
    complement_seq = complement(sys.argv[1])
    reverse_seq = reverse(sys.argv[1])
    comp_rev_seq = reverse_complement(sys.argv[1])

    print(f"The original sequence:              {sequence}")
    print(f"Its complement:                     {complement_seq}")
    print(f"Its reverse:                        {reverse_seq}")
    print(f"Its complement:                     {comp_rev_seq}")
