#Got help from tutor and co-pilot
#import the csv importer module from the python library
import csv

#initialize 2 variables for the 2 columns of data we have, that are currently empty:
months = []
pl = []
chg = []
chg_mo = []

#name our csv_file dataset by the file name (not file path)
csv_file = 'budget_data.csv'


with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    header = next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        months.append(row[0])
        pl.append(int(row[1]))
        if len(months) > 1:
            chg_in_p = int(row[1]) - prev_mo_pl
            chg.append(chg_in_p)
            chg_mo.append(row[0])
        prev_mo_pl = int(row[1])

#The total number of months included in the dataset
total_months = len(months)
print(total_months)

#The net total amount of "Profit/Losses" over the entire period
total_net_pl = sum(pl)
print(total_net_pl)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes (should be $-8311.11)
avg_chg = sum(chg) / len(chg)
print(avg_chg)

#The greatest increase in profits (date and amount) over the entire period (should be Aug-16 ($1862002))
max_chg = max(chg)
print(max_chg)
idx = chg.index(max_chg)
max_chg_mo = chg_mo[idx]
print(max_chg_mo)

#The greatest decrease in profits (date and amount) over the entire period (should be Feb-14 ($-1825558))
min_chg = min(chg)
print(min_chg)
idx = chg.index(min_chg)
min_chg_mo = chg_mo[idx]
print(min_chg_mo)

export_file = open("output.txt", "w")
export_file.write("Financial Analysis\n")
export_file.write("----------------------------\n")
export_file.write(f"Total Months: {total_months}\n")
export_file.write(f"Total: ${total_net_pl}\n")
export_file.write(f"Average Change: ${avg_chg}\n")
export_file.write(f"Greatest Increase in Profits: {max_chg_mo} (${max_chg})\n")
export_file.write(f"Greatest Decrease in Profits: {min_chg_mo} (${min_chg})\n")
export_file.close()
