#!/bin/bash

eval $(minikube docker-env)

docker build -t hello-node:v2 .
kubectl set image deployment/hello-node hello-node=hello-node:v2
