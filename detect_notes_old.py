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
    data_list = {}
    client = pymongo.MongoClient("mongodb://kar:kar123@cluster0-shard-00-00-skdsn.mongodb.net:27017,\
cluster0-shard-00-01-skdsn.mongodb.net:27017,cluster0-shard-00-02-skdsn.mongodb.net:27017/users?\
ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    
    records = client.test.notes.find({"post_ml": False})

    if records.count()!=0:
        for each_record in records:    
            print(each_record["note_desc"])
            test1 = comprehend.detect_entities(Text=each_record["note_desc"], LanguageCode='en')
            fields = json.dumps(comprehend.detect_entities(Text=each_record["note_desc"], LanguageCode='en')\
                                , sort_keys=True, indent=4)
            print('Calling DetectEntities')
            data_list = {}
            for data in test1["Entities"]:
                if data['Type'] == "PERSON":
                    print("Person: "+ str(data['Text']))
                    if "contact_name" in data_list:
                        data_list["contact_name"].append(str(data['Text']))
                    else:
                        data_list["contact_name"] = str(data['Text'])
                elif data['Type'] == "LOCATION":
                    print("location: "+ str(data['Text']))
                    if "location" in data_list:
                        data_list["location"].append(str(data['Text']))
                    else:
                        data_list["location"] = data['Text']
                elif data['Type'] == "DATE":
                    print("meeting_date: "+ str(data['Text']))
                    if "meeting_date" in data_list:
                        data_list["meeting_date"].append(data['Text'])
                    else:
                        data_list["meeting_date"] = data['Text']
                else:
                    print("something else : "+ str(data['Text']))
                    if "uncategorized" in  data_list:
                        data_list["uncategorized"].append(data['Text'])
                    else:
                        data_list["uncategorized"] = data['Text']
            print('End of DetectEntities\n')
            data_list["post_ml"] = True
            print(data_list)
            client.test.notes.update_one({"_id":each_record["_id"]}, {"$set":data_list})
        print("Completed updating notes to reminders!!!")
    else:
        print("No records to update notes to reminder!")
        
        
if __name__ == "__main__":
   main() 
