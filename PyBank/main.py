import os   
import csv

PyBankpath = os.path.join('Resources', 'budget_data.csv')

# Opening the following csv file to read specfic data

with open(PyBankpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Taking off the header from the 1st row
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}") #  ---> Can be used to print the header if needed

# Creating separate lists to store specific functions

    Profit = []
    Months = []


# Creating a loop to store specific values in the list above
    for rows in csvreader:
        Profit.append(int(rows[1]))
        Months.append(rows[0])

    # Storing variables in a separate list for change in revenue
    revenue_change = []

    # Start a loop to go through the change in values
    for x in range(1, len(Profit)):
        revenue_change.append((int(Profit[x]) - int(Profit[x-1])))

    # Calculating the average revenue change
    average_revenue = sum(revenue_change) / len(revenue_change)

    # Calculating the total # of months
    month_total = len(Months)

    # Calculating the greatest increase in revenue
    greatest_profit_increase = max(revenue_change)
    # Calculating the greatest decrease in revenue
    greatest_profit_decrease = min(revenue_change)

    # Finding the corresponding date that alings with the greatest increase or decrease in value
    greatest_date_increase = Months[revenue_change.index(greatest_profit_increase)+1]
    greatest_date_decrease = Months[revenue_change.index(greatest_profit_decrease)+1]

    # Generating the following set of results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_total))
    print("Total: " + "$" + str(sum(Profit)))
    print("Average Change: " + "$" + str(round(average_revenue, 2)))
    print("Greatest Increase in Profits: " + str(greatest_date_increase) + " ($" + str(greatest_profit_increase) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_date_decrease) + " ($" + str(greatest_profit_decrease) + ")")

# Creating a path to write the output Data:
PyBankpath_output = os.path.join('Analysis', 'Financial_analysis.txt')

# Creating an output as a text file
with open (PyBankpath_output, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write("Total Months: " + str(month_total) + "\n")
    text.write("Total: " + "$" + str(sum(Profit)) + "\n")
    text.write("Average Change: " + "$" + str(round(average_revenue, 2)) + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_date_increase) + " ($" + str(greatest_profit_increase) + ")" + "\n")
    text.write("Greatest Decrease in Profits: " + str(greatest_date_decrease) + " ($" + str(greatest_profit_decrease) + ")" + "\n")

