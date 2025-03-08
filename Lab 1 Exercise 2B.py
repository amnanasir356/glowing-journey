def read_earthquake_data(file_path):
    earthquake_data = {}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                parts = line.strip().split()
                magnitude, date, time, latitude, longitude, depth, *region = parts
                region = ''.join(region)

                # Combine all Alaska entries into a single entry
                if 'ALASKA' in region:
                    region = 'ALASKA'

                if region not in earthquake_data:
                    earthquake_data[region] = []

                earthquake_data[region].append([date, float(magnitude)])
            except ValueError:
                print(f"Error parsing line {line_number}: {line}")
                continue

    return earthquake_data


def write_formatted_data(file_path, earthquake_data):
    with open(file_path, 'w') as file:
        for region, data in earthquake_data.items():
            formatted_data = f"[{region.upper()}, {[f'{entry[0]}, {entry[1]}' for entry in data]}]"
            file.write(formatted_data.replace("'", "") + '\n')


if __name__ == "__main__":
    earthquake_file_path = "earthquake.txt"
    output_file_path = "earthquakefmt.txt"

    data = read_earthquake_data(earthquake_file_path)
    write_formatted_data(output_file_path, data)

    
