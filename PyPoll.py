import pandas as pd

data = pd.read_csv('election_data.csv')

vote_counts = data['Candidate'].value_counts(normalize=False)
vote_percs  = data['Candidate'].value_counts(normalize=True)

results_file = open('results.txt', 'w')

results_text = []

results_text.append('Election Results')
results_text.append('-------------------------')
results_text.append('Total Votes: %d' % data.shape[0])
results_text.append('-------------------------')

for candidate_name in vote_counts.keys():
    results_text.append('%s: %.3f%% (%d)' % (candidate_name, vote_percs[candidate_name], vote_counts[candidate_name]))
    
results_text.append('-------------------------')
results_text.append('Winner: %s' % vote_counts.keys()[0])
results_text.append('-------------------------')

for line in results_text:
    print(line)
    results_file.write(line + '\n')

results_file.close()
