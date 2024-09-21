# Common `kubectl` Commands


### General Commands
- `kubectl version` - Display the Kubernetes version being used.
- `kubectl cluster-info` - Show cluster information.
- `kubectl get nodes` - List all nodes in the cluster.
- `kubectl get namespaces` - List all namespaces.
- `kubectl config view` - Show the configuration used by `kubectl`.
- `kubectl config get-contexts` - List available contexts.
- `kubectl config use-context <context-name>` - Switch to a specific context.

### Working with Pods
- `kubectl get pods` - List all pods in the current namespace.
- `kubectl get pods -n <namespace>` - List all pods in a specific namespace.
- `kubectl describe pod <pod-name>` - Display detailed information about a specific pod.
- `kubectl logs <pod-name>` - View the logs of a specific pod.
- `kubectl logs -f <pod-name>` - Stream logs from a running pod.
- `kubectl exec -it <pod-name> -- /bin/bash` - Open a bash terminal in a running pod.
- `kubectl delete pod <pod-name>` - Delete a specific pod.

### Working with Deployments
- `kubectl get deployments` - List all deployments in the current namespace.
- `kubectl describe deployment <deployment-name>` - Show detailed information about a deployment.
- `kubectl apply -f <file.yaml>` - Apply a configuration to a resource from a file.
- `kubectl create -f <file.yaml>` - Create a resource from a file.
- `kubectl rollout status deployment <deployment-name>` - Show the status of a deployment's rollout.
- `kubectl rollout undo deployment <deployment-name>` - Roll back a deployment to the previous version.
- `kubectl scale deployment <deployment-name> --replicas=<count>` - Scale a deployment to a specified number of replicas.

### Working with Services
- `kubectl get services` - List all services.
- `kubectl describe service <service-name>` - Display detailed information about a service.
- `kubectl delete service <service-name>` - Delete a specific service.

### Working with ConfigMaps and Secrets
- `kubectl get configmaps` - List all configmaps.
- `kubectl get secrets` - List all secrets.
- `kubectl describe configmap <configmap-name>` - Display detailed information about a configmap.
- `kubectl describe secret <secret-name>` - Display detailed information about a secret.
- `kubectl create configmap <configmap-name> --from-literal=<key>=<value>` - Create a configmap from a literal value.
- `kubectl create secret generic <secret-name> --from-literal=<key>=<value>` - Create a generic secret from a literal value.

### Working with Namespaces
- `kubectl get namespaces` - List all namespaces.
- `kubectl create namespace <namespace-name>` - Create a new namespace.
- `kubectl delete namespace <namespace-name>` - Delete a specific namespace.

### Viewing Resource Usage
- `kubectl top nodes` - Show resource usage for nodes.
- `kubectl top pods` - Show resource usage for pods.

### Debugging and Troubleshooting
- `kubectl describe <resource> <name>` - Describe a resource (pod, deployment, service, etc.).
- `kubectl get events` - Show cluster events.
- `kubectl get pod <pod-name> -o yaml` - Output the YAML for a specific pod.
- `kubectl get all` - List all resources (pods, services, etc.) in the current namespace.
- `kubectl get all -n <namespace>` - List all resources in a specific namespace.

### Docker 
- `eval $(minikube docker-env)` to attach docker server to kubernates server 