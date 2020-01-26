class Slacker:
    def __init__(self, id, name, time_period,
                 address_name, restaurant_name,
                 address_latlon, restaurant_latlon, food_order):
        self.id = id
        self.name = name
        self.time_period = time_period
        self.address_name = address_name
        self.restaurant_name = restaurant_name
        self.address_latlon = address_latlon
        self.restaurant_latlon = restaurant_latlon
        self.food_order = food_order



class DaBaoer:
    def __init__(self, id, name, address_name, restaurant_name, address_latlon, restaurant_latlon):
        self.id = id
        self.name = name
        self.address_name = address_name
        self.restaurant_name = restaurant_name
        self.address_latlon = address_latlon
        self.restaurant_latlon = restaurant_latlon

    def get_slackers(self, slacker_list):
        self.slacker_list = slacker_list
        self.slacker = ""

class uselessClass:
    def __init__(self, name, address):
        self.name = name
        self.address = address








