# Demo Provisioner

Ansible based demo provisioner.
It currently works with OCP clusters from RHPDS and OpenTLC.

## Installation

Clone this repo, change to the correct branch (if needed), then:

```
python3 -m venv myenv
pip install pip --upgrade
pip install -r requirements.txt 
```

## Usage 

```
ansible-playbook provision.yml -e @extra_vars.yml
```

where `extra_vars.yml` contains the following variables:
- `demo_name`: ccfd as default
- `ocp_host`: API URL of the OCP cluster
- `ocp_user`, `ocp_pass`: OCP Cluster credentials
- `ocs_version`: It must match your OCP cluster version, such as `stable-4.6`

Regarding `ocs_version`, it should accept same version as OCP cluster and 
one version above and below (OCP = 4.7 ==> ODF/OCS = 4.6, 4.7, 4.8).

See `extra_vars_example.yml` as example.


## MacOS notes:

Use `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`

