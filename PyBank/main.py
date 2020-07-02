import csv
import sys

orig_content = sys.stdout
f = open('PyBank.txt',  'w')
sys.stdout = f

#open designated 
with open("Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    #initialize monthly counter, PL(Profit/Loss) list, profitSum
    month_count = 0
    PL = []
    profitSum = 0
    d = {}
    datelist = []
    diffl = []

    #greatI = ["",0]
    #greatD = ["",999999]

    greatI = 0
    greatD = 0
    diff2 = 0

    #loop to go through each column (col) and row
    for row in csvreader:
        #To neglect the first header 'date' and 'profit/losses'
        #iterate month_count, append PL to PL list, and assigning values to directory
        month_count += 1
        PL.append(int(row[1]))
        d[row[0]] = int(row[1])
        datelist.append(row[0])
    
    #initialize diff, difference count
    diff = 0
    diffcount = 0
    
    #loop calculates the average change by finding the difference between each of the values and sums the values
    #into diff and keeps a diff count to find average change
    for i in range(len(PL)-1):
        diff += (PL[i+1] - PL[i])
        diff2 = (PL[i+1] - PL[i])
        diffl.append(diff2)

        # Greatest Increase in profits
        if diff2 > greatI:
            greatI = diff2
            Increasedate = datelist[i+1]
        if diff2 < greatD:
            greatD = diff2
            Decreasedate = datelist[i+1]

        diffcount += 1
    
    AvgCh = diff / diffcount

    #Loop Tallies the total sum
    for i in range(len(PL)):
        profitSum = profitSum + PL[i]
    
    #print desired values
    print("Financial Analysis")
    print("------------------------------")
    print("Months:", month_count)
    print("Total: $" + str(profitSum))
    print("Average Change: $" + str(round(AvgCh, 2)))
    print("Greatest Increase in Profits: $" + str(greatI), "(" + str(Increasedate) + ")")
    print("Greatest Decrease in Profits: $" + str(greatD), "(" + str(Decreasedate) + ")")

sys.stdout = orig_content
f.close()