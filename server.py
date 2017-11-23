'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server 
################################## server.py #############################
'''
import time
import grpc
import replicator_pb2
import replicator_pb2_grpc
import uuid
import rocksdb
from random import *
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

serverdb = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))
keys =[]

class ReplicatorServicer(replicator_pb2_grpc.ReplicatorServicer):
    def __init__(self,f):
        self.f =f

    def __call__(self):
        self.key = self.f()
        self.value = masterDB.get(self.key)
        print ("key = "+ self.key.decode())
        print("value = "+self.value.decode())

    def GetInstance(self,request,context):
        return replicator_pb2_grpc.Response(operation=self.f,key=self.key,value=self.value)

@ReplicatorServicer
def put():
    value = input("Enter value to Put: ")
    key= str(randint(1,500))
    while key in keys:
        key = str(randint(1,500))
    keys.append(key)
    print("Key is : "+key)
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    serverdb.put(key,value)
    print(serverdb.get(key))
    return key

@ReplicatorServicer
def delete():
    key = input("Enter key to delete: ")
    while key not in keys:
        print("Key not in database")
    keys.remove(key)
    key = key.encode('ASCII')
    serverdb.delete(key)
    return key

@ReplicatorServicer
def update():
    key = input("Enter key to update: ")
    while key not in keys:
        print("key value not in database")
    value = input("Enter the value to be updated: ")
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    serverdb.put(key,value)
    return key

def run(host,port):
    print("Server started at...%d" % port)
    while(1):
       operation = input("Please specify the operaion to perform : \nEnter \n1. PUT\n2. DELETE \n3. UPDATE\n")
       if(operation=="1"):
           put()
       elif(operation=="2"):
           delete()
       elif(operation=="3"):
           update()

       server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
       replicate_pb2_grpc.add_ReplicateServicer_to_server(Replicate(operation), server)
       server.add_insecure_port('%s:%d' % (host, port))
       server.start()

if __name__ == '__main__':
    run('0.0.0.0', 3000)

