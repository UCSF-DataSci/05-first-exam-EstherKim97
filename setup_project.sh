#!/bin/bash

#Create a main project directory called "bioinformatics_project"
mkdir bioinformatics_project

# Inside the main directory, create the following subdirectories
cd bioinformatics_project

mkdir data
mkdir scripts
mkdir results

# Create Python files in scripts directory
cd scripts

touch generate_fasta.py
touch dna_operations.py
touch find_cutsites.py

# Create file in results directory
cd ..
cd results
touch cutsite_summary.txt

# Create file in data directory
cd ..
cd data
touch random_sequence.fasta

# Create README.md file in main directory
cd ..
touch README.md
echo "The main directory "bioinformatics_project" was created with subdirectories of data, scripts, and results. In data directory, fasta file was made, Python files for scripts directory, txt file in results directory." > README.md

