#!/bin/bash
source bin/activate
pip uninstall notebook -y
python3 setup.py bdist_wheel
pip install dist/notebook-7.0.0.dev0-py3-none-any.whl
python3 -m jupyter notebook