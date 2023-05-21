#!/bin/bash

echo "Waiting for MySQL to start..."
sleep 30

echo "MySQL started."

python3 ./import_script.py
