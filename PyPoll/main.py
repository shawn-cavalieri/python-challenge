import os
import csv

# read in the csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# create variables to hold totals and percents

total = 0
khan = 0
correy = 0
li = 0
o_tooley = 0
khan_pct = 0
correy_pct = 0
li_pct = 0
o_tooley_pct = 0

# assign votes to candidates

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)

    for row in csvreader:
        total += 1
        if row[2] == 'Khan':
            khan += 1
        elif row[2] == 'Correy':
            correy += 1
        elif row[2] == 'Li':
            li += 1
        else:
            o_tooley += 1

# identify percentage of votes

khan_pct = (khan/total)*100
correy_pct = (correy/total)*100
li_pct = (li/total)*100
o_tooley_pct = (o_tooley/total)*100

# write an if statement to identify the winner

if int(khan) > int(correy) and int(khan) > int(li) and int(khan) > int(o_tooley):
    winner = "Khan"
elif int(correy) > int(khan) and int(correy) > int(li) and int(correy) > int(o_tooley):
    winner = "Correy"
elif int(li) > int(correy) and int(li) > int(khan) and int(li) > int(o_tooley):
    winner = "Li"
else:
    winner = "O'Tooley"

# write to a text file    

text_file = """
    Election Results
--------------------------
Total Votes: {total}
--------------------------
Khan: {khan_pct:.1f}% ({khan})
Correy: {correy_pct:.1f}% ({correy})
Li: {li_pct:.1f}% ({li})
O'Tooley: {o_tooley_pct:.1f}% ({o_tooley})
--------------------------
    Winner: {winner}
-------------------------- """.format(total=total, khan=khan, khan_pct=khan_pct, correy=correy, correy_pct=correy_pct, 
li=li, li_pct=li_pct, o_tooley=o_tooley, o_tooley_pct=o_tooley_pct, winner=winner)

print(text_file)
with open('summary.txt', 'w') as outfile:
    outfile.write(text_file)