#!/bin/bash# 


# - Change the permissions on the script to make it executable: chmod +x install.sh
# - Run the script from the command line with super-user rights (required to install packages via apt): sudo ./install.sh
# - Run the script main.py: python main.py or python main <N_TREES>


# Install Python
apt-get -y update
apt-get install -y python3-pip python3-venv

# Create empty virtual environment
python -m venv bankml_env
source bankml_env/bin/activate

# Install project dependencies
pip install -r requirements.txt
