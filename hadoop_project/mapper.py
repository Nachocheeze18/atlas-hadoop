#!/usr/bin/env python3
"""Import"""
import csv
import sys

reader = csv.reader(sys.stdin, delimiter=',')
for row in reader:
    if len(row) >= 4:
        print(str(row[0]) + '\t' + str(row[1]) + ',' + str(row[3]))
