from urllib.request import urlopen
import json
import ssl

class News:
    def __init__(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = urlopen('https://newsapi.org/v2/everything?q=Cyber%20Security&apiKey=cbdc18ab9da94004b749731e335b6e40',context=ctx)
        self.obj = json.load(url) 


    def checkForWord(self,lis):
        #for word in lis:
            #if (word.lower().find("india") != -1):
                #return True
        return True

    def parseData(self,object):
        requiredList = []
        if(object["status"] == 'ok'):
            oneobject = {}
            data = object['articles']
            for dataobj in data:
                oneobject = {}
                
                result = self.checkForWord([dataobj["title"],dataobj["description"]])
                if(result==True):
                    oneobject["title"] = dataobj["title"]
                    oneobject["source"] = dataobj["source"]
                    oneobject['urlToImage'] = dataobj["urlToImage"]
                    oneobject['time'] = dataobj["publishedAt"]
                    oneobject['url'] = dataobj["url"]
                    requiredList.append(oneobject)
        return requiredList

    def news(self):
        return self.parseData(self.obj)

