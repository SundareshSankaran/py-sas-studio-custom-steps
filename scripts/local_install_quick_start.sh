#!/usr/bin/env bash

set -euo pipefail


# Parameters:
# 1 = name of virtual environment
# 2 = future use, path to requirements.txt (if different from default)

# Create a virtual environment
python -m venv $1

# Activate virtual environment
. $1/bin/activate

# upgrade pip to latest
python -m pip install --upgrade pip

# Install the package
python -m pip install --upgrade -e .

echo "---------------------------------------------"
echo "Package installed in virtual environment $1"
echo "---------------------------------------------"