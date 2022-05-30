"""This is a shoe stock management system"""

class Shoes():

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        #return readbale string in a table format
        return "{:<15} {:<15} {:<20} {:<15} {:<15}".format(self.country, self.code, self.product, self.cost, self.quantity)


shoe_object_list = []


#adding shoes data to list as objects
def read_shoes_data():

    """
    This function will open the file
    inventory.txt and read the data from this file the create shoes
    object and append this object into the shoes list. one line in
    this file represents data to create one object of shoes. 

    """
    
    try:
        with open ('inventory.txt', 'r') as inventory_textfile:
            
            for row in inventory_textfile:
                row = row.replace('\n', '')
                row = row.split(',')

                #create a shoe object which will be appendend to the list
                shoe = Shoes(row[0], row[1], row[2], row[3], row[4]) 
                shoe_object_list.append(shoe)
                
    except FileNotFoundError:
        print("File not found")


    
def capture_shoes():
    """
    this function will allow a user to capture
    data about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.

    """

    code_found = 1
    
    #read data from textfile to list   
    if len(shoe_object_list) == 0:
        read_shoes_data()
        
    #ask for user inputs to append to list
    country = input("Please enter country: ")
    
    code = input("Please enter code in format as follows 'SKU12345': ")
    
    #check if code doesn't already exist
    while code_found == 1:
        for row in shoe_object_list:
            if code == row.code:
                code = input("SKU already exists! Please enter code in format as follows 'SKU12345': ")
                code_found = 1
                break
            else:
                code_found = 0

    
    product = input("Please enter product name: ")
    
    while True:
        try:
            cost = int(input("Please enter product cost to the nearest whole number: "))
            break
        except ValueError:
            print("Oops! Invalid number, please try again.")
            
    while True:
        try:
            quantity = int(input("Please enter quantity: "))
            break
        except ValueError:
            print("Oops! Invalid number, please try again.")
        
    #create shoe object and append to list
    shoe = Shoes(country, code, product, cost, quantity)
    shoe_object_list.append(shoe)
    
    try:
        with open ('inventory.txt', 'w') as inventory_textfile:
            for row in shoe_object_list:
                inventory_textfile.write(str(row.country) + "," + str(row.code) + "," + str(row.product) + "," + str(row.cost) + "," + str(row.quantity) + "\n")
            print("New shoe data added!" + "\n")
    except FileNotFoundError:
            print("File not found")



def view_all():
    """"
    This function will iterate over all the shoes list and
    print the details of the shoes 

    """

    #read data from textfile to list
    #shoe_object_list = []
    if len(shoe_object_list) == 0:
        read_shoes_data()
    
    #loop through list of objects and use str funtion to convert objects to readable data an print int a table format
    for row in shoe_object_list:
        shoe = Shoes(row.country, row.code, row.product, row.cost, row.quantity)
        print(shoe.__str__())
        
    print("\n")

    

def re_stock():
    """
    This function will find the shoe object with the
    lowest quantity, which is the shoes that need to be
    restocked. Ask the user if he wants to add the quantity of
    these shoes and then update it. This quantity is
    updated on the file.

    """

    if len(shoe_object_list) == 0:    
        read_shoes_data()
    
    min_num = int(shoe_object_list[1].quantity)
    index = 1
    
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue
        
        value.quantity = int(value.quantity)
        #checking which number is smaller and assigning that number to min variable
        if value.quantity < min_num:
            min_num = value.quantity
            index = row

    print(f"The show with the lowest stock is {shoe_object_list[index].product} Quantity: {shoe_object_list[index].quantity}")
    update_quantity = input("Would you like to update the shoes quantity 'yes' or 'no'? ").lower()

    #if yes is selected allow user to enter number to replinish with and add this number to list and write to textfile
    #if no quantity remains unchanged
    if update_quantity == "yes":
        while True:
            try:
                new_quantity = int(input("What additional quantities would you like to add: "))
                break
            except ValueError:
                print("Oops! Invalid number, please try again.")
            
        new_total = shoe_object_list[index].quantity + new_quantity
        shoe_object_list[index].quantity = new_total
        
        try:
            with open ('inventory.txt', 'w') as inventory_textfile:
                for row in shoe_object_list:
                    inventory_textfile.write(str(row.country) + "," + str(row.code) + "," + str(row.product) + "," + str(row.cost) + "," + str(row.quantity) + "\n")
                    
                print("Quantity updated" + "\n")
                
        except FileNotFoundError:
                print("File not found")
                
        
        
    elif update_quantity == "no":
        print("Quantity unchanged" + "\n")
        
    else:
        print("Incorrect input" + "\n")

    
    
def search_shoe():
    """
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be
    printed

    """
    shoe_not_found = 0
    
    if len(shoe_object_list) == 0:
        read_shoes_data()
        
    shoe_search = input("Enter SKU you are searching for e.g.'SKU12345': ")
    
    for row in shoe_object_list:
        if shoe_search == row.code:
            return row.code
            break
        else:
            #if shoe is not found set variable to 1
            shoe_not_found = 1
            
    if shoe_not_found == 1:
        return "Shoe SKU not found!"
    
    print("\n")
  

 
def value_per_item():
    """
    this function will calculate the total value
    for each item . (value = cost * quantity). Information printed on the
    console for all the shoes.

    """
    
    if len(shoe_object_list) == 0:
        read_shoes_data()

    #printing inital headings
    print("{:<15} {:<20} {:<15}".format("Code", "Product","Value"))
    
    for row, value in enumerate(shoe_object_list):

        #don't check the first column with titles
        if row == 0:
            continue

        value.quantity = int(value.quantity)
        value.cost = int(value.cost)

        #print values in table format
        print("{:<15} {:<20} R{:<15}".format(value.code, value.product, value.quantity*value.cost))

    print("\n")



def highest_qty():
    """
    Product with the highest quantity is set on sale.
    """
    #read data from textfile to list
    if len(shoe_object_list) == 0:
        read_shoes_data()    
    
    max_num = int(shoe_object_list[1].quantity)
    index = 1
    
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue
        
        value.quantity = int(value.quantity)
        #checking which number is smaller and assigning that number to min variable
        if value.quantity > max_num:
            max_num = value.quantity
            index = row
    
    print(f"{shoe_object_list[index].code}({shoe_object_list[index].product}) is on SALE!!!" + "\n")



def main():
    
    """
    Now in your main create a menu that executes each function
    above. This menu should be inside the while loop. Be creative.
    """
    while True:
        #presenting the menu to the user and 
        #making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
        a - Add new shoe to database
        v - View all shoes on database
        r - Restock shoe with lowest quantity
        s - Search for a shoe using SKU code
        val - Stock on database value
        h - Shoe to sale
        e - Exit
        : ''').lower()

        #add new shoe to database
        if menu == "a":
            capture_shoes()
        #view all shoes
        elif menu == "v":
            view_all()
        #restock shoe with lowest quantity
        elif menu == "r":
            re_stock()
        #search for a shoe
        elif menu == "s":
            print(f"Shoe: {search_shoe()}" + "\n")
        #get value of stock on hand
        elif menu == "val":
            value_per_item()
        #put a shoe on sale with highest quantity
        elif menu == "h":
            highest_qty()
        #exit
        elif menu == "e":
            print("Goodbye!")
            exit()
        else:
            print("You have made a wrong choice, Please Try again!")



        
if __name__=="__main__":
    main()
