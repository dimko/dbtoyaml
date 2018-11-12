import argparse
import postgresClient
import yaml


def toYaml(table, columns=None):
    ymlFile = file('out/{}.yaml'.format(table), 'w')
    dbData = postgresClient.readTable(table, columns)

    for data in dbData:
        yaml.dump(data, stream=ymlFile, default_flow_style=False)
        ymlFile.write("\r")


def parseArgs(table, columns):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', required=True, default='users')
    parser.add_argument('-c', '--columns', required=False, nargs='*')
    arguments = parser.parse_args(table, columns)

    return (arguments.table, arguments.columns)


if __name__ == "__main__":
    toYaml(parseArgs('-t table', '-c [\'email\']'))
