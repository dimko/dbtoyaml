import argparse, sys

def parseTablesColumns():
    parser = argparse.ArgumentParser(description='Provide a list of tables and columns to be dumped')
    parser.add_argument('-T', '--tables', required=True, help='list of tables to dump', nargs='+')
    parser.add_argument('-C', '--columns', required=True, nargs='+', help='list of columns to dump')
    parser.add_argument('-c', '--config', required=False, help='conf file', default='local')
    parser.add_argument('-s', '--section', required=False, help='section of conf file to be used', default='workable_database')
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    parseTablesColumns()