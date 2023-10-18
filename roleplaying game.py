print("YOU HAVE 30 POINTS TO SPEND ON: \n ***STRENGTH*** \n ***HEALTH*** \n ***WISDOM*** \n ***DEXTERITY***")
print("Each attribute cost 5 POINTS for one tier")

points = 30

# 2d array of users attributes (includes names of attributes in [0] and how many of that attribute they have in [1])
user_attributes = [["strength", "health", "wisdom", "dexterity"], [0, 0 , 0, 0]]

# loop to bring the user back to the menu when they finished an activity 
menu = True
while menu:
    question = input("\nEnter X to buy an attribute, Y to sell an attribute or Z to see your attributes: ")
    question.lower()

    if question == "x":
        print("You currently have", points, "points")

        #allows user select an attribute to buy, if it is not a valid attribute, they can try again
        is_attribute = False
        while is_attribute == False:
            buy_attribute = input("Enter the attribute you want to buy: ")
            buy_attribute.lower()
            if points >= 5:
                if buy_attribute in user_attributes[0]:
                    
                    #incriments the user attribute 2d array by one according to the position of the attribute in the array
                    attribute_index = user_attributes[0].index(buy_attribute)
                    new_element = user_attributes[1][attribute_index] + 1
                    user_attributes[1][attribute_index] = new_element
                    is_attribute = True
                    
                    points = points - 5
                    print("You have", points, "points")
                
                else:
                    print("That is not a valid attribute, try again")
            
            else:
                print("You do not have enough points to buy an attribute")
                is_attribute = True
        

        input("Press enter to go back to the menu")
                 
    # allows user select an attribute to sell if they have it in the attribute list
    elif question == "y":
        sell_attribute = input("Enter the attribute you want to sell: ")
        if sell_attribute in user_attributes[0]:
            points = points + 5
            index = user_attributes[0].index(sell_attribute)
            user_attributes[1][index] = user_attributes[1][index] - 1
            
            print("You now have", points, "points")
        
        else:
            print("You do not have that attribute")
            
        input("Press enter to go back to the menu")

    # shows the user the list of their attributes
    elif question == "z":
        length = len(user_attributes[0])
        for x in range(length):
            print(user_attributes[0][x], ":", user_attributes[1][x])
            
        