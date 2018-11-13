#!/usr/bin/env python2.7

import postgresClient, yaml, argParser


def toYaml(tables=argParser.parseTablesColumns().tables, columns=argParser.parseTablesColumns().columns, config=argParser.parseTablesColumns().config, section=argParser.parseTablesColumns().section):
    print "Create yml files for tables: {} and columns: {}".format(", ".join(tables), ", ".join(columns))
    for t in tables:
        ymlFile = file('out/{}.yml'.format(t), 'w')
        dbData = postgresClient.readTable(table=t, columns=columns, conf=config, section=section)

        for data in dbData:
            yaml.dump(data, stream=ymlFile, default_flow_style=False)
            ymlFile.write("\r")


if __name__ == "__main__":
    toYaml()
