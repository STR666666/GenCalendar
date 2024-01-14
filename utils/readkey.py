import os
import configparser

def readkey():
    config_path = "utils/apikey.ini"
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def set_env():
    config = readkey()
    os.environ["OPENAI_API_KEY"] = config["OpenAI"]["OPENAI_API_KEY"] if os.environ.get('OPENAI_API_KEY') is None else os.environ["OPENAI_API_KEY"]
