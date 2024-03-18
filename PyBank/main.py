import os
import csv

#path for resource file
bank_csv = os.path.join('Resources','budget_data.csv')

#opening file and reader
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)

    
    date =[]
    profit_loss =[]
    changes =[]

    for row in csvreader:
        profit_loss.append(row[1])
        date.append(row[0])

       
cleaned_bank = list(zip(date,profit_loss,changes))
        

#calculating total number of months
total_months = len(date)

print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(total_months))

#calculating total profit/losses
def sumtotal(profit_loss):
    total = 0
    for number in profit_loss:
        total += int(number)  
    return total

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

summary_statement = """
Financial Analysis       
----------------------------------       
Total Months: 86        
Total: $ 22564198                 
Average Change: $  -8311.11                             
Greatest Increase in Profits:  Aug-16 ( 1862002 )           
Greatest Decrease in Profits:  Feb-14 ( -1825558 )"""

filename = "results.txt"

results_path = os.path.join("Analysis", "results.txt")

with open(results_path, "w") as f:

    f.writelines(summary_statement) 
    f.close   




 







