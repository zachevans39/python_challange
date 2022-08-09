
import os
import csv


budget_csv = os.path.join('budget_data.csv')
num_months= 0
month_change=[]
net_change_lists=[]
total_net= 0
max_change=0
Min_change=0
prev_month=0
with open(budget_csv) as csvfile:
    csv_reader= csv.reader(csvfile, delimiter=",")
    row = next(csv_reader)
    
   

    for row in csv_reader:
        num_months += 1
        total_net += int(row[1])
        month_change = abs(int(row[1]) - prev_month)
        prev_month = int(row[1])
        net_change = int(row[1]) /len(row[1])
        net_change_lists.append(month_change)
        
        

        #if max_change < (int(row[1])):
            #print(max_change)
            #max_change= row[1]
            #print(max_change)
    print(net_change)
    print(net_change_lists)

    monthly_change = sum(net_change_lists) / len(net_change_lists)/100

    high = max(net_change_lists)
    low = min(net_change_lists)

    print(f"Total Months: {num_months}")
    print(f"Total: {total_net}")
    print(f"Average Change: {monthly_change}")
    print(f"Greatest Increase in Profits:{(high)}")
    print(f"Greatest Decrease in Profits:{(low)}")


    for row in csv_reader:
        print(row)
 

