# Provisioner

Ansible based demo provisioner.


Usage: 

```
ansible-playbook provision.yml -e @extra_vars.yml
```

where `extra_vars.yml` contains the following variables:
- demo_name: ccfd as default
- ocp_host: API URL of the OCP cluster
- ocp_user
- ocp_pass
