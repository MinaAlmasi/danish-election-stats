#!/bin/bash

# create virtual environment
python -m venv env

# activate virtual environment 
source ./env/bin/activate

echo -e "[INFO:] Installing necessary requirements..."

# install reqs
python -m pip install -r requirements.txt

# deactivate env 
deactivate

echo -e "[INFO:] Setup complete!"