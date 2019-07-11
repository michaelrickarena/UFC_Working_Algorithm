import itertools
import csv

def comb1(k, available, used):
	if len(used)==k: #hits the required number of units in a combo
		yield tuple(used)
	elif len(available)==0: # went through all avaliable and has none left over
		pass
	else:
		head=available.pop(0)
		used.append(head)
		for c in comb1(k, available[:], used[:]):
			yield c
		used.pop()
		for c in comb1(k, available[:], used[:]):
			yield c

n=50000
n2=49500

def comb_wrapper(k,s,n,n2):
	for c in comb1(k,list(s),[]):
		total= sum(s[i]['cost'] for i in c)
		if list(filter(lambda player_name: s[player_name]["Opponent"] in c, c)):
			continue
		if n >= total >= n2:
			yield c



s={'Drew Dober': {'cost': 9500, 'Opponent': 'Polo Reyes'}, 'Eryk Anders': {'cost': 9400, 'Opponent': 'Vinicius Castro'}, 'Jordan Griffin': {'cost': 9300, 'Opponent': 'Vince Murdock'}, 'Jared Gordon': {'cost': 9200, 'Opponent': 'Dan Moret'}, 'Ricardo Ramos': {'cost': 9100, 'Opponent': 'Journey Newson'}, 'Alonzo Menifield': {'cost': 9000, 'Opponent': 'Paul Craig'}, 'Roosevelt Roberts': {'cost': 8900, 'Opponent': 'Vinc Pichel'}, 'Francis Ngannou': {'cost': 8800, 'Opponent': 'Junior Dos Santos'}, 'Dalcha Lungiambula': {'cost': 8700, 'Opponent': 'Dequan Townsend'}, 'Demian Maia': {'cost': 8600, 'Opponent': 'Anthony Rocco Martin'}, 'Emily Whitmire': {'cost': 8500, 'Opponent': 'Amanda Ribas'}, 'Joseph Benavidez': {'cost': 8400, 'Opponent': 'Jussier Formiga'}, 'Jussier Formiga': {'cost': 7800, 'Opponent': 'Joseph Benavidez'}, 'Amanda Ribas': {'cost': 7700, 'Opponent': 'Emily Whitmire'}, 'Anthony Rocco Martin': {'cost': 7600, 'Opponent': 'Demian Maia'}, 'Dequan Townsend': {'cost': 7500, 'Opponent': 'Dalcha Lungiambula'}, 'Junior Dos Santos': {'cost': 7400, 'Opponent': 'Francis Ngannou'}, 'Vinc Pichel': {'cost': 7300, 'Opponent': 'Roosevelt Roberts'}, 'Paul Craig': {'cost': 7200, 'Opponent': 'Alonzo Menifield'}, 'Journey Newson': {'cost': 7100, 'Opponent': 'Ricardo Ramos'}, 'Dan Moret': {'cost': 7000, 'Opponent': 'Jared Gordon'}, 'Vince Murdock': {'cost': 6900, 'Opponent': 'Jordan Griffin'}, 'Vinicius Castro': {'cost': 6800, 'Opponent': 'Eryk Anders'}, 'Polo Reyes': {'cost': 6700, 'Opponent': 'Drew Dober'}}
k=6




mycombs=list(comb_wrapper(k, s, n, n2))
print(len(mycombs))

# Put in Excel
with open('Real_LR.csv', 'w', newline='') as f:
	thewriter=csv.writer(f)
	thewriter.writerow(['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6'])
	for comb in mycombs:
		thewriter.writerow(comb)