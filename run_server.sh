#!/bin/bash
echo "Content-Type: text/plain"
echo ""
echo "Server is running..."

# Activate the virtual environment
source /u/haoqian/public_html/myenv/bin/activate

# Run the Flask server in the background
nohup python3 /u/haoqian/public_html/app.py


# # Sleep
# sleep 60

# # Kill the Flask server process
# PROGRAM_NAME="/u/haoqian/public_html/app.py"

# PID=$(pgrep -f $PROGRAM_NAME)

# # Check if the PID exists and kill the process
# if [ -z "$PID" ]; then
#   echo "No process found with the name $PROGRAM_NAME"
# else
#   kill -9 $PID
#   echo "Process $PROGRAM_NAME with PID $PID has been killed"
# fi

echo ""
echo "The end"