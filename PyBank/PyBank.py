#type code here
#used chatgpt for help


import pandas as pd

def read_csv_data(file_path):
    data = pd.read_csv(file_path)
    return data

def calculate_statistics(data):
    months = len(data)
    total_profit_losses = data["Profit/Losses"].sum()
    data["Change"] = data["Profit/Losses"].diff()
    average_change = data["Change"].mean()
    max_increase = data["Change"].max()
    max_decrease = data["Change"].min()

    max_increase_date = data.loc[data["Change"] == max_increase, "Date"].iloc[0]
    max_decrease_date = data.loc[data["Change"] == max_decrease, "Date"].iloc[0]

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

if __name__ == "__main__":
    main()