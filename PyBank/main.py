import csv

#Path to CSV
file_path = r'C:\Users\evilp\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv'

#Variables to store analysis results
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#Read the CSV
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    header = next(csvreader)

    #Loop through each row in the CSV
    for row in csvreader:
        #Increment total months
        total_months += 1

        #Add the profit/loss for the current month to the net total
        profit_loss = int(row[1])
        net_total += profit_loss

        #Calculate the change in profit/loss from the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            total_change += change

            #Check if the current change is the greatest increase or decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        #Store profit/loss for the next iteration
        previous_profit_loss = profit_loss

#Calculate the average change
average_change = total_change / (total_months - 1)

#Generate the results
analysis_output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

#Print the results
print(analysis_output)

#Export to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

print(f"The analysis has been saved to {output_file}.")