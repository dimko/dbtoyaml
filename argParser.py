import argparse, sys

def parseTablesColumns():
    parser = argparse.ArgumentParser(description='Provide a list of tables and columns to be dumped')
    parser.add_argument('-t', '--tables', required=True, help='list of tables to dump', nargs='+')
    parser.add_argument('-c', '--columns', required=True, nargs='+', help='list of columns to dump',)
    arguments = parser.parse_args()
    return arguments
    # return (arguments.table, arguments.columns)

if __name__ == "__main__":
    parseTablesColumns()