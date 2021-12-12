import json, codecs

class FileManager:

    def writeDataToFile(self, fileName, data):    
        with open(fileName, 'wb') as f:
             json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii = False)


    def readDataToFile(self, fileName):    
        with open(fileName) as f:
              lines = f.readlines()
