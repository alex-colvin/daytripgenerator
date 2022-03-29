import random
destinations =["Oak Island, North Carolina","Honolulu, Hawaii","Charleston, South Carolina","Epcot at Disney World, Orlando, Florida","Bar Harbor, Maine","Raleigh, North Carolina"]
#selects list of restaurants for random selection based on randomly selected destination.
def get_restaraunts_by_location (location):
    restaraunts =[""]
    oak_island_restaraunts = ["Swain's Seafood and Cut Restaurant","Turtle Island Restaurant","Shagger Jacks","Tranquil Harbour Restaurant & Bar","Little Bit's Grill","Thai By the Sea","Duffer's Pub & Grille","Long Beach Diner","Oak Island Sub Shop","Bob's Dogs"]
    honolulu_restaraunts = ["Liliha's Bakery...The Manapua is amazing", "South Shore Market","South Shore Market","The Pig and The Lady","53 By The Sea","Moku Kitchen","Mac 24/7","Kaneohe Pancake House...MMM...Red Velvet Pancakes","Koa Pancake House...Loco Moco's!!","Taco Del Mar...Make sure to get your burritos 'wet!'","Ono Korean BBQ"]
    charleston_restaraunts = ["Halls Chophouse...Get ready to lighten your wallet!","Hank's Seafood Restaurant","High Cotton Charleston Restaurant","Butcher & Bee","Poogan's Porch","Magnolias","Taco Boy...Great fish tacos!","Smokey Bones N. Charleston","Rodney Scott's BBQ - Charleston","Red's Ice House...Great 'Shrip Po Boys!'"]
    orlando_restaraunts = ["Rose & Crown Dining Room","Tokyo Dining","Choza de Margarita","Yorkshire County Fish Ship","Crepes des Chefs de France","Joy of Tea","Lotus Bloom Cafe","Refreshment Outpost","Biergarten Restaraunt","Tutto Gusto Wine Cellar"]
    bar_harbor_restaraunts = ["Geddy's","Galyn's","Side Street Cafe","McKay's Public House","Paddy's Irish Pub & Restaurant","Havana","Bar Harbor Lobster Co....Wicked Good Lobstah!!","Testa's Bar & Grill","Thirsty Whale Tavern","Paddy's food spirits and ale"]
    raleigh_restaraunts = ["Lemon Thai Restaraunt...Great Pad Thai!!","Poke Burri...SUSHI BURRITOS!?!?!", "Taza Grille...Hey Boss! Come on Down!","Humble Pie","Gravy...Enough Said","Oak Steakhouse","Snoopy's Hot Dogs & More...Best Hot Dogs this side of New York","Angus Barn...Get ready to lighten your wallet!","Pressed by Spanglish...Great Paninis","Los Tres Magueyes...Best Queso Ever!" ]
    if location == "Oak Island, North Carolina":
        restaraunts = oak_island_restaraunts
    elif location == "Honolulu, Hawaii":
        restaraunts = honolulu_restaraunts
    elif location == "Charleston, South Carolina":
        restaraunts = charleston_restaraunts
    elif location == "Epcot at Disney World, Orlando, Florida":
        restaraunts = orlando_restaraunts
    elif location == "Bar Harbor, Maine":
        restaraunts = bar_harbor_restaraunts
    elif location == "Raleigh, North Carolina":
        restaraunts = raleigh_restaraunts
    return restaraunts
#changes the default transportation options based on available transportation at randomly selected locations.
def get_transportation_by_location (location):
    modes_of_transportation = ["a Car","a Bus","a Train","an Uber","a Lyft"]
    if location == "Oak Island, North Carolina":
        modes_of_transportation.append("a Ferry")
        modes_of_transportation.append("My car. I'll come pick you up!")
    elif location == "Honolulu, Hawaii":
        modes_of_transportation[1] = "Da Bus"
        modes_of_transportation.append("the Super Ferry")
    elif location == "Charleston, South Carolina":
        modes_of_transportation.append("a Trolley")
        modes_of_transportation.append("a Horse and Buggy")
    elif location == "Epcot at Disney World, Orlando, Florida":
        modes_of_transportation.append("the Tram")
        modes_of_transportation.append("the Skyliner")
    elif location == "Bar Harbor, Maine":
        modes_of_transportation.append("a Bicycle")
        modes_of_transportation.append("an RV")
    elif location == "Raleigh, North Carolina":
        modes_of_transportation.append("a Byrd Scooter")
        modes_of_transportation.append("a Trolley Pub Car")
    return modes_of_transportation
