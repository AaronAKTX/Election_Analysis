import os
import csv

csv_path = os.path.join ("Resources","netflix_ratings.csv")
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader (csv.reader(csvfile, delimiter=","))


