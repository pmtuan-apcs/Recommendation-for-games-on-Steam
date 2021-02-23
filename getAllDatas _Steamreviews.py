
import csv
#load appID lists

import steamreviews
request_params = dict()

request_params['language'] = 'english'

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

si = len(appID)

for i in appID:
    
    cnt +=1
    if cnt <1:
        continue
   # AppId is 1091500, and we need 1000 reviews
    
    review_dict, query_count = steamreviews.download_reviews_for_app_id(i,
                                                                    chosen_request_params=request_params)


    # Save the data as json file, provide the folder path as the argument

    print(i,cnt,si-cnt)
