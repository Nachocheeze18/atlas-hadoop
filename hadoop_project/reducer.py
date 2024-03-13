#!/usr/bin/env python3
"""Imports"""
import sys

top_salaries = []

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    id_number, salary, company = fields
    salary = float(salary)
    top_salaries.append((salary, id_number, company))
    top_salaries.sort(reverse=True)
    top_salaries = top_salaries[:10]

for salary, id_number, company in top_salaries:
    print(f"{id_number}\t{salary}\t{company}")
