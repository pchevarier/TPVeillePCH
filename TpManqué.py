f = open("data.log","r")
entries = f.readlines()
for item in entries :
date_type = item.split(" - ")[0]
type_info = date_type.lstrip("[").rstrip("]")
type_info_tmp = type_info.split(" : ")
if(len(type_info_tmp)==2):
if(type_info_tmp[1] == "ERROR"):
print(type_info_tmp[0])
