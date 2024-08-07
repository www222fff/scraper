#!/bin/bash

export EMAIL_ADDRESS="danny.a.wang@a.com"
export EMAIL_PASSWORD="addsfas"

python collect_reward.py

if [ $? -ne 0 ]; then
    echo "collect_reward.py failed"
    exit 1
fi

python scraper_web.py

if [ $? -ne 0 ]; then
    echo "scraper-web.py failed"
    exit 1
fi

echo "Complete!"
