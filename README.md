# Dyntrace
Dyntrace update job
create vault_api_key.yml vasult file with api-key variable stored.
ansible-playbook activegates_playbook.yml --ask-vault-pass -e "@vault_api_key.yml"
