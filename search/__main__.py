from configparser import ConfigParser
from importlib import resources
import sys

def main():
    cnf = ConfigParser()
    cnf.read_string(resources.read_text("search", "config.txt"))
    url = cnf.get("feed", "url")



if __name__ == "__main__":
    main()