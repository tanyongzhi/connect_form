from dummy_people import *
from helper_functions import *
from constants import *

all_slackers = [slacker_adam, slacker_betty, slacker_catie]
optimized_slacker_list = get_optimized_slacker_list(all_slackers, dabaoer_baobao)

print(optimized_slacker_list[0].name)