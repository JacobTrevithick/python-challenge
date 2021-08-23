import os
import csv
# import statistics as stat

def average(num_list):
    return sum(num_list) / len(num_list)

def get_changes(num_list):
    '''
    Adapted function for finding the next value in a list using enumerate method.

    Code adapted from Kite online coding resource:
    https://www.kite.com/python/answers/how-to-access-previous-and-next-values-when-looping-through-a-list-in-python#:~:text=Use%20enumerate()%20to%20access,list%5Bindex%2D1%5D%20.
    '''
    change_list = []
    for index, num in enumerate(num_list):
        if index -1 >= 0:
            change_list.append(num_list[index] - num_list[index - 1])
    return change_list


budget_data_csv = os.path.join("Resources", 'budget_data.csv')

with open(budget_data_csv, 'r') as csv_file:
    
    budget_data = csv.reader(csv_file, delimiter = ',') 

    # total_months = len(list(budget_data)) - 1
    total_months = 0
    net_profit = 0
    profit_list = []
    month_list = []

    csv_header = next(budget_data, None)

    for row in budget_data:
        
        total_months += 1
        net_profit += int(row[1])

        month_list.append(row[0])
        profit_list.append(int(row[1]))

profit_changes = get_changes(profit_list)
avg_change = round(average(profit_changes), 2)

print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {month_list[profit_changes.index(max(profit_changes)) + 1]} (${max(profit_changes)})")
print(f"Greatest Decrease in Profits: {month_list[profit_changes.index(min(profit_changes)) + 1]} (${min(profit_changes)})")