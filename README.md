# 272-Assignment_2

 To implement a RocksDB replication in Python using the gRPC server.
 
 Data changes to RocksDB in the master node has to be pushed to the slave node if the slave node is up and the updates have to be done at the slave node as well.
 
 neha@neha: python server.py
 Server started at...3000
Please specify the operaion to perform : 
Enter 
1. PUT
2. DELETE 
3. UPDATE

In another terminal run the client simultaneously and the stream can be seen.

neha@neha: python client.py