#selects list of entertainment options based on randomly selected destination.
def get_entertainment_by_location (location):
    entertainment =[""]
    oak_island_entertainment = ["Go Fishing on the Pier","Fly a Kite","Go Flounder Gigging at Night","Read a Book on the Beach","Play Beach Volleyball","Play Miniature Golf","Go to the Aquarium","Swim in the Waves"]
    honolulu_entertainment = ["Hike Diamondhead","Hike the Stairway to Heaven","Golf at Turtle Bay","Go Cliff Jumping at China Walls","Take Surf Lessons at Waikiki Beach","Hike Kokohead","Go on a Whale Watching Tour","Go on a Sunset Cruise"]
    charleston_entertainment = ["Tour Fort Sumter","Tour the USS Yorktown","Go on a Haunted Carriage Tour","Visit Bee City Zoo","Kayak at Sullivan's Island","Go to the Water Park","Visit the Battery","Go to the Movies","Visit Boone Hall Plantation"]
    orlando_entertainment = ["Ride Test Track","Ride Mission SPACE","Ride Soarin' Around the World","Ride Frozen Ever After","Ride The Seas with Nemo and Friends","Ride Guardians of the Galaxy"]
    bar_harbor_entertainment = ["Go Blueberry Picking","Go Whale Watching","Go on a Lobster Fishing tour","Hike in Acadia National Park","Charter a Fishing Vessel","Go Kayaking","Go on a Sailboat Tour"]
    raleigh_entertainment = ["Go Ice Skating","Race go-carts","Visit the Art Museum","Go to a Hurricanes Game","Go to an NC State Game","Go to a Durham Bulls Game","BMX at Lion's Park","Hike at Fall's Lake","Get your Jump on at Defy Gravity","Kayak Down the Nuese River","Bike the Raleigh Greenway","Go to Boxcar Bar and Arcade"]
    if location == "Oak Island, North Carolina":
        entertainment = oak_island_entertainment
    elif location == "Honolulu, Hawaii":
        entertainment = honolulu_entertainment
    elif location == "Charleston, South Carolina":
        entertainment = charleston_entertainment
    elif location == "Epcot at Disney World, Orlando, Florida":
        entertainment = orlando_entertainment
    elif location == "Bar Harbor, Maine":
        entertainment = bar_harbor_entertainment
    elif location == "Raleigh, North Carolina":
        entertainment = raleigh_entertainment
    return entertainment
#randomly selects item from a list
def get_random_selection (some_list):
    random_selection = random.choice(some_list)
    return random_selection
#lets user choose y/n based on the randomly selected options.
def get_user_choice(some_list, category_name):
    user_choice = "n"
    while user_choice.lower() == "n":
            random_selection = get_random_selection(some_list)
            user_choice = input(f"Your randomly selected {category_name} is '{random_selection}'. Do you like this choice? Enter y/n :")
            if user_choice.lower() == 'n':
                print("Sorry, Let's try this again...")
                some_list.remove(random_selection)
            else:
                print(f"Great Choice! You chose '{random_selection}'.")
    return random_selection
final_destination = get_user_choice (destinations, "Destination")
restaraunts = get_restaraunts_by_location (final_destination)
final_restaurant = get_user_choice (restaraunts, "Restaurant")
modes_of_transportation = get_transportation_by_location (final_destination)
final_mode_of_transportation = get_user_choice (modes_of_transportation, "Mode of Transportation")
forms_of_entertainment = get_entertainment_by_location (final_destination)
final_form_of_entertainment = get_user_choice (forms_of_entertainment, "Form of Entertainment")
print(f"""Congratulations! Your day trip booking is complete.
You have chosen to travel to '{final_destination}'.
You have chosen to dine at '{final_restaurant}'.
You have chosen to get around in/on '{final_mode_of_transportation}'.
You have chosen to '{final_form_of_entertainment}'.
Have a great time!!""")
