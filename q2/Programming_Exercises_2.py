#Exercise 1: My School Bag
school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"] #[] defines a list and stores it within the variable school_items. The "" encasing each item identifies it as a string or str
print("All Five Items:") #Displays what is inside the () accordingly
#Below uses print and school_items[] to directly grab a specific item from the defined list, this is also called indexing. Arrays always start their index counting from 0
print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])

print("\nFirst item:") #/n is used as an escape character, giving the dislay an empty space for a cleaner and more organized look
print(school_items[0]) #once again uses print and school_items to grab a specific item from the list, this being the first item, using index 0
print("\nLast item:")
print(school_items[4]) #once again uses print and school_items to grab a specific item from the list, this being the last item, using index 4




#Exercise 2: Travel Destination Manager
Destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]  #[] defines a list and stores it within the variable school_items. The "" encasing each item identifies it as a string or str

print("All Destinations:")  #Displays what is inside the () accordingly
for destination in Destinations: #uses a for loop to print each destination once
    print(destination)

print("\nSliced Destinations:") #\n adds an empty space for visual orginization
print(Destinations[1:4]) #Destinations[1:4] grabs the specific items from index 1 up to, but not including, index 4

search = input("\nSearch for a Destination: ")  #Asks the user to search for a destination of choice
if search in Destinations: #checks if the chosen destination is within the defined list
    print(f"{search} exists in the list.") #f directly embeds stated variables into texts using {}. States that the entered destination was found in the list
else:
    print(f"{search} does not exist in the list.") #the message displayed if destination chosen was not found in the list

Destinations[2] = "Iloilo" #after the code runs, replaces index 2, "Davao" with "Iloilo"
print("\nUpdated Destinations:") #Prints the updated list after the replacement
print(Destinations)


