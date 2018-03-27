import os
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from io import StringIO
import urllib.parse
import urllib.request


subscription_key = '838b012b4a6f46acacfca98228ced4bb'
assert subscription_key
text_analytics_base_url = "https://eastasia.api.cognitive.microsoft.com/text/analytics/v2.0/"

#language_api_url = text_analytics_base_url + "languages"
#print(language_api_url)

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

'''
documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' }
]}
'''

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}


# make API call
def sentimentCall(text):
    documents_list = []
    idx = 1

    for t in text:
        docu_dic = {}
        if len(t) > 0:
#            print('------------------------{}--------------------------'.format(idx))
#            print(t)
            docu_dic['id'] = str(idx)
            docu_dic['language'] = 'en'
            docu_dic['text'] = t
#            print('------------------------dic--------------------------')
#            print(docu_dic)
    
#            print('------------------------document_list--------------------------')
            documents_list.append(docu_dic)
#            print(documents_list)
    #        print(len(documents_list))
            idx = idx + 1

#    print('------------------------list--------------------------')
   # print(documents_list)
    documents_dic = {}
    documents_dic['documents'] = documents_list
#    print(documents_dic)
#    io = StringIO()
    documents = json.dumps(documents_dic)

    '''
    documents = {'documents' : [
      {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
      {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
      {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
      {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
    ]}
    '''
    print('------------------------json--------------------------')
    print(documents)

    headers   = {"Accept":"application/json",  "Content-Type": "application/json", "Ocp-Apim-Subscription-Key": subscription_key}
    #response  = requests.post(language_api_url, headers=headers, json=documents)

    response  = requests.post(sentiment_api_url, headers=headers, json=documents)

    #languages = response.json()
    #pprint(languages)
    sentiments = response.json()
    pprint(sentiments)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


target = 'https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/'
target = 'http://www.bbc.com/news/world-asia-43550938'

req = requests.get(target)
#print(req)
print('--------------------------------------------------')

html = req.text
#print(html)
print('--------------------------------------------------')

soup = BeautifulSoup(html, 'html.parser')

#print(soup.title.string)

raw_header = soup.find_all('h1')
raw_texts = soup.find_all('p')

def extractString(soubObj):
    _texts = []
    for t in soubObj:
#        print("t: {}".format(t))
        if t is not None:
            if t.string is not None:
#                print(t.string)
                _texts.append(t.string)
    return _texts

header_str = extractString(raw_header)
texts_str = extractString(raw_texts)
#print(header_str)
#print(texts_str)
header_str.extend(texts_str)

texts = header_str


data = concated_data = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
idx = 0
for t in texts:
    if t is not None:
        if t.string is not None:

            char_len = 0
            if len(data[idx]):
                con_data = ''.join(data[idx])
                con_data = con_data.replace('"', '')
                char_len = len(con_data)
                #print("char_len: {}", char_len)

            if char_len < 200:
            #print("t: " + t.string)
                #if t.string is not ' ':
                data[idx].append(t.string)
            else:
                idx = idx + 1
                #if t.string is not ' ':
                data[idx].append(t.string)



#print((data[0]))
#print((data[1]))
idx = 0
for d in data:
    concated_data[idx] = ''.join(d)
    concated_data[idx] = concated_data[idx].replace('"', '')
    idx = idx + 1

for con in concated_data:
    print('------------------------{}--------------------------'.format(concated_data.index(con)))
#    print(con)
#con_data = ''.join(data).replace('"', '')
#print(len(con_data))
#print(con_data)

sentimentCall(concated_data)
print('data--------------------------------------------------')
#print(data)

print('concate data--------------------------------------------------')
#print(con_data)

#print(len(con_data))


'''
for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
'''
