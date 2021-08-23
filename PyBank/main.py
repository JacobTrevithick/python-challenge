import os
import csv
# import statistics as stat

def get_changes(num_list):
    '''
    Adapted function for finding the next value in a list using enumerate method.

    Code adapted from this Kite online coding resource:
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

    csv_header = next(budget_data, None)


    for row in budget_data:
        
        total_months += 1
        net_profit += float(row[1])
        profit_list.append(float(row[1]))

    profit_changes = get_changes(profit_list)
    print(max(profit_changes))
    print(min(profit_changes))
    # print(stat.mean(profit_changes))
    print(net_profit)
    print(total_months)




