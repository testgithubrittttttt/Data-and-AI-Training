import configparser
config = configparser.ConfigParser()

#python directory
config["database"] = {
    "host":"localhost",
    "port":3386,
    "user": "root",
    "password":"admin1386"
}
with open("app.ini","w") as configfile:
    config.write(configfile)
config.read("app.ini")
print(config["database"]["host"])
