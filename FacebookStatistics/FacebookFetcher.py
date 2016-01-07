from urllib.request import urlopen
import json

posts = []

count = 0

def getStringFromAddress(address):
    return urlopen(address).readall().decode('utf-8')

def getJson(string):
    return json.loads(string)

def getNext(jsonObject):
    try:    
        newAddress = jsonObject["paging"]["next"]
        
        return newAddress
        
    except: 
        print("Something went wrong.")
        saveResult()
        print("Partial results saved with %d posts" % len(posts))
        print(curAddress)

def saveResult():
    resultFile = open('./result.json', 'w+')
    resultFile.write(json.dumps(posts))
        
def appendResult(jsonObject):
    for curPost in jsonObject["data"]:
        posts.append(curPost)

curAddress = "https://graph.facebook.com/v2.0/145632722140414/posts?fields=link%2Cmessage&with=time&limit=100&access_token=CAACEdEose0cBAFaOJ2zRZAdHZCVOKHfGrI2DHFNgfSlJtb6PiswX0t8dXglJ2dMX1JbCu8jbctjQ1yZBl3ZCg5TiQUl3gBggD173tpbYOAgpjS4JSkCET7vMywTpI3ZBR3hOlBwsGj9lTRNZAw9V6AuCZAN9oM8pCsMozQN4YTcIveQOjQppPzEK04LZBXs6khdpgBsES5bNDQZDZD"

for x in range(1,1000):
    print("Request number %d" % x)
    resultString = getStringFromAddress(curAddress)
    curObject = getJson(resultString)
    appendResult(curObject)
    curAddress = getNext(curObject)
    
    if x % 25 == 0:
        print(curAddress)
    
print("%d posts fetched" % len(posts))

saveResult()