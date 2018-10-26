#!/bin/bash
echo "*/1 * * * * python $PWD/send_data.py > $PWD/cronlog.log" > /var/spool/cron/crontabs/$USER
echo "done"
echo "file edited :/var/spool/cron/crontabs/$USER"
cat /var/spool/cron/crontabs/$USER
echo "py file : python $PWD/send_data.py"
