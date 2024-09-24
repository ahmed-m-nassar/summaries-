## Using minikube with wsl , You can`t access the service 
Use this command to find what ip:port to connect to : 

**minikube service client-node-port --url**

Dont close terminal , otherwise the ip:port will change

## No permission issues on image , but permission issues when Creating pod 

Use a specific user and Group in pod 

EX :
```YAML
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
```
And when Building Docker image , make sure you change permissions to allow that user and group to access files with problems : 


## Cant connect to database in another pod
if you have a service that connects to another service , make sure that you type the clusterip and its port when you try to connect to the service , not the service name 
