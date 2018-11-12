# dbtoyaml
Simple tool to dump postgresSQL db data to yaml formated files

#Preconfiguration
create a .conf file located in properties/ directory to point to your postgres database, or edit the pre-existing local.conf

#Usage py
./yaml_dumper.py -t <table_name> -c <column_names>

e.g ./yaml_dumper.py -t users -c email, names