import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader) #remove header
    #create variables and then assign values to them 
    voters=[]
    candidates=[] 
    vote_counter=0
    vote_percent=[]
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            voters.append(1) #bring in the first voter 
        else:
            #not sure if we went over it in class - I had to look up how to return the index of a list
            candidate_index=candidates.index(row[2]) 
            voters[candidate_index]=voters[candidate_index]+1
        vote_counter=vote_counter+1
    
    for votes in voters:
        percentages=(votes/vote_counter)*100
        vote_percent.append(percentages)

    #Determine the winner
    percent=0
    for value in vote_percent:
        if value>percent:
            percent=value
            #use index instead of incrementing the position because the winner is in a different list
            position=vote_percent.index(value) 
            winner=candidates[position]

# print results
analysis=(
f'Election Results\n'
f'----------------------------\n'
f'Total Votes: {vote_counter}\n'
f'----------------------------\n'
f'{candidates[0]}: {vote_percent[0]:.3f}% ({voters[0]})\n' #interesting syntax for decimal places 
f'{candidates[1]}: {vote_percent[1]:.3f}% ({voters[1]})\n'
f'{candidates[2]}: {vote_percent[2]:.3f}% ({voters[2]})\n'
f'{candidates[3]}: {vote_percent[3]:.3f}% ({voters[3]})\n'
f'----------------------------\n'
f'Winner: {winner}\n'
f'----------------------------\n'
)

print(analysis)

#Write to txt file
pypoll_analysis=os.path.join('.','Analysis', 'analysis.txt')
with open(pypoll_analysis, 'w') as txt_file:
     txt_file.write(analysis)

