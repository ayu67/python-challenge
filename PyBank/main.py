import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader) #remove header
    #create lists that we can use to perform calculations 
    month=[]
    pl=[]
    for row in csvreader:
        month.append(row[0])
        pl.append(int(row[1]))

    net_change=[]
    for entry in range(1,len(pl)): #this list should have one less entry than the profit/loss one
        net_change.append(pl[entry]-pl[entry-1])

    net_change.insert(0,0) #insert a zero at the first entry to show no change in the first month

    total_months=len(month)
    #total_pl=sum(pl) not sure if allowed to use sum function since we didn't go over it (I think)
    total_pl=0
    for x in pl:
        total_pl=total_pl+x        
    
    #average_change=sum(net_change)/len(net_change)
    total_change=0
    position=0
    greatest_increase=0
    greatest_decrease=0
    for x in net_change:
        total_change=total_change+x
        if x>greatest_increase:
            greatest_increase=x
            greatest_month=month[position]
        if x<greatest_decrease:
            greatest_decrease=x
            least_month=month[position]
        position=position+1 #python lists start from 0 so this is at the end of the loop 

    average_change=total_change/(len(net_change)-1) #subtract 1 because we inserted a value earlier

# print results
analysis=(
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${total_pl}\n'
f'Average change: ${average_change:.2f}\n'
f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n'
f'Greatest Decrease in Profits: {least_month} (${greatest_decrease})'
)

print(analysis)

#Write to txt file
pybank_analysis=os.path.join('.','Analysis', 'analysis.txt')
with open(pybank_analysis, 'w') as txt_file:
    txt_file.write(analysis)

