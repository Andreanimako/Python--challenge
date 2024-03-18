import os
import csv

#outlining path for resource file
bank_csv = os.path.join('Resources','budget_data.csv')

#opening file and reader and storing header row
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)

   #creating lists for reference 
    date =[]
    profit_loss =[]
    changes =[]

    for row in csvreader:
        profit_loss.append(row[1])
        date.append(row[0])
       

#calculating total number of months
total_months = len(date)

#printing results
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(total_months))

#calculating total profit/losses by defining a function
def sumtotal(profit_loss):
    total = 0
    for number in profit_loss:
        total += int(number)  
    return total

#printing total profit/loss
print("Total: $",sumtotal(profit_loss) )



#calculating changes in profit/loss by converting strings to float
for i in range(1, len(profit_loss)):
    current_profit = float(profit_loss[i])
    previous_profit = float(profit_loss[i-1])
    dailychange = current_profit - previous_profit
    changes.append(dailychange) 

  
# determining greatest increase and greaest decraese in profit/loss
max_changes = max(changes)

min_changes = min(changes)


#printing average changes, greatest increase and greatest derease and rounding off results
print("Average Change: $ ",round(sum(changes)/len(changes), 2))
print("Greatest Increase in Profits: ",str(date[changes.index(max_changes)+1]),"(",round(max_changes),")")
print("Greatest Decrease in Profits: ",str(date[changes.index(min_changes)+1]),"(",round(min_changes),")")

#setting text for text file as a variable
summary_statement = """
Financial Analysis       
----------------------------------       
Total Months: 86        
Total: $ 22564198                 
Average Change: $  -8311.11                             
Greatest Increase in Profits:  Aug-16 ( 1862002 )           
Greatest Decrease in Profits:  Feb-14 ( -1825558 )"""

#creating new file and file path
filename = "results.txt"

results_path = os.path.join("Analysis", "results.txt")

#writing new reults file
with open(results_path, "w") as f:

    f.writelines(summary_statement) 
    f.close   




 







