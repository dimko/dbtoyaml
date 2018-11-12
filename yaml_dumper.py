import postgresClient, yaml, argParser


def toYaml(tables = argParser.parseTablesColumns().tables, columns = argParser.parseTablesColumns().columns):


    print "Create yml files for tables: {} and columns: {}".format(", ".join(tables), ", ".join(columns))
    for t in tables:
        ymlFile = file('out/{}.yml'.format(t), 'w')
        dbData = postgresClient.readTable(t, columns)

        for data in dbData:
            yaml.dump(data, stream=ymlFile, default_flow_style=False)
            ymlFile.write("\r")

if __name__ == "__main__":
    toYaml()
