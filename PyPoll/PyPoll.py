#Got help from tutor and co-pilot
#import the csv importer module from the python library
import csv

id = []
candidate_dict = {

}

total_votes = 0
winner = ''
winner_votes = 0

#name our csv_file dataset by the file name (not file path)
csv_file = 'election_data.csv'

with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        candidate = row[2]
        if not candidate in candidate_dict:
            candidate_dict[candidate] = 0
        candidate_dict[candidate] += 1

candidate_count = len(candidate_dict)
candidate_count

print(candidate_dict)

total_votes = sum(candidate_dict.values())
print(total_votes)
lines = []
lines.append('Election Results')
lines.append('-------------------------')
lines.append(f'Total Votes: {total_votes}')
lines.append('-------------------------')



for candidate, votes in candidate_dict.items():
    vote_pct = votes / total_votes
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
    lines.append(f'{candidate}: {vote_pct:.3%} ({votes})')

lines.append('-------------------------')
lines.append(f'Winner: {winner}')
lines.append('-------------------------')

print('\n'.join(lines))

with open('election_results.txt', 'w') as txt_file:
    txt_file.write('\n'.join(lines))