from steam_reviews import ReviewLoader
import csv
import json
#load appID lists

f_appID = open("games-features.csv","r", encoding='utf-8')
appID = []
reader = csv.reader(f_appID,delimiter=',')
line = 0
for i in reader:
    line +=1
    if line == 1:
        continue
    appID.append(i[0])

cnt = 0

NREVIEWS = 1000

si = len(appID)

path = 'data_1000reviews/'
name = 'reviews_'
ext = '.json'

NO_reviews = []
ID = []
for i in appID:
    
    file_path = path + name + str(i) + ext

    json_file  = open(file_path,'r')
    if json_file.closed:
        continue
    data = json.load(json_file)
    if 'query_summary' not in data:
        continue
    if 'total_reviews' not in data['query_summary']:
        continue
    NO_reviews.append(data['query_summary']['total_reviews'])
    
    ID.append(i)
    
    cnt +=1
    print(i,cnt,si-cnt)
f_save = open('Number_reviews.csv','w+')
for i in range(len(ID)):
    f_save.write(str(ID[i])+','+str(NO_reviews[i])+'\n')

f_save.close()
    
"""
import inspect

func = steamreviews.download_reviews_for_app_id
def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
print(get_default_args(func))
"""