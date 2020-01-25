

class Slacker:
    def __init__(self, id, name, time_period, address_latlon, restaurant_latlon):
        self.id = id
        self.name = name
        self.time_period = time_period
        self.address_latlon = address_latlon
        self.restaurant_latlon = restaurant_latlon

    def get_order(self, food_order):
        self.food_order = food_order




class DaBaoer:
    def __init__(self, id, name, address_latlon, restaurant_latlon):
        self.id = id
        self.name = name
        self.address_latlon = address_latlon
        self.restaurant_latlon = restaurant_latlon

    def get_slackers(self, slacker_list):
        self.slacker_list = slacker_list
        self.slacker = ""






