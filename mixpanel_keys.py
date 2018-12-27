import json
json_data = open('//HOFILE04/USERS_M/T032160/Amica/Digital Marketing/Mixpanel python scripts/mixpanel_android_01.json')
json_data_load = json.load(json_data)
my_list = []
for r in json_data_load:
	for s in r:
		for k in r[s]:
			my_list.append(k)
			print(my_list)
			if k =="":
				break
					