#importing os and csv libraries to handle files
import os
import csv

#creating budget_data_csv file object
poll_csv = os.path.join("Resources", 'election_data.csv')

#open budget file object as csv file
with open(poll_csv, 'r') as csv_file:
    
    #create csv reader object to iterate through months
    poll_data = csv.reader(csv_file, delimiter = ',') 

    #skip header row
    csv_header = next(poll_data, None)

    total_votes = 0
    cand_dict = {}

    for row in poll_data:
        
        total_votes += 1

        if row[2] not in cand_dict:
            cand_dict[row[2]] = [1]
        else:
            cand_dict[row[2]][0] += 1

    # for loop doing two things: finding the winner and calc'ing/adding the percentage of votes to candidate dict

winner_total = 0
for candidate in cand_dict:
    
    if cand_dict[candidate][0] > winner_total:
        winner_total = cand_dict[candidate][0]
        winner = candidate
    
    cand_percent = float(cand_dict[candidate][0]/total_votes) * 100
    cand_dict[candidate].append(cand_percent)

'''
Terminal Printing: vote percentages for each candidate are forced to round to .000% place
'''

print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
for cand in cand_dict:
    print("{}: {:.3f}% ({})".format(cand, cand_dict[cand][1], cand_dict[cand][0]))
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)


#creating financial analysis text file 
election_results = os.path.join("analysis", 'election_results.txt')

with open(election_results, 'w') as txt_file:
    
    #Write election report to text file.

    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("---------------------------------------\n")
    for cand in cand_dict:
        txt_file.write("{}: {:.3f}% ({})\n".format(cand, cand_dict[cand][1], cand_dict[cand][0]))
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("---------------------------------------\n")

    txt_file.close()