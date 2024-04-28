#!/bin/bash
pscli vault  read -- 'secret/data/etl_application' > secret.tmp
while IFS=$' ' read -r col1 col2
do
    if [ "$col1" = "username" ]; then
    	export API_USER=$col2
    fi
    if [ "$col1" = "password" ]; then
    	export API_PASS=$col2
    fi
done <secret.tmp
if [[ -z "${API_USER}" ]]; then
    echo "API_USER not found"
    rm -fr secret.tmp
    exit 1
fi
if [[ -z "${API_PASS}" ]]; then
    echo "API_PASS not found"
    rm -fr secret.tmp
    exit 1
fi
rm -fr secret.tmp