

def search(drug_cost, top_cost_drug):
	"""search and update the top_cost_drug list"""
	k = 0
	while k<len(top_cost_drug):
		if top_cost_drug[k]['drug_name']==drug_cost['drug_name']:
			top_cost_drug[k]['num_prescriber'] += 1
			top_cost_drug[k]['total_cost'] += drug_cost['drug_cost']
			return top_cost_drug
		k += 1
	
	if k == len(top_cost_drug):
		new_dic = {'drug_name':drug_cost['drug_name'],'num_prescriber':1,'total_cost':drug_cost['drug_cost']}
		top_cost_drug.append(new_dic)
		return top_cost_drug

# def search(drug_cost,top_cost_drug):
# 	new_dic = {'drug_name':drug_cost['drug_name'],'num_prescriber':1,'total_cost':drug_cost['drug_cost']} 
# 	try:
# 		k = top_cost_drug.index(new_dic)
# 	except ValueError:
# 		top_cost_drug.append(new_dic)
# 		print('no such record')
# 	else:
# 		print(top_cost_drug[k]['drug_name'])
# 		top_cost_drug[k]['num_prescriber'] += 1
# 		top_cost_drug[k]['total_cost'] += drug_cost['drug_cost']
# 	finally:
# 		return top_cost_drug

def myfunc(dic):
	"""return the value corresponding to 'total_cost' in the dictionary"""
	return dic['total_cost']

def sort_dic(top_cost_drug):
	"""sort the list of dictionaries based on the value of 'total_cost'"""
	top_cost_drug.sort(reverse=True,key=myfunc)
	return top_cost_drug

## main program

drug_cost = {}
top_cost_drug = []

try:
	finput = open('itcont.txt','r')
except IOError:
	print('Cannot open input file')
try:
	foutput = open('top_cost_drug.txt','w')
except IOError as e:
	print(e)

# check if there is a header line. by default, there is one
header  = 1
ch =  finput.read(1)
if ch < '0' or ch > '9':
	header = 1
else:
	header = 0
finput.seek(0)

for line in finput:
	if header == 1:
		header = 0
		continue
	else:
		record = line.split(',')
		drug_cost = {'drug_name':record[-2],'drug_cost':float(record[-1])}
		top_cost_drug = search(drug_cost,top_cost_drug)

sorted_top_cost_drug = sort_dic(top_cost_drug)

foutput.write('drug_name,num_prescriber,total_cost\n')

for dic in sorted_top_cost_drug:
	foutput.write('{},{},{:.2f}\n'.format(dic['drug_name'],dic['num_prescriber'],dic['total_cost']))
		
finput.close()
foutput.close()