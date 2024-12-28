def place_order(customer_name, food_items, special_requests ="No"):
    # display the order summary
    print("\nOrder summary : ")
    print(f"Customer name : {customer_name}")
    print("Food items Ordered : ")
    for i in food_items:
        print(i)
    print(f"Special Requests: {special_requests}")




if __name__ == "__main__":
    # user input for customer name
    name = input("Enter your name : ").strip() #strip() function is used to remove leading and trailing whitespace (spaces, tabs, or newline characters) from a string
    order_items=[]

    # user input for food items to be ordered
    print("\nEnter the food items you want to order. Type 'done' when finished : ")
    while True:
        item = input().strip()
        if item.lower() == "done": # lower() function is used to transform string to lower case
            break
        if item:
            order_items.append(item)

    # user input for any special requests
    special_requests = input("\nAny special requests? If none, press Enter :  ").strip()
    if not special_requests:
        special_requests="No"
    place_order(name, order_items,special_requests)

