# Demo Provisioner

Ansible based demo provisioner.
It currently works with OCP clusters from RHPDS and OpenTLC.


## Usage 

```
ansible-playbook provision.yml -e @extra_vars.yml
```

where `extra_vars.yml` contains the following variables:
- `demo_name`: ccfd as default
- `ocp_host`: API URL of the OCP cluster
- `ocp_user`, `ocp_pass`: OCP Cluster credentials

## MacOS notes:

Use `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`

