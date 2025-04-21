#!/bin/bash

# Activate the virtual environment
source ./taskauto/bin/activate

# Run the main.py file with the "-d" flag to complete the tasks by default
python3 main.py -d

# Deactivate the virtual environment
deactivate