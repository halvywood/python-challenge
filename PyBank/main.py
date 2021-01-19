# import os and csv modules
import os
import csv

months = 0


# define the csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    row = next(csvreader)

    months += 1
    total = 0
    previous_amount = int(row[1])
    monthly_change = []
    monthly_count = []
    greatest_increase = 0
    greatest_increase_month = 0
    greatest_decrease = 0
    greatest_decrease_month = 0

    # Total months, total profit loss, and variables for rows
    # Read each row
    for row in csvreader:
        # print(row)
        revenue = int(row[1]) 
        # print(revenue)
        total += revenue
        # print(total)
        months += 1
        # print(months)


        amount_change = int(row[1]) - previous_amount
        monthly_change.append(amount_change)
        previous_amount = int(row[1])
        monthly_count.append(row[0])

        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            # print(greatest_increase)
            greatest_increase_month = row[0]
            # print(greatest_increase_month)
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            # print(greatest_decrease)  
            greatest_decrease_month = row[0]
            # print(greatest_decrease_month)  
        
    # Avg. and Date
    average_change = sum(monthly_change)/ len(monthly_change)
    x = round(average_change,2)
    # print(average_change)
    
    most = max(monthly_change)
    # print(most)
    least = min(monthly_change)
    # print(least)
        
# --------------------------------------------------------
# prints
print("Financial Analysis")
print("-------------------------------")

print(f"Total Months:  {months}")
print(f"Total:  ${total}")
print(f"Average Change:  ${x}")
print(f"Greatest Increase in Profits:  {greatest_increase_month}, (${most})")
print(f"Greatest Decrease in Profits:  {greatest_decrease_month}, (${least})")