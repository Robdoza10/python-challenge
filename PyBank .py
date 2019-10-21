import pandas as pd

data = pd.read_csv('budget_data.csv')


results_file = open('results.txt', 'w')

results_text = []


results_text.append('Financial Analysis')
results_text.append('----------------------------')
results_text.append('Total Months: %d' % data.shape[0])
results_text.append('Total: $%d' % data['Profit/Losses'].sum())
results_text.append('Average  Change: $%.2f' % data['Profit/Losses'].mean())

max_change = data['Profit/Losses'].max()
max_month  = data[data['Profit/Losses'] == max_change]['Date'].tolist()[0]
results_text.append('Greatest Increase in Profits: %s ($%.2f)' % (max_month, max_change))

min_change = data['Profit/Losses'].min()
min_month  = data[data['Profit/Losses'] == min_change]['Date'].tolist()[0]
results_text.append('Greatest Decrease in Profits: %s ($%.2f)' % (min_month, min_change))

for line in results_text:
    print(line)
    results_file.write(line + '\n')

results_file.close()
