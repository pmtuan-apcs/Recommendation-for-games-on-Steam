from steam_reviews import ReviewLoader
import csv
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

for i in appID:
    
    cnt +=1
    if cnt <11:
        continue
   # AppId is 1091500, and we need 1000 reviews
    reviews = ReviewLoader().set_language('english').load_from_api(i)


    # Save the data as json file, provide the folder path as the argument
    reviews.save_json('/data_1000reviews/')
       

    print(i,cnt,si-cnt)
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