ansible-sqitch
=========

Ansible role that installs Sqitch with PostgreSQL, MySQL or SQLite support on Debian/Ubuntu.


Requirements
------------

This role has no pre-requisites. 

Dependencies
------------

The dependencies depend on the database to install.

PostgreSQL: `libdbd-pg-perl`, `postgresql-client`

MySQL: `libdbd-mysql-perl`, `mysql-client`

SQLite: `libdbd-sqlite3-perl`, `sqlite3`

Variables
---------

```yml
sqitch_database_support: 
 - PostgreSQL  # Can be any of SQLite, MySQL, PostgrSQL. Install sqitch with support to this database. See Example Playbook for usage

```
Example Playbook
----------------
One database 
```yml
- hosts: servers
      roles:
         - role: ansible-sqitch
           vars:
            sqitch_database_support: 
              - PostgreSQL
```
Multiple databases
```yml
- hosts: servers
      roles:
         - role: ansible-sqitch
           vars:
            sqitch_database_support: 
              - PostgreSQL
              - MySQL
```


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
