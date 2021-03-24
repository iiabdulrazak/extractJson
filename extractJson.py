import json
import pandas as pd
import requests as re

#getting data from the api then converting it to json file.
url = 'https://raw.githubusercontent.com/facebookresearch/fine_grained_hateful_memes/master/data/annotations/train.json'
res = re.get(url)
#checking response type
print(f'Response Type: {res}')
#saving extracted text into variable
apiData = res.text

#saving api output into json file
with open("apiData.json","w") as out:
    out.write(apiData)
    
#converting json data into .csv
data = pd.read_json('apiData.json', lines=True)
print(data.head(2))
data.to_csv('apiData.csv')
