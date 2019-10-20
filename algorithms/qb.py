import json
import csv
import datetime

# read all files
# load the data into dictionaries
with open('C://Users/Meng/Desktop/machine_transaction.json','r') as machine_trans:
	trans = json.load(machine_trans)

equip = []
with open('C://Users/Meng/Desktop/equipment_lu.csv','r') as equip_info:
	for line in equip_info:
		dic = {}
		id,model = line.strip().split('|')
		dic['eq_id'] = id
		dic['model'] = model
		equip.append(dic)

time = []
with open('C://Users/Meng/Desktop/timesheets.csv','r') as time_sheet:
	for line in time_sheet:
		dic = {}
		clock_off,clock_on, cost_per_hour,fname,lname,person_id = line.strip().split('|')
		dic['clock_off'] = clock_off
		dic['clock_on'] = clock_on
		dic['cost_per_hour'] = cost_per_hour
		dic['fname'] = fname
		dic['lname'] = lname
		dic['person_id'] = person_id
		time.append(dic)

# number of equipment without eq_id
cnt = 0
for i in range(len(equip)):
	if i!=0 and equip[i]['eq_id'] == '"NULL"':
		cnt += 1
# print(cnt)

# directory of models with eq_ids
equip_dir = {}
for i in range(len(equip)):
	if i!=0:
		if equip[i]['model'] not in equip_dir:
			equip_dir[equip[i]['model']] = 1
		else:
			equip_dir[equip[i]['model']] += 1
# print(equip_dir)

# find most frequenctly used equipment based on times
equip_usage = {}
for i in range(len(trans)):
	if i!=0 and trans[i]['eq_id'] not in equip_usage:
		equip_usage[trans[i]['eq_id']] = 1
	elif i!=0:
		equip_usage[trans[i]['eq_id']] += 1
# print(equip_usage)

# group people who has the cost_per_hour
cost_per_hour = {}
for i in range(len(time)):
	if i!=0:
		clockon = datetime.datetime.strptime(time[i]['clock_on'], '"%Y-%m-%d %H:%M:%S"')
		clockoff = datetime.datetime.strptime(time[i]['clock_off'], '"%Y-%m-%d %H:%M:%S"')
		timediff = clockoff - clockon
		time[i]['totaltime'] = timediff

		# employees with the same cost_per_hour 
		if time[i]['cost_per_hour'] not in cost_per_hour:
			cost_per_hour[time[i]['cost_per_hour']] = {time[i]['person_id']}
		else:
			cost_per_hour[time[i]['cost_per_hour']].add(time[i]['person_id'])
# print(cost_per_hour.keys())

# smaller than 300 per hour: 200, 100


# 3d_printers
threed_printer = []
for i in range(len(trans)):
	if trans[i]['operation']['activity'] == '3d_printing':
		if trans[i]['eq_id'] not in threed_printer:
			threed_printer.append(trans[i]['eq_id'])
# print(threed_printer)

# find distinct names in time
distinctname = set()
names = {}
for i in range(len(time)):
	if i!=0:
		fullname = time[i]['lname'].strip('"')+time[i]['fname'][1]
		distinctname.add(fullname)

		# count number of name with the same first name inital and last name
		# if count == 1, they can be distinguished
		if fullname not in names:
			names[fullname] = 1
		else:
			names[fullname] += 1
# print(distinctname)
# need to check if 'person_id' can match 'operator' in machine_transaction










