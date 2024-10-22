import random
import os
import textwrap

# Function to create random DNA sequence of 1 million base pairs

def random_DNA_seq(length):
    basepairs = ['A', 'C', 'G', 'T']
    return ''.join(random.choices(basepairs, k = length))

# Main function to save the sequence in FASTA format

if __name__ == "__main__":
    DNA_sequence = random_DNA_seq(1000000)

    current_directory = os.getcwd()
    preferred_directory = os.path.join(current_directory, "..", "data")

    if not os.path.exists(preferred_directory):
        os.makedirs(preferred_directory)

    os.chdir(preferred_directory)

    with open("random_sequence.fasta", 'w') as file:
        file.write("> Random DNA Sequence \n")
        file.write('\n'.join(textwrap.wrap(DNA_sequence, width = 80)))

    print(f"Random DNA sequence generated and saved to {preferred_directory}")
  
