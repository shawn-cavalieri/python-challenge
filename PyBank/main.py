import os
import csv

# read in the csv file

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)
    
    # create lists to hold values

    months = []
    revenue = []
    current_month_revenue = []
    previous_month_revenue = []
    revenue_change = []

    # for loop to append lists
    
    for row in csvreader:
        months.append(row[0])
        revenue.append(row[1])
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
  
    x = 0
    for x in range(len(revenue) - 1):
        profit_loss = int(revenue[x+1]) - int(revenue[x])
        revenue_change.append(profit_loss)
    total = sum(revenue_change)
    monthly_change = total / len(revenue_change)

    y = 0
    greatest_increase = max(revenue_change)
    y = revenue_change.index(greatest_increase)
    month_increase = months[y+1]
    
    z = 0
    greatest_decrease = min(revenue_change)
    z = revenue_change.index(greatest_decrease)
    month_decrease = months[z+1]


# write to a text file  

text_file = """
    Financial Analysis
-----------------------------
Total number of months: {months}
Total: ${total_revenue}
Average Change = ${monthly_change:.2f}
Greatest Increase in Profits: {month_increase} (${greatest_increase})
Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})
""".format(months=months, total_revenue=total_revenue, monthly_change=monthly_change, greatest_increase=greatest_increase,
    greatest_decrease=greatest_decrease, month_increase=month_increase, month_decrease=month_decrease)

print(text_file)
with open('summary.txt', 'w') as outfile:
    outfile.write(text_file)

   


