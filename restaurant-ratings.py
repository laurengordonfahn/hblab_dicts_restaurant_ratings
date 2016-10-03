# your code goes here
def restaurant_rating(filename):
    """ Function takes arguement of a file name and iterates line by line over file to print out alphabitized restruant and rating.
    No return value only outputs print lines."""
    restaurant_rating_dict = {}
    for restaurant_data in open(filename):
        restaurant_data_list = restaurant_data.rstrip().split(":")
        
        restaurant_rating_dict[restaurant_data_list[0]] = restaurant_data_list[1]
    ordered_restruant = sorted(restaurant_rating_dict.items())

    for tup in ordered_restruant:
        print "{} is rated at {}.".format(tup[0], tup[1])
restaurant_rating("scores.txt")