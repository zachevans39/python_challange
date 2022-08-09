import os
import csv
from unittest import result




poll_csv = os.path.join('election_data.csv')

num_votes=0
candidates_choices = []
candidates_votes = {}
win_total =0
win_percent=0

with open(poll_csv) as csvfile:
    csv_reader= csv.reader(csvfile, delimiter=",")
    row = next(csv_reader)

    for row in csv_reader:
        num_votes += 1
        candidate_name = row[2] 
        if candidate_name not in candidates_choices:
            candidates_choices.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] += 1
    for candidate_name in candidates_votes:
        votes = candidates_votes.get(candidate_name)
        vote_percentage = float(votes) / float(num_votes) * 100
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
        print(candidate_results)
        if (votes > win_total) and (vote_percentage > win_percent):
            win_total = votes
            winning_candidate = candidate_name
            win_percent = vote_percentage

    winner = (f"The winner is:{winning_candidate}")      
    
          


    print(f"Total Votes: {num_votes}")
    print(winner)  
