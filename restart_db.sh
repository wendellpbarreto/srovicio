#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: Sroaddiction
# @doc: dependencies.sh
# @desc: 
# ----------------------------------


while true; do
    read -p "Are you using Linux (y or n)? " yn
    case $yn in
        [Yy]* )
        	sudo -u postgres psql -c 'DROP DATABASE sroaddiction_db'
			sudo -u postgres psql -c 'CREATE DATABASE sroaddiction_db'
			sudo -u postgres psql -c 'CREATE USER sroaddiction_admin'
			sudo -u postgres psql -c "ALTER USER sroaddiction_admin WITH PASSWORD 'zaaNF=Olzi)ytZ'"
			sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE sroaddiction_db TO sroaddiction_admin'
			sudo -u postgres psql -d sroaddiction_db -c 'CREATE EXTENSION hstore' 

			break;;
        [Nn]* ) 
			psql -c 'DROP DATABASE sroaddiction_db'
			psql -c 'CREATE DATABASE sroaddiction_db'
			psql -c 'CREATE USER sroaddiction_admin'
			sudo -u postgres psql -c "ALTER USER sroaddiction_admin WITH PASSWORD 'zaaNF=Olzi)ytZ'"
			psql -c 'GRANT ALL PRIVILEGES ON DATABASE sroaddiction_db TO sroaddiction_admin'
			psql -d sroaddiction_db -c 'CREATE EXTENSION hstore'

			break;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo '[>] Syncing db...'
python manage.py syncdb

echo '[>] Collecting static files...'
python manage.py collectstatic