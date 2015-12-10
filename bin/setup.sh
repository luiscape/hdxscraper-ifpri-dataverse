#!/bin/bash

#
#  Settingup Virtual Environment.
#
virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
