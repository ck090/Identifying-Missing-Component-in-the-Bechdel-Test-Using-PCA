import json
import requests
import csv

# URL 
url = 'http://bechdeltest.com/api/v1/getAllMovies'

# Get response for getting all the movie lists
response = requests.get(url)
json_data = json.loads(response.text)

# Length of the entire Bechdel test approved movies
print(len(json_data))

filename = "Bechdel_Approved.csv"

def write_csv(data, filename):
    print("Writing..")
    with open(filename, 'wt') as csv_file:
        writer = csv.DictWriter(csv_file, data[0].keys())
        print(data[0].keys(), data[1].keys(), data[0].values())
        writer.writeheader()
        for row in data:
            print(row)
            writer.writerow(row)
        # for index in range(len(json_data)):
        #     writer.writerow((data[index].values()))

write_csv(json_data, filename)