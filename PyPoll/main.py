import os
import csv

#impoting csv by creating fle path
poll_path = os.path.join("Resources","election_data.csv")

#opening csv file
with open(poll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    Ballot_ID = []
    County = []
    Candidate = []
    candidatelist = []

    for row in csvreader:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

 #calculating total number vites cast
    total_votes = len(Ballot_ID) 

    for name in Candidate:
        if name in candidatelist:
            pass
        else:
            candidatelist.append(name)
    
    #calculating number of votes for each candidate
    def candidate_votes(name): 
        votes = 0
        for item in Candidate:
            if item == name:
                votes = votes+ 1
        return votes        
        #print (name,":",votes," votes")     

    
    charles_votes =candidate_votes("Charles Casper Stockham")
    diana_votes = candidate_votes("Diana DeGette")
    raymon_votes = candidate_votes("Raymon Anthony Doane")

    #calculaing percentage of votes
    Charles_percent = round((candidate_votes("Charles Casper Stockham")/ total_votes)*100, 3)
    Diana_percent = round((candidate_votes("Diana DeGette")/ total_votes)*100, 3)
    Raymon_percent = round((candidate_votes("Raymon Anthony Doane")/ total_votes)*100, 3)

    candidate_Percent_votes ={"Charles Casper Stockham":Charles_percent,"Diana DeGette": Diana_percent,"Raymon Anthony Doane":Raymon_percent}

    #print(candidate_Percent_votes)
    
    #winner will be the highest perentage votes
    winner = max(candidate_Percent_votes)

    print("Election Results")
    print("-------------------------------")
    print("Total votes: ", total_votes)
    print("-------------------------------")
    print("Charles Casper Stockham: ",Charles_percent,"%","(",charles_votes,")")
    print("Diana DeGette: ",Diana_percent,"%","(",diana_votes,")")
    print("Raymon Anthony Doane: ",Raymon_percent,"%","(",raymon_votes,")")
    print("-------------------------------")
    print("Winner: ","Diana DeGette")
    print("-------------------------------")


# exporting resilts summary in text file in Analysis folder
summary_statement = """Election Results
-------------------------------
Total votes:  369711
-------------------------------
Charles Casper Stockham:  23.049 % ( 85213 )
Diana DeGette:  73.812 % ( 272892 )
Raymon Anthony Doane:  3.139 % ( 11606 )
-------------------------------
Winner:  Diana DeGette
-------------------------------"""

filename = "election_results.txt"

election_path = os.path.join ("Analysis", "election_results.txt")

with open (election_path, "w") as f:

    f.writelines(summary_statement)

    f.close
    

    

    
   
    
        
