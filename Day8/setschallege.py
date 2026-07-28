#set coding challege:
std1_id=[22,31,69,45,78,69,31]
new_std1_id=set(std1_id)
std2_id=[56,31,69,45,56,34,22]
new_std2_id=set(std2_id)
for item in new_std1_id: 
   if item in new_std2_id:
     print(item) 
#print(new_std1_id & new_std2_id) 
#common=new_std1_id.intersection(new_std2_id) 
#print("common",common) 
