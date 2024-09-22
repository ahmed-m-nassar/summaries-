## Minikube
### Installation
- curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
- sudo install minikube-linux-amd64 /usr/local/bin/minikube

### Verify Installation
- minikube version

### create a single-node Kubernetes cluster
- sudo dockerd
- minikube start

### Check cluster status 
- minikube status

### Check logs 
- minikube logs


## Helm

### Installation
- curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

## Kubectl
### Installation
-  curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
- chmod +x ./kubectl
- sudo mv ./kubectl /usr/local/bin/kubectl

## Skaffold
### Installation
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && \
sudo install skaffold /usr/local/bin/

### Verify Installation
- kubectl version --client

### Pods Commands
- `kubectl get pods` - List all pods in the current namespace.
- `kubectl get pods -n <namespace>` - List all pods in a specific namespace.
- `kubectl describe pod <pod-name>` - Display detailed information about a specific pod.
- `kubectl logs <pod-name>` - View the logs of a specific pod.
- `kubectl logs -f <pod-name>` - Stream logs from a running pod.
- `kubectl exec -it <pod-name> -- /bin/bash` - Open a bash terminal in a running pod.
- `kubectl delete pod <pod-name>` - Delete a specific pod.

### Deployment Commands
- `kubectl get deployments` - List all deployments in the current namespace.
- `kubectl describe deployment <deployment-name>` - Show detailed information about a deployment.
- `kubectl apply -f <file.yaml>` - Apply a configuration to a resource from a file.
- `kubectl create -f <file.yaml>` - Create a resource from a file.
- `kubectl rollout status deployment <deployment-name>` - Show the status of a deployment's rollout.
- `kubectl rollout undo deployment <deployment-name>` - Roll back a deployment to the previous version.
- `kubectl scale deployment <deployment-name> --replicas=<count>` - Scale a deployment to a specified number of replicas.

### Services Commands
- `kubectl get services` - List all services.
- `kubectl describe service <service-name>` - Display detailed information about a service.
- `kubectl delete service <service-name>` - Delete a specific service.

### Secrets Commands
- `kubectl get secrets` - List all secrets.
- `kubectl describe configmap <configmap-name>` - Display detailed information about a configmap.
- `kubectl describe secret <secret-name>` - Display detailed information about a secret.
- `kubectl create secret generic <secret-name> --from-literal=<key>=<value>` - Create a generic secret from a literal value.

### Debugging 
- `kubectl describe <resource> <name>` - Describe a resource (pod, deployment, service, etc.).
- `kubectl get events` - Show cluster events.
- `kubectl get pod <pod-name> -o yaml` - Output the YAML for a specific pod.
- `kubectl get all` - List all resources (pods, services, etc.) in the current namespace.
- `kubectl get all -n <namespace>` - List all resources in a specific namespace.


### Config Files 
#### 1- Pod
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: myapp
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
``` 

- **apiVersion**: The API version for creating a Pod.
- **kind**: Type of resource (Pod).
- **metadata**: Contains the Pod's name and labels.
- **labels** : Used to match a service to this port
- **spec**: The Pod specification, defining the containers.
- **containers**: Defines the container running in the Pod.
- **image**: The container image to use (nginx in this case).
- **ports**: Exposing port 80.

#### 2- Deployment

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
```
- **replicas**: Number of Pod replicas the Deployment should maintain.
- **selector**: Determines which Pods are selected to be managed by the Deployment.
- **template**: Defines the Pod template to be used for creating the Pods, similar to the standalone Pod spec above.

#### 3- Node Port Service
```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```

- **type**: NodePort: Exposes the service on a node's IP at a specific port.
- **selector**: Connects the service to Pods with the label app: myapp.
 - **port** : The port the Service exposes inside the cluster (e.g., 80)
- **targetPort** : The actual port where the container inside the Pod is listening 
- **nodePort** : The port on each Node where external traffic can access the service
    
External traffic directed to <NodeIP>:<nodePort> is forwarded to the Service, which then forwards it to the targetPort on the Pod.

#### 4- Cluster IP Service
```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-clusterip-service
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 80
```
- **type**: ClusterIP: The default type that makes the service reachable only within the cluster.
- **selector**: Matches Pods with the label app: myapp.
- **ports**: Maps the service port (port: 80) to the Pod's container port (targetPort: 80).


#### 5- NGINX Ingress
##### Installation
- helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
- helm repo update
- helm install nginx-ingress ingress-nginx/ingress-nginx

##### Example 
```YAML
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /web
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80

```
- **Host**: example.com is the domain to route traffic for.
Path-based routing:
- **/api** routes traffic to the service **api-service** on port 80. (api service is Cluster ip with port 80)
- **/web** routes traffic to the service **web-service** on port 80. (web service is Cluster ip with port 80)
- **nginx.ingress.kubernetes.io/rewrite-target**: Ensures the traffic is routed correctly even when subpaths are involved.

#### 5- PVC
```YAML
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

In Pod
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: my-storage
  volumes:
    - name: my-storage
      persistentVolumeClaim:
        claimName: my-pvc

```

- **apiVersion**: v1 (PVC is a core resource in Kubernetes).
- **kind**: PersistentVolumeClaim.
- **metadata.name**: The name of the PVC, my-pvc.
- **spec.accessModes**: Defines the access mode as ReadWriteOnce, meaning that this storage can be mounted as read-write by only one node at a time.
- **resources.requests.storage**: Requests a volume of 5GiB.

#### 6- Skaffold

```YAML
    apiVersion: skaffold/v2beta12
    kind: Config
    deploy:
      kubectl:
        manifests:
          - ./k8s/*
          - ./k8s-dev/*
    build:
      local:
        push: false
      artifacts:      
        - image: rallycoding/client-skaffold
          context: client
          docker:
            dockerfile: Dockerfile.dev
          sync:
            manual:
              - src: "src/**/*.js"
                dest: .
              - src: "src/**/*.css"
                dest: .
              - src: "src/**/*.html"
                dest: .
        - image: rallycoding/worker-skaffold
          context: worker
          docker:
            dockerfile: Dockerfile.dev
          sync:
            manual:
              - src: "*.js"
                dest: .
        - image: rallycoding/server-skaffold
          context: server
          docker:
            dockerfile: Dockerfile.dev
          sync:
            manual:
              - src: "*.js"
                dest: .
```
- **apiVersion**: Specifies the version of the Skaffold API being used.
- **kind**: Indicates that this configuration is of type Config.
- **deploy**: Defines how the application will be deployed.
- **kubectl**: Specifies the use of kubectl for deployment.
- **manifests**: Lists the paths to Kubernetes manifest files. Here, it includes all YAML files in both ```./k8s/``` and ```./k8s-dev/``` directories.
- **build**: Describes how images are built.
- **local**: Indicates that the images will be built locally.
- **push**: false: Specifies that images will not be pushed to a remote registry after building.
- **image**: The name of the Docker image to be built.
- **context**: The directory context for the build (in this case, the client directory).
- **docker**: Configuration for building the Docker image, specifying the Dockerfile.dev file.
- **sync**: Defines manual file syncing:
- **Files** matching ```src/**/*.js```, ```src/**/*.css```, and ```src/**/*.html``` will be synced from the source directory to the destination in the container whenever changes are detected.'''