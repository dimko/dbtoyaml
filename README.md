# dbtoyaml
Simple tool to dump postgresSQL db data to yaml formated files

#Preconfiguration
create a .conf file located in properties/ directory to point to your postgres database, or edit the pre-existing local.conf

#Usage

./yaml_dumper.py -T <table_name> -C <column_names>

e.g ./yaml_dumper.py -T users -C email names


#Optional Parameters

You can specify the configuration file to be used and the database to target.

Default values are local.conf and workable_database

./yaml_dumper.py -T <table_name> -C <column_names> -c < .conf file> -s <section file>

e.g ./yaml_dumper.py -T users -C email names -c stg7.conf -s shield_database