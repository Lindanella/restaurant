#CS175
#Linda Pimpinella
#restaurant
loop_1 = 'yes'
while loop_1 == 'yes':
    vegetarian = False
    vegan = False
    gluten_free = False
    vegetarian_input = input("Is anyone in your party a vegetarian: ")
    if vegetarian_input == 'yes' or vegetarian_input == 'Yes':
        vegetarian = True
    vegan_input = input("Is anyone in your party a vegan: ")
    if vegan_input == 'yes' or vegan_input =='Yes':
        vegan = True
    gluten_freeInput = input ("Is anyone in your party gluten free: ")
    if gluten_freeInput == 'yes' or gluten_freeInput =='Yes':
        gluten_free = True
    print ('''Here are all the possible places to eat
        Joes Gourmet Burgers
        Main Street Pizza Company
        Corner Cafe
        Mamas Fine Italian
        The Chefs Kitchen''')
    print ('Here is the list of locations you and your party can eat at:') 
    if not(vegetarian or vegan or gluten_free):
        print("Joes Gourmet Burgers")
    if not(vegan):
        print ("Main Street Pizza Company")
    if not(gluten_free or vegan):
        print ("Mamas Fine Italian")
    print ("Corner Cafe and The Chefs Kitchen")
    loop_1 =input('Would you like to run another resturant search yes or no: ')
    
    
