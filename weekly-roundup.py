import csv
import os

# initialize variables
output_file = 'weekly-roundup.csv'
total_calls = 0
call_counts = {}

# loops through each CSV file in the current directory (this will be a collection of everyones daily calls)
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Total calls':
                    total_calls += int(row[1])
                else:
                    call_counts[row[0]] = call_counts.get(row[0], 0) + int(row[1])

# write the data to the weekly output file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Total Calls', total_calls])
    for call_type, count in call_counts.items():
        writer.writerow([call_type, count])

print(f'Weekly roundup data has been written to {output_file}')