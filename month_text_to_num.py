#!/usr/bin/env python

import bibtexparser
import calendar
import os
import sys

month_dict = dict((v.lower(), str(k)) for k,v in enumerate(calendar.month_abbr))
del month_dict['']

def convert_line(input_data):
    if 'month' in input_data.lower():
        for month, num in month_dict.iteritems():
            index = input_data.find(month)
            if index != -1:
                input_data = input_data[:index] + str(num) + input_data[index+3:]

    return input_data

if __name__ == "__main__":
    input_file = sys.argv[1]

    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = "out.bib"

    with open(input_file, "r") as f:
        db = bibtexparser.load(f)

    for i, entry in enumerate(db.entries):
        if 'month' in entry:
            entry['month'] = month_dict[entry['month']]

        db.entries[i] = entry

    with open(output_file, "w") as bib:
        bibtexparser.dump(db, bib)

    
