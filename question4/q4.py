import csv

with open('output.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    with open('country_vaccination_stats.csv', 'r') as input:
        reader = csv.reader(input)
        # write header row
        header = next(reader)
        writer.writerow(header)
        # write data rows
        for row in reader:
            writer.writerow(row)
