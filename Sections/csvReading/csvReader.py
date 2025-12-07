import csv

with open('pokemon.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Process each subsequent row (as a dictionary)
        print(row['name']) # Access by header name