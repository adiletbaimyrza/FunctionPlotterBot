import os

this_path = os.path.dirname(os.path.realpath(__file__))
results_dir = os.path.join(this_path, 'results')

file_path = os.path.join(results_dir, 'old_time_results.txt')
with open(file_path, 'r') as f:
    olds = [float(line) for line in f]

file_path = os.path.join(results_dir, 'new_time_results.txt')
with open(file_path, 'r') as f:
    news = [float(line) for line in f]

sum_olds = sum(olds)
sum_news = sum(news)

avg_olds = sum_olds / 10
avg_news = sum_news / 10

times_better = sum_olds / sum_news
times_better_percents = times_better * 100

file_path = os.path.join(results_dir, 'avgs.txt')
with open(file_path, 'w') as f:
    f.write('old average(s): ' + str(avg_olds) + '\n')
    f.write('new average(s): ' + str(avg_news) + '\n')
    f.write('new module faster: ' + str(times_better_percents) + '%\n')