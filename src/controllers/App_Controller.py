from ..helpers import YamlHelper

class AppController(object):
    def __init__(self):
        print(YamlHelper.load_file("../configs/Axolotl.yaml"))


















        # todo animal class,
        #   Have few attributes:
        #   legs (ex. deer legs)
        #   body (snake body)
        #   head (alligator head)
        #   covering (naked, fur, scales, plates, chitin)
        #   tail (rabbit tail)
        #   teeth (sharks teeth)

        #todo
        #   create a class for evrey animal in the world, store in configs
        #   get from website "https://a-z-animals.com/animals/"
        #   build a scraper tool
        #   all animals will have a few attributes on the site like:
        #       Prey
        #       group behavior
        #       Most Distinctive Feature
        #       Gestation Period
        #       Habitat
        #       Diet
        #       Lifestyle
        #       Skin Type
        #       etc
        #   all of these will be scraped and put into a zeperat yaml, for example Zorse.yaml

        # todo logic will have to be written to take the correct attribute from correct part
        #   ex. teeth -> food type, you cant have shark teeth and eat spinich
        #   ex. legs -> speed
        #   colors should be blended, at least somewhat, with distinct feature
        #   should be able to filter/group by habitat:
        #       ex. habitat='grassland' if habitat in animal.habitat ...
        #       then only pull animals from that selective grouping, making the amalgam plausible
        #   similarly group by diet, mammal, reptile, speed, lifespan, or any other group
        #       look into python.pandas for this