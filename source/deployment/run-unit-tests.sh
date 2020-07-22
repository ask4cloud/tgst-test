#!/bin/bash
#echo 'pip3 install -r ../source/requirements.txt -t ../source/ --user'
# pip3 install -r ../source/requirements.txt -t ../source/ --user
echo 'pip3 install -r ../source/requirements.txt -t ../source/'
pip3 install -r ../source/requirements.txt -t ../source/
echo 'pip3 install -r ../source/testing_requirements.txt'
pip3 install -r ../source/testing_requirements.txt --user
echo 'cd ../source && python3 -m pytest tests && cd -'
cd ../source && python3 -m pytest tests && cd -