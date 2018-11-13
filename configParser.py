import configparser, os


def fetch(key, file, section):
    config = configparser.ConfigParser()
    config.read(os.path.join("properties/", "{}.conf".format(file)))
    return config[section].get(key)
