
# The total number of months included in the dataset
import os
import csv
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    totalmonths = 0
    totalprofit = 0
    headers = next(csvreader)
    month = []
    profit = []
    monthlyprofitchange = []
  
    for row in csvreader:
        print (row)
        totalmonths = totalmonths + 1
        totalprofit = totalprofit + int(row[1])
        totalmonths.append(row[0])
        totalprofit.append(int(row[1])

        

print(totalmonths)
print(totalprofit)
print(totalprofit/totalmonths)
print(row[0])
print(row[1])




# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period