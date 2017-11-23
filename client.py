'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import rocksdb
from random import *
import replicator_pb2
import replicator_pb2_grpc
import grpc
import argparse
from concurrent import futures

PORT = 3000
clientdb = rocksdb.DB("clientdb.db", rocksdb.Options(create_if_missing=True))
keys =[]

class ReplicatorClient():
   def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = replicator_pb2.ReplicatorStub(self.channel)

   def GetInstance(self,request):
       return self.stub.GetInstance(replicator_pb2.Request(data=request))

def put():
    value = input("Enter value to Put: ")
    key= str(randint(1,500))
    while key in keys:
        key = str(randint(1,500))
    keys.append(key)
    print("Key is : "+key)
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    clientdb.put(key,value)
    print(serverdb.get(key))
    return key

def delete():
    key = input("Enter key to delete: ")
    while key not in keys:
        print("Key not in database")
    keys.remove(key)
    key = key.encode('ASCII')
    serverdb.delete(key)
    return key

def update():
    key = input("Enter key to update: ")
    while key not in keys:
        print("key value not in database")
    value = input("Enter the value to be updated: ")
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    serverdb.put(key,value)
    return key

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = ReplicatorClient(host=args.host)
    response = client.GetInstance('connect')
    for resp in response:
        print(resp.uid)
    

if __name__=="__main__":
    run()


