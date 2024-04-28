#!/bin/bash
pscli vault  read -- -field=display_name /auth/token/lookup-self
pscli vault  read -- ------- > data_tooling_credentials.tmp
awk '/private_key_data/ {print $2}' data_tooling_credentials.tmp | base64 --decode > key.json

#awk '/lease_id/ {print $2}' data_tooling_credentials.tmp | VAULT_NAMESPACE=sbg/gcp/ VAULT_TOKEN=$(cat ~/.vault-token) xargs pscli vault lease revoke
#rm data_tooling_credentials.tmp
#rm key.json