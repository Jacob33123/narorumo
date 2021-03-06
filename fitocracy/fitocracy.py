#!/usr/bin/env python3

"""
Use this script to find out how many miles you've logged in total on Fitocracy! 

Go to your profile > History > Running, then click CSV. It will produce, in
your browser, a bunch of CSV data. Save that to a file, then run this script on
that file!

Should work both under recent Python 2 and Python 3.
"""

from __future__ import print_function
from __future__ import division
import csv
import sys

multiplier_table = { "mi": 1.0,
                     "km": 0.621371192,
                     "ft": (1 / 5280),
                     "m": 0.000621371192,
                     "yd": (1 / 1760) }

def to_miles(dist, units):
    asfloat = float(dist)
    multiplier = multiplier_table[units]
    return asfloat * multiplier

def find_dist_unit(text):
    for unit in multiplier_table.keys():
        if (" " + unit) in text:
            return unit

def total_miles_from_text(text, verbose=False):
    lines = text.split("\n")
    csvReader = csv.reader(lines)
    total_miles = 0
    headers = next(csvReader)
    combinedIndex = headers.index("Combined")
    distIndex = 5
    dateIndex = headers.index("Date (YYYYMMDD)")

    for row in csvReader:
        if len(row) <= min(distIndex, combinedIndex): continue
        dist = row[distIndex]
        distunit = find_dist_unit(row[combinedIndex])
        date = row[dateIndex]
        if(dist):
            miles = to_miles(dist, distunit)
            if verbose:
                print("on", date, "did this many miles:", miles)
            total_miles += miles
    return total_miles

def main():
    if len(sys.argv) != 2:
        print("usage: python3 {0} myrunningstats.csv".format(sys.argv[0]))
        return
    with open(sys.argv[1], "r") as infile:
        text = infile.read()
        total_miles = total_miles_from_text(text)
        print("You have gone this many miles on Fitocracy:", total_miles)

if __name__ == "__main__": main()
