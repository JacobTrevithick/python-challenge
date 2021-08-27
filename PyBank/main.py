#importing os and csv libraries to handle files
import os
import csv


def average(num_list):
    '''
    Gets average of all values in a list
    '''
    return sum(num_list) / len(num_list)

def get_changes(num_list):
    '''
    Adapted function for finding the next value in a list using enumerate method.

    Take the difference between the current and previous value in list, and append that to a new 'change_list'. Does not calculate for very first number in the list

    Code adapted from Kite online coding resource and from in class example:
    https://www.kite.com/python/answers/how-to-access-previous-and-next-values-when-looping-through-a-list-in-python#:~:text=Use%20enumerate()%20to%20access,list%5Bindex%2D1%5D%20.
    '''
    change_list = []
    for index, num in enumerate(num_list):
        if index - 1 >= 0:
            change_list.append(num_list[index] - num_list[index - 1])
    return change_list

#creating budget_data_csv file object
budget_data_csv = os.path.join("Resources", 'budget_data.csv')

#open budget file object as csv file
with open(budget_data_csv, 'r') as csv_file:
    
    #create csv reader object to iterate through months
    budget_data = csv.reader(csv_file, delimiter = ',') 

    total_months = 0
    net_profit = 0
    profit_list = []
    month_list = []

    #skip header row
    csv_header = next(budget_data, None)

    #iterate through each month
    for row in budget_data:
        
        #count total months and sum total profits/losses
        total_months += 1
        net_profit += int(row[1])

        #populating list of months and list of profit values to use later
        month_list.append(row[0])
        profit_list.append(int(row[1]))

'''
calc profit changes from month-to-month using get_changes function.
average those changes and round to 2 decimal places
Month corresponding to greatest increase and decrease are found by retrieving the index of the max/min profit change and corresponding that to the month_list.
Note: month_list index must be +1 because profit change not calc'd for first month.
'''

profit_changes = get_changes(profit_list)
avg_change = round(average(profit_changes), 2)

max_profit_val = max(profit_changes)
max_profit_month = month_list[profit_changes.index(max_profit_val) + 1]

min_profit_val = min(profit_changes)
min_profit_month = month_list[profit_changes.index(min_profit_val) + 1]


'''
Terminal Printing:
'''

print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_val})")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit_val})")


#creating financial analysis text file 
financial_analysis_file = os.path.join("analysis", 'Financial_Analysis.txt')

with open(financial_analysis_file, 'w') as txt_file:
    
    #Write financial report to text file.

    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_profit}\n")
    txt_file.write(f"Average Change: ${avg_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_val})\n")
    txt_file.write(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit_val})")

    txt_file.close()