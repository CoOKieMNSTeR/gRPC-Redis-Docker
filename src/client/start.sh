#!/bin/bash
while ! nc -z localhost 5672; do sleep 3; done
python grpc.client.py
