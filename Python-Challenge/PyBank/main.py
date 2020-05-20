# imported csv module to help read in csv data
import csv

# created a path to read the budget_data.csv
data_path = '/Users/noahsuskin/Desktop/Rutgers_DataScienceBootcamp'\
                    '/Python/Python-Challenge/PyBank/Reasources/budget_data.csv'

# created a path where I wanted my txt file to go
output_data_path = '/Users/noahsuskin/Desktop/Rutgers_DataScienceBootcamp'\
                    '/Python/Python-Challenge/PyBank/Analysis/Financial_Analysis.txt'

# looped through data to find total number of months and total amount of money over the period
# Appended profit/loss values into a new list so I could perform calculations easier
counter = 0
total_amount = 0
value_lst = []
num_lst = []
change_lst = []
with open(data_path, 'r') as file:
    data = csv.reader(file, delimiter=',')
    headers = next(data)
    # print(headers)
    for row in data:
        # print(row)
        counter += 1
        total_amount += int(row[1])
        num_lst.append(int(row[1]))
        value_lst.append(row)


# print(num_lst)
# looped through number profit/loss list to find the changes in profit/loss values for each month
for i in range(len(num_lst)):
    if i == len(num_lst) - 1:
        break
    else:
        change = num_lst[i + 1] - num_lst[i]
        change_lst.append(change)

# Found max & min values in profit/loss and saved to a variable
# calculated average change and saved to a variable
# print(change_lst)
max_change = max(change_lst)
min_change = min(change_lst)
sum_of_changes = sum(change_lst)
average_change = round((sum_of_changes/len(change_lst)), 2)

# found index of max and min values to help find the date on which the values happened
max_change_index = change_lst.index(max_change)
min_change_index = change_lst.index(min_change)

# Found date by referencing the index and adding one because of the difference in the length of lists
max_date = value_lst[max_change_index + 1][0]
min_date = value_lst[min_change_index + 1][0]
# print(max_date)
# print(min_date)

# Created a string that summarized the answers that related to the instructions
answer_string = f"Financial Analysis \n" \
                f"---------------------------------------------- \n" \
                f"Total Months: {counter} \n" \
                f"Total: ${total_amount} \n" \
                f"Average Change: ${average_change} \n" \
                f"Greatest Increase in Profits: {max_date} ({max_change}) \n" \
                f"Greatest Decrease in Profits: {min_date} ({min_change})"

# printed answer to the terminal
print(answer_string)

# exported a text file that contained the answer string
with open(output_data_path, 'w') as new_datafile:
    new_datafile.write(answer_string)

