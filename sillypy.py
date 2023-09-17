import configparser
import getopt
import sys

args = sys.argv[1:]
options = "hmo:f:"
long_options = ["help", "my_file", "output=", "config="]
default_ini = "sillypy.ini"
Config = configparser.ConfigParser()
Config.read(default_ini)
try:
    args, vals = getopt.getopt(args, options, long_options)
    for arg, val in args:
        if arg in ("-h", "--help"):
            print(
                "Usage: %s"
                % """
            Simple python script: takes arguments, prints out .ini file.
            -h, --help: this help
            -o, --output= : prints out value
            -f, --config=config.ini : use config.ini instead of default
            -m : returns own file name
"""
            )
            exit()
        elif arg in ("-m", "--my_file"):
            print("Displaying file_name:", sys.argv[0])
        elif arg in ("-o", "--output"):
            print(f"-o value is: {val}")
        elif arg in ("-f", "--config"):
            Config = configparser.ConfigParser()
            Config.read(val)
except getopt.error as err:
    print(str(err))
#
print(Config.sections())
for section in Config.sections():
    for option in Config[section]:
        print(option, Config.get(section, option))
