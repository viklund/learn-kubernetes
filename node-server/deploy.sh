#!/bin/bash

kubectl run hello-node --image=hello-node:v1 --port=8080 --image-pull-policy=Never
kubectl expose deployment hello-node --type=LoadBalancer
