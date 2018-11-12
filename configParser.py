import configparser, os


def fetch(key = '', file = 'local'):
    config = configparser.ConfigParser()
    config.read(os.path.join("properties/", "{}.conf".format(file)))
    for section in config.sections():
            return config[section].get(key)
