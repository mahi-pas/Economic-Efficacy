import csv
import glob

def merge_files(output_file, input_files):
    data = {}
    headers = ["STATE"]

    # Load state to state code mapping
    state_to_code = {}
    with open('MyData/state_to_statecode.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            state_to_code[row[0]] = row[1]

    for file in input_files:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            if header[0].upper() == "STATE":
                headers.extend(header[1:])
                for row in reader:
                    state = row[0]
                    if state in state_to_code:
                        if state not in data:
                            data[state] = row[1:]
                        else:
                            data[state].extend(row[1:])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for state in sorted(data.keys()):
            writer.writerow([state] + data[state])

if __name__ == '__main__':
    input_files = glob.glob('Data/*.csv') + glob.glob('MyData/*.csv')
    merge_files('MyData/merged_data.csv', input_files)

