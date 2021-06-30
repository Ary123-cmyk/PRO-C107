import plotly.express as px
import pandas as pd
from alive_progress import alive_bar
from rich import inspect
csv = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv")
levels = []
attempts = []
with alive_bar(len(csv)) as bar:
	for idx in range(0, len(csv)):
		levels.append(csv.iloc(0)[idx]["level"])
		attempts.append(csv.iloc(0)[idx]["attempt"])
		bar()
inspect(levels)
inspect(attempts)
level1 = []
i = 0
for lev in levels:
	if lev == 'Level 1':
		level1.append(attempts[i])
	i = i + 1
level2 = []
i = 0
for lev in levels:
	if lev == 'Level 2':
		level2.append(attempts[i])
	i = i + 1
level3 = []
i = 0
for lev in levels:
	if lev == 'Level 3':
		level3.append(attempts[i])
	i = i + 1
level4 = []
i = 0
for lev in levels:
	if lev == 'Level 4':
		level4.append(attempts[i])
	i = i + 1
total = 0
for att in level1:
	total = total + att
mean1 = total/len(level1)
total = 0
for att in level2:
	total = total + att
mean2 = total/len(level2)
total = 0
for att in level3:
	total = total + att
mean3 = total/len(level3)
total = 0
for att in level4:
	total = total + att
mean4 = total/len(level4)
print("Level 1 Mean: {}".format(mean1))
print("Level 2 Mean: {}".format(mean2))
print("Level 3 Mean: {}".format(mean3))
print("Level 4 Mean: {}".format(mean4))