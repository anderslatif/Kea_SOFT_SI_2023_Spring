

## Generate MySQL documentation

Use MRO to generate HTML docs (only MySQL):

> npx mro



## Backup MySQL with the mysqldump tool

### Installation

Windows: Should be included when installing MySQL.

MacOS:

> brew install mysql-client

Once installed the final output recommends you to do this:

> echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.zshrc

Fedora:

> sudo apt install mysql-client

### Backup into sql file

To backup a MySQL database (data + schema) use mysqldump:

> mysqldump -u <username> -p <database_name> > <file_name.sql>

Ignore tables by adding: 

> mysqldump -u <username> -p <database_name> --ignore-table=<table_name> > <file_name.sql>

### Restore from sql file

> mysqldump -u username -p <database_name> < <file_name.sql>

Can also do this from the MySQL prompt:

> mysql> USE <database_name>;

> mysql> source <file_name.sql>;
