#!/bin/bash

# Write a Nagios/Icinga plugin that detects if child processes of crond have
# been running for too long (configurable in minutes or seconds, one threshold
# which yields a warning and one which is critical). It should output the PIDs
# and executable names of the long-runners and an exit code that corresponds to
# the oldest process under consideration

# Threshold in seconds
WARNING_TH=600
ERROR_TH=1200

oldest_child_pid=0
oldest_time=0

crond_pid=`ps auxf | awk '$11 == "crond" { print $2 }'`

for child in `ps -ef | awk -v x=$crond_pid '$3 == x { print $2 }'`
do 
	# Here you have one of of the elements of tree 
    # parent -> child
    child_time=`ps -p $child -o etime= | awk -F : '{ print $1*3600+$2*60+$3}'`

    if [ $child_time -gt $WARNING_TH ]; then
     	if [ $child_time -gt $ERROR_TH ]; then
     		child_name=`ps ax | awk -v x=$child '$1 == x { print $5 }'`
     		if [ $child_time -gt $oldest_time ]; then
                    oldest_time=$child_time
                    oldest_child_pid=$child
               fi
     		echo "ERROR: process $child $child_name is running for $child_time seconds!"
     	else
     	    child_name=`ps ax | awk -v x=$child '$1 == x { print $5 }'`
               if [ $child_time -gt $oldest_time ]; then
                    oldest_time=$child_time
                    oldest_child_pid=$child
               fi
     	    echo "Warning: process $child $child_name is running for $child_time seconds!"
        fi
    fi
done

if [ $oldest_time -gt 0 ]; then
	exit $oldest_child_pid
else
	exit 0 # Everything is fine
fi