import re

array1 = []
array2 = []
reg1 = r'a_fire_\w+'
with open("test.txt", "r", encoding='utf-8') as file:
    for line in file.readlines():
        keyword = re.search(r'a_fire_\w+', line)
        if keyword:
            array1.append(keyword.group(0))
            array2.append(re.search(r'(?<=a_fire_)\w+', keyword.group(0)).group(0))
print(array1)
print(array2)
print(len(array1))
print(len(array2))
# POST _reindex
# {
#   "source": {
#     "index": "a_fire_mdry"
#   },
#   "dest": {
#     "index": "a_kec_mdry"
#   }
# }
for item in array2:
    post_command = 'POST _reindex\n{\n"source": {\n"index": "a_fire_'+item+'"\n},\n"dest": { \n"index": "a_kec_' + \
                   item + '"\n}\n} '
    print(post_command + '\n\n')
