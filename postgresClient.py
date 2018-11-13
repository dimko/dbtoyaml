import psycopg2
import psycopg2.extras as extras
import configParser as config


def connect(conf, section):
    try:
        conn = psycopg2.connect(database=config.fetch(key='name', file=conf, section=section),
                                host=config.fetch(key='localhost', file=conf, section=section),
                                port=config.fetch(key='port', file=conf, section=section),
                                user=config.fetch(key='user', file=conf, section=section),
                                password=config.fetch(key='password', file=conf, section=section), cursor_factory=extras.DictCursor)
        return conn
    except:
        print "Connection error, please check your connection settings"
        raise

def close(connection):
    try:
        connection.cur.close()
    except:
        print "Connection not closed!"
        raise



def readTable(table, columns, conf, section):
    results = []
    try:
        conn = connect(conf=conf, section=section)
        cur = conn.cursor()
        cur.execute("SELECT {} FROM {}".format(", ".join(columns), table))
        for i in cur.fetchall():
            results.append(dict(i))
        if results is not None:
            return results
    except:
        print "No results were returned"
        raise

if __name__ == "__main__":
    readTable('users', ['email', 'name'])