#!/usr/bin/env bash

set -euo pipefail

python -m venv sasstep

. sasstep/bin/activate

python -m pip install --upgrade pip

python -m pip install uv

uv pip install setuptools py-sas-studio-custom-steps ipykernel jupyter 

python -m ipykernel install --user --name=sasstep

deactivate

