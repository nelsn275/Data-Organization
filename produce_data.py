import csv
import math

# GLOBALS                     Index #
I_NAME =                        0
I_FORM =                        1
I_RETAIL_PRICE =                2
I_RETAIL_PRICE_UNIT =           3
I_YIELD =                       4
I_CUP_EQUIVILENT_SIZE =         5
I_CUP_EQUIVILENT_UNIT =         6
I_CUP_EQUIVILENT_PRICE =        7

#                           File Path
FRUIT_DATA_2022_PATH = "data/fruit2022.csv"
VEGGIE_DATA_2022_PATH = "data/veggies2022.csv"

def main():
    """Run the Program"""
    produce = get_input()
    produce_ratio(produce)


def load_csv_file(filename):
    """Load data from a csv file into a list"""

    data_list = []

    # Open the CSV file and return a list of lists of produce data
    with open (filename) as data:
        food_data = csv.reader(data, delimiter= ',')
        next(food_data)
        for row in food_data:
            data_list.append(row)
        return data_list

def get_input():
    """Figure out what fruit or vegetable the user wants to receive data on"""

    # Create a while loop that will run until someone has picked out a vegetable or fruit
    done = False
    while not done:

        type = input("\nDo you want a Fruit or Vegetable (F/V) ").upper()

        # If the user inputs F or Fruit load the fruit CSV form and search for the fruit requested. Return the fruit list
        if type == "FRUIT" or type == "F":

            data = load_csv_file(FRUIT_DATA_2022_PATH)
            user_fruit = input("What fruit would you like data for? (To see a list of all fruits type f) ").capitalize()

            if user_fruit == "F":
                display_all_items(data)
            else:
                for fruit in data:
                    if fruit[I_NAME] == user_fruit and fruit[I_FORM] == "Fresh":
                        return fruit

        # If the user wants veggies, load the vegetable CSV form and search for the vegetable requested
        elif type == "VEGETABLE" or type ==  "V":

            data = load_csv_file(VEGGIE_DATA_2022_PATH)
            user_veggie = input("What vegetable would you like data for? (To see a list of all vegetables press v) ").capitalize()

            if user_veggie == "V":
                    display_all_items(data)
            else:
                for veggie in data:
                    if veggie[I_NAME] == user_veggie and veggie[I_FORM] == "Fresh":
                        return veggie

        # Error Handling
        else:
            print("\nPlease enter an acceptable value\n")

def produce_ratio(item):
    """Determine how many lbs of an item are needed and how much it will cost"""

    # Ensure that the numbers we will be doing math with are parsed into a float
    cups_eq_size = float(item[I_CUP_EQUIVILENT_SIZE])
    retail_price = float(item[I_RETAIL_PRICE])

    # Gather input from user and math.ceil to round up to the nearest pound
    cups = float(input(f"How many cups of {item[I_NAME]} do you need? "))
    lbs_needed = math.ceil((cups * cups_eq_size) * 10) / 10
    total_price = round(lbs_needed * retail_price, 2)

    # Display results and cite sources
    print("\nAccording to ers.usda.gov as of 2022")
    print(f"For {cups} cups of {item[I_NAME]}")
    print(f"You will need to buy {lbs_needed} lbs of {item[I_FORM]} {item[I_NAME]}")
    print(f"At ${round(retail_price, 2)} {item[I_RETAIL_PRICE_UNIT]} this will cost you ${total_price}\n")

def display_all_items(items):
    """Display all the fruits or veggies in the list that are labled as 'Fresh' """
    for item in items:
        if item[I_FORM] == "Fresh":
            print(item[I_NAME])
    

if __name__ == "__main__":
    main()