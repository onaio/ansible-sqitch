ansible-sqitch
=========

Ansible role that installs sqitch on Debian/Ubuntu.

Requirements
------------

This role has no pre-requisites. 

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------


    - hosts: servers
      roles:
         - ansible-sqitch

Testing
------------

This project uses molecule for testing using a docker driver and testinfra as the verifier

Start by creating a virtual environment and install the pypi packages in `requirements.txt`

Then to run the full test sequence

```sh
molecule test
```

License
-------

APACHE-2

Author Information
------------------

[Ona Engineering](https://ona.io)
