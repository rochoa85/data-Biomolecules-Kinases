#! /usr/bin/env python
import sys, csv

# NOTE: For this script it is required two CSV files with the results of BLAST between two sets of proteins in both directions.
# It means, using as query the two sets of fasta sequences during the BLAST.
#
# An example of how to run this script is: python2.7 find-reciprocal-2.py human_Lmajor.csv Lmajor_human.csv
#
# Any questions please write to: rodrigo.ochoa@udea.edu.co

# number below which to discard results
E_CUTOFF = 1e-10

def load_csv_to_dict(filename):
    """
    Load the CSV file into a dictionary, tying query sequences to subject
    sequences.
    """
    d = {}

    current_query_name, best_expect = None, None
    matches = []
    
    for (query_name, subject_name, score,expect) in csv.reader(open(filename)):
        # fix the names that start with a 'gi|XXXXXXX|'
        query_name = demangle_name(query_name)
        subject_name = demangle_name(subject_name)

        # convert the e-value into a floating point number
        expect = float(expect)

        if query_name == current_query_name:
            if expect == best_expect and expect < E_CUTOFF:
                matches.append(subject_name)
        else:
            # new query ==> store matches, reset
            if matches:
                d[current_query_name] = matches

            # store the new match?
            matches = []
            if expect < E_CUTOFF:
                matches.append(subject_name)

            current_query_name, best_expect = query_name, expect
            
    if matches:
        d[current_query_name] = matches

    return d

def demangle_name(name):
    """
    This functions strips off the 'gi|XXXXX|' name encoding that NCBI uses.

    Note that NCBI does this automatically for subject sequences.
    """
    if name.startswith('gi|'):
        name = name.split('|')
        name = name[2:]
        name = "|".join(name)

    return name

# Read the CSV files with the BLAST results in both ways

in_file_1 = sys.argv[1]
in_file_2 = sys.argv[2]

d1 = load_csv_to_dict(in_file_1)
d2 = load_csv_to_dict(in_file_2)

output = csv.writer(sys.stdout)

for name in d1:
    matches = d1[name]                  # 'matches' is a list
    for name2 in matches:
        matches2 = d2.get(name2)

        if matches2 and name in matches2: # so is 'matches2'
            output.writerow([name, name2])

