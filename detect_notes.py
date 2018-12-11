import boto3
import json
import paramiko
import os
import pymongo
import ssl
import time
import datetime

def main():

    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
    #os.chdir("/home/karthikeya_raogv/.aws/")
    #with open("test.txt", "r") as file:
    #    text = file.read()
    data_list = ["personName","location","dateTime"]
    #data_list= {}
    client = pymongo.MongoClient("mongodb://kar:kar123@cluster0-shard-00-00-skdsn.mongodb.net:27017,\
cluster0-shard-00-01-skdsn.mongodb.net:27017,cluster0-shard-00-02-skdsn.mongodb.net:27017/appdata?\
ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    
    records = client.test.appdata.find({"flag": False})

    if records.count()!=0:
        for each_record in records:    
            print(each_record["notes"])
            test1 = comprehend.detect_entities(Text=each_record["notes"], LanguageCode='en')
            fields = json.dumps(comprehend.detect_entities(Text=each_record["notes"], LanguageCode='en')\
                                , sort_keys=True, indent=4)
            print('Calling Detect Entities')
            data_list = {}
            for data in test1["Entities"]:
                if data['Type'] == "PERSON":
                    print("Person: "+ str(data['Text']))
                    if "contact_name" in data_list:
                        data_list["personName"].append(str(data['Text']))
                    else:
                        data_list["personName"] = str(data['Text'])
                elif data['Type'] == "LOCATION":
                    print("location: "+ str(data['Text']))
                    if "location" in data_list:
                        data_list["location"].append(str(data['Text']))
                    else:
                        data_list["location"] = data['Text']
                elif data['Type'] == "DATE":
                    print("meeting_date: "+ str(data['Text']))
                    if "meeting_date" in data_list:
                        data_list["dateTime"].append(data['Text'])
                    else:
                        data_list["dateTime"] = data['Text']
                else:
                    print("something else : "+ str(data['Text']))
                    if "uncategorized" in  data_list:
                        continue
            print('End of DetectEntities\n')
            print(data_list)
            client.test.appdata.update_one({"_id":each_record["_id"]}, {"$set":{"keywords":data_list,"flag":True}})
        print("Completed updating notes to reminders!!!")
    else:
        print("No records to update notes to reminder!")
        
        
if __name__ == "__main__":
   main() 
