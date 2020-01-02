# Fork Monitor

Ansible roles and playbook for provisioning http://forkmon.ethdevops.io

## Usage

```
> cd ansible
> ansible-playbook -i inventory/production ./mainchain.yaml --verbose --check
```

## Roles

* `python` - installs Python 2 and pip

* `docker` - installs Docker and docker-py (needed for Ansible docker module)

* `start_nodes` - checks if geth (pre- and post- byzantium fork) and parity nodes are running, and starts them

* `start_status` - builds fork monitor app and starts it
