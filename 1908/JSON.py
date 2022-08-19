import json
with open("files/eq.json", encoding="utf8") as f:
    jj = json.load(f)
K1 = ['timestamp', 'referer', 'location', 'remoteHost', 'partyId', 'sessionId', 'pageViewId', 'eventType', 'item_id', 'item_price', 'item_url', 'basket_price', 'detectedDuplicate', 'detectedCorruption', 'firstInSession', 'userAgentName']
for i in jj:
    if len(i.keys()) != 16:
        print(False, "Лишние ключи в ответе")
    for s in i.keys():
        if s not in K1:
            print(False, i.keys())
for i in range(len(jj)):
    for t in jj[i]:
        print(t, jj[i][t])
        if t == "timestamp" and type(jj[i][t]) != int:
            print("Timestamp value error!")
        elif t == "referer" and "https:" not in jj[i][t]:
            print("referer value error!")
        elif t == "location" and "https:" not in jj[i][t]:
            print("referer value error!")
        
