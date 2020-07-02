import csv
import sys

orig_content = sys.stdout
f = open('PyPoll.txt',  'w')
sys.stdout = f

#opening csvfile and assigning it to pointer 'csvfile'.
with open("Resources/election_data.csv", "r") as csvfile:
    csvreader =csv.reader(csvfile)
    #Disregarded the header using this conditional as it is invalid data.
    next(csvreader)

    #Using a counter to tally and cand to keep dictionary of each candidate and their votes.
    votes = 0
    cand = {}
    
    #Created 2 for loops to loop through the columns and rows.
    for row in csvreader:

        #votes counts the total number of votes.
        votes += 1

        #Used conditional to check if the candidate is already listed in the dictionary.
        #If not added to 'cand' and then assigned value of 1 as a count to tally number of votes for each.
        #I also updated its value everytime it came across the repeated name in dict.
        if row[2] not in cand:
            cand[row[2]] = 1
        else:
            cand[row[2]] += 1
                    
    #Results in desired format
    print("Election Results")
    print("-------------------------")
    print("Total Votes:",votes)
    
    #Loop gets individal key/value pair from dict and creates percentage of votes for each candidate.
    #NOTE: pw stands for previous winner, cw stands for current winner.
    
    #set previous winner = 0 because no preceeding value.
    pw = 0
    
    for key, value in cand.items():
        
        percent = percent = "{0:.0%}".format(value/votes)
        
        #current winner = value since it is the current value we are working with.
        cw = value
        
        #Comparing each candidates votes by looking at its value.
        if cw > pw:
            winner_val = cw
            
            #setting current value to previous value every time after each loop runs.
            pw = cw
            
            #checking winner_value with original value in dict to get the corresponding key.
            if winner_val == value:
                winner = key
            
        else:
            winner_val = pw
            if winner_val == value:
                winner = key
                
        #Also the loop prints the total votes and percent of votes for 
        #each as previously calculated.
        print(key + ":", percent , "(" + str(value) + ")")
    
    print("-------------------------")
    print("Winner:", winner)
    print("-------------------------")

sys.stdout = orig_content
f.close()