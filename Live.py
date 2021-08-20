from datetime import date
from nsepy import get_history
import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = "ind_nifty100list.csv"
symbols = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 
    for row in csvreader:
        symbols.append(row[2])

n = len(symbols)
symbols = symbols[1:n]
n = len(symbols)
print(n)
