#!/bin/sh
while true; do
    python url_test.py
    sleep ${CHECK_INTERVAL:-60}
    if [ $? -ne 0 ]; then
        echo "Error occurred, exiting..."
        exit 1
    fi
done
