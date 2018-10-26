#!/bin/bash
DIR="django-dev"
if [ -d "$DIR" ]; then
  echo "venv $DIR found"
  source $DIR/bin/activate
  echo "venv activated.."
  python utils/check_con.py
  code ./ClientMonitor
else
  echo "venv not found...creating one"
  python -m pip3 install --upgrade virtualenv
  virtualenv -p python3 $DIR
  source $DIR/bin/activate
  ./$DIR/bin/python3 -m pip install -r requirements.txt
  echo "venv created successfully and activated.."
  python utils/check_con.py
  code ./ClientMonitor
fi

