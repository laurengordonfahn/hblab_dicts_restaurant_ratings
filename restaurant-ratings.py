# your code goes here
# def restaurant_rating(filename):
#     """ Function takes arguement of a file name and iterates line by line over file to print out alphabitized restruant and rating.
#     No return value only outputs print lines."""
#     restaurant_rating_dict = {}
#     for restaurant_data in open(filename):
#         restaurant_data_list = restaurant_data.rstrip().split(":")
        
#         restaurant_rating_dict[restaurant_data_list[0]] = restaurant_data_list[1]
#     ordered_restruant = sorted(restaurant_rating_dict.items())

#     for tup in ordered_restruant:
#         print "{} is rated at {}.".format(tup[0], tup[1])

# restaurant_rating("scores.txt")

# def restaurant_rating(filename):
#     """Function takes arguement text file and user input to create an alphabitized print out of resturants and there ratings. 
#     Return value is None only print """
#     restaurant_rating_dict = {}
#     for restaurant_data in open(filename):
#         restaurant_data_list = restaurant_data.rstrip().split(":")
        
#         restaurant_rating_dict[restaurant_data_list[0]] = int(restaurant_data_list[1])

#     user_restaurant = raw_input("Give us a resturant name.\n")
#     user_rating = int(raw_input("Give us a rating for that restruant.\n"))

#     restaurant_rating_dict[user_restaurant] = user_rating

#     ordered_restruant = sorted(restaurant_rating_dict.items())

#     for tup in ordered_restruant:
#         print "{} is rated at {}.".format(tup[0], tup[1])
        
# restaurant_rating("scores.txt")

def open_ratings(filename):
    """ """
    restaurant_data_list = []
    
    for restaurant_data in open(filename):
        restaurant_data_list.append(restaurant_data.rstrip().split(":"))
    return restaurant_data_list
# print open_ratings("scores.txt")

def user_restaurant_rating():
    user_restaurant = raw_input("Give us a resturant name.\n")
    user_rating = int(raw_input("Give us a rating for that restruant.\n"))
    return [user_restaurant, user_rating]

# print user_restaurant_rating()


def driver_input_choices():
    driver_input = raw_input(
"""What would you like to do: 
Type '1' if you would like to see all the resturnts we have rated? 
Type '2' if you would like to add a resturnant and rate it.  
Type 'q' if you would like to quit this program.
""")

    if driver_input == "1":
        return "1"
    elif driver_input == "2":
        return "2"
    elif driver_input.lower() == "q":
        return "q"
    else:
        "We did not understand you."
        driver_input_choices()
# print driver_input_choices()

def create_dict_resturant_ratings(filename):       
    restaurant_rating_dict = {}

    driver_input = driver_input_choices()
    if driver_input == "1":

        restaurant_data_list = open_ratings(filename)  
        
        restaurant_rating_dict = {}
        for resturant_list in restaurant_data_list:
            print resturant_list
            restaurant_rating_dict[resturant_list[0]] = int(resturant_list[1])
        
        ordered_restruant = sorted(restaurant_rating_dict.items())

        for tup in ordered_restruant:
            print "{} is rated at {}.".format(tup[0], tup[1])

    elif driver_input == "2":
        restaurant_data_list = open_ratings(filename)  
        user_input_list = user_restaurant_rating()
        restaurant_rating_dict = {}

        restaurant_rating_dict[user_restaurant] = user_rating

        for resturant_list in restaurant_data_list:
            restaurant_rating_dict[restaurant_data_list[0]] = int(restaurant_data_list[1])
        
        ordered_restruant = sorted(restaurant_rating_dict.items())

        for tup in ordered_restruant:
            print "{} is rated at {}.".format(tup[0], tup[1])
    
    else: 
        "Program closing."
        return
        
create_dict_resturant_ratings("scores.txt")