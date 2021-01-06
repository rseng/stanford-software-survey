#!/usr/bin/env python

import argparse
from collections import defaultdict
import csv
import json
import os
import sys

root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
multiple_choice_fields = ["Have you ever included costs for software development in a funding proposal?"]

def get_parser():

    parser = argparse.ArgumentParser(description="Prepare csv data file")

    parser.add_argument("input", help="input csv script")
    parser.add_argument(
        "--delim",
        dest="delim",
        help="File separator (defaults to , for csv)",
        default=",",
    )
    parser.add_argument(
        "--outdir",
        dest="outdir",
        help="Output directory (defaults to _data, must be relative to scripts folder)",
        default=os.path.join(root, "_data"),
    )
    return parser


def write_json(filename, obj):
    """write json to file, with pretty print"""
    with open(filename, "w") as fd:
        fd.write(json.dumps(obj, indent=4))
    return filename


def read_rows(filepath, newline="", delim=","):
    """read in the data rows of a csv file."""
    # Read in the entire membership counts
    with open(filepath, newline=newline) as infile:
        reader = csv.reader(infile, delimiter=delim)
        data = [row for row in reader]
    return data


def validate_rows(rows):
    """ensure that rows are defined (not an empty list) and each is equal length"""
    if not rows:
        sys.exit("The data file is empty.")
    length = len(rows[0])
    if any([len(x) != length for x in rows]):
        sys.exit("All rows must have equal length.")


def rows_to_dict(rows):
    """Given a csv format, convert to dictionary. We could easily do that with
    pandas or similar but I'd rather not add an extra dependency.
    """
    # Header (and keys) are the first row
    header = rows.pop(0)

    data = {}
    for idx, key in enumerate(header):

        # special case multiple choice
        if key in multiple_choice_fields:
            values = []
            for row in rows:
                for entry in row[idx].split(';'):
                    if not entry:
                        continue
                    values = values + [entry]
        else:
            values = [x[idx] for x in rows if x[idx]]

        # Remove any [] from the key
        key = key.replace('[','').replace(']', '').strip()
        counts = defaultdict(lambda: 0)
        for value in values:
            counts[value] += 1
        data[key] = {"values": values, "counts": dict(counts)}

    return data


def main():
    """main entrypoint for generating data output file"""

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    for name in [args.input, args.outdir]:
        if not name or not os.path.exists(name):
            sys.exit("%s does not exist." % name)
    
    # Read rows and ensure that all are equal length
    rows = read_rows(args.input, delim=args.delim)
    validate_rows(rows)

    # Organize results by header fields as keys, add counts
    data = rows_to_dict(rows)

    # Output file is same name with json, but not in raw folder
    basename = "%s.json" % os.path.basename(os.path.splitext(args.input)[0])
    filename = os.path.join(args.outdir, basename)
    print("Writing output to %s" % filename)
    write_json(filename, data)


if __name__ == "__main__":
    main()
