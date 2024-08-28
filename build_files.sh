#!/bin/bash

# Ensure pip is available
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing..."
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
fi

# Install dependencies
pip install -r requirements.txt

# Collect static files (if necessary)
python manage.py collectstatic --noinput
