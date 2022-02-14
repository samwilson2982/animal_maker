import requests
from bs4 import BeautifulSoup
import time
import ruamel.yaml
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq
yaml = ruamel.yaml.YAML()
def get_anmials():
    URL = "https://a-z-animals.com/animals/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    all_lists = soup.find_all("ul", {"class": "list-unstyled row"})
    for l in all_lists:
        a_tags = l.findAll("a", recursive=True)
        for a in a_tags:
            config_name = a.text.replace(" ", "_")
            config_path = "src/configs/{}.yaml".format(config_name)
            config_attributes = {}
            try:
                config_attributes = get_attributes(a.get("href"), config_attributes)
                flag = True
                if "Group" in config_attributes:
                    if config_attributes["Group"] == "Dog" or config_attributes["Group"] == "Hound":
                        flag = False
                if "Dog group" in config_attributes:
                    flag = False
                if flag:
                    print("getting animal {}".format(a.text))
                    config_attributes["name"] = dq(config_name)
                    sortedDict = dict(sorted(config_attributes.items(), key=lambda x: x[0].lower()))
                    with open(config_path, "w+", encoding="utf-8") as f:
                        yaml.dump(sortedDict, f)
                else:
                    pass
            except Exception as e:
                print("{}".format(str(e)))



def get_attributes(URL, d={}):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #dict_keys = soup.find("div", {"class": "col-lg"}).findChildren("dt",recursive=True)
    dict_keys = soup.find_all("dt", recursive=True)
    #dict_values = soup.find("div", {"class": "col-lg"}).findChildren("dd",recursive=True)
    dict_values = soup.find_all("dd", recursive=True)
    for dk, dv in zip(dict_keys, dict_values):

        if type(dv.text) == str:
            d[dk.text] = dq((dv.text).rstrip().replace("\n", ""))
        else:
            d[dk.text.lower()] = dq(str(dv.text))
    return d

def pet_subcatagory(URL, parent_animal):
    try:
        print("sub catagory found! {}".format(parent_animal))
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        sub_catagories = soup.find("ul", {"class": "list-unstyled row"}).findChildren("a",recursive=True)
        for a in sub_catagories:
            print("getting {} subcatagory {}".format(parent_animal, a.text))

            try:
                config_name = ("{}-{}".format(parent_animal, a.text)).replace(" ", "_")
                config_path = "src/configs/{}.yaml".format(config_name)
                config_attributes = {}
                config_attributes = get_attributes(a.get("href"), config_attributes)
                config_attributes["name"] = '"'+a.text+'"'
                sortedDict = dict(sorted(config_attributes.items(), key=lambda x: x[0].lower()))
                with open(config_path, "w+") as f:
                    f.write(yaml.safe_dump(sortedDict))
            except:
                print("error getting breed {}".format(a.text))
    except:
        print("just forget this one :( {}".format(parent_animal))

get_anmials()

