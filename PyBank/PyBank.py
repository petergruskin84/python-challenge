#type code here
#used chatgpt for help
import csv

def read_csv_data(r'/Users/pete.home/Library/Mobile Documents/com~apple~CloudDocs/Data Analytics Bootcamp/3.X Python HW/python-challenge/PyBank/budget_data.csv):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[0]
            profit_loss = int(row[1])
            data.append((date, profit_loss))
    return data

def calculate_statistics(data):
    months = len(data)
    total_profit_losses = sum(profit_loss for , profit_loss in data)
    changes = [profit_loss2 - profit_loss1 for (, profit_loss1), (_, profit_loss2) in zip(data, data[1:])]
    average_change = sum(changes) / len(changes)
    max_increase = max(changes)
    max_decrease = min(changes)

# Find corresponding dates for max increase and max decrease
max_increase_date = data[changes.index(max_increase) + 1][0]
max_decrease_date = data[changes.index(max_decrease) + 1][0]

return {
    "Total Months": months,
    "Net Total Profit/Losses": total_profit_losses,
    "Average Change": average_change,
    "Greatest Increase in Profits": {"Date": max_increase_date, "Amount": max_increase},
    "Greatest Decrease in Profits": {"Date": max_decrease_date, "Amount": max_decrease}
}

def main():
    file_path = "path/to/your/file.csv"  # Replace with the actual path to your CSV file
    data = read_csv_data(file_path)
    result = calculate_statistics(data)

# Print the results
for key, value in result.items():
    print(f"{key}: {value}")

if name == "main":
    main()
    