# imported csv to read the csv file
import csv

# created path for an input
read_path = '/Users/noahsuskin/Desktop/Rutgers_DataScienceBootcamp/Python/Python-Challenge/' \
            'PyPoll/Resources/election_data.csv'

# Created path to store answer as a txt
output_path = '/Users/noahsuskin/Desktop/Rutgers_DataScienceBootcamp/Python/Python-Challenge/' \
            'PyPoll/Analysis/Analysis.txt'

# Created a variable to counter number of votes
num_of_votes = 0
# Created a list to hold each different candidate that received votes
candidate_lst = []
# Created a list to count how many votes each candidate had (votes are matched with candidate list by index
vote_lst = []
# Created a list to hold the data from the csv file to manipulate easier
data_lst = []

# Opened file and extracted necessary information
with open(read_path, 'r') as datafile:
    data = csv.reader(datafile)
    headers = next(data)
    # print(headers)
    for row in data:
        data_lst.append(row)
        num_of_votes += 1
        if row[2] not in candidate_lst:
            candidate_lst.append(row[2])

# looped through candidate list and data list to count each vote for each candidate
for candidate in candidate_lst:
    vote_count = 0
    for vote in data_lst:
        if candidate == vote[2]:
            vote_count += 1
    vote_lst.append(vote_count)

# calculated percent of vote
percent_votes = []
for vote in vote_lst:
    percent = round(((vote/num_of_votes) * 100), 2)
    percent_votes.append(percent)

# found max value in vote list
max_value = max(vote_lst)
# found index to match with the name of candidate
max_index = vote_lst.index(max_value)
# saved the candidate name with the most votes to a variable
winner = candidate_lst[max_index]


# Saved all information to a string that prints to the terminal
answer_string = f"Election Results\n" \
                f"-----------------------------\n" \
                f"Total Votes: {num_of_votes} \n" \
                f"-----------------------------\n" \
                f"{candidate_lst[0]}: {percent_votes[0]}% ({vote_lst[0]})\n" \
                f"{candidate_lst[1]}: {percent_votes[1]}% ({vote_lst[1]})\n" \
                f"{candidate_lst[2]}: {percent_votes[2]}% ({vote_lst[2]})\n" \
                f"{candidate_lst[3]}: {percent_votes[3]}% ({vote_lst[3]})\n" \
                f"---------------------------------------------------------------\n" \
                f"Winner: {winner} \n" \
                f"---------------------------------------------------------------"

print(answer_string)
# --------------------------------------------------------------------------------------------------------

# wrote a txt file and saved to the analysis folder containing the information from the answer string
with open(output_path, 'w') as answer_file:
    answer_file.write(answer_string)

