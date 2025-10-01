from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

#print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences= []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference)
    # Add the customer preference to the list

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags=set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    new_product= {
        "name": product["name"],
        "tags":set(product["tags"])
    }
    converted_products.append(new_product)
    


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags)

    
    
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    reccomendations=[]
    for product in products:
        number = count_matches(product["tags"],customer_tags)
        reccomendations.append({
            "name": product["name"],
            "match  found": number
        }) 
    reccomendations.sort(key=lambda x: x["match  found"], reverse=True)
    return reccomendations
        
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    



# TODO: Step 7 - Call your function and print the results

results =recommend_products(converted_products, customer_tags)

print("reccomended Products:")
for result in results:
    if result["match  found"] > 0:
        print(f"{'-'}{result['name']}: ({result['match  found']} match(es))")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
#1. the core opereations that I used were loops and intersections. I used loops to iterate through the products, for example when i wanted to change the list to a set, i need it to iterate so i can change it to a set, and intersections to find common tags between products and customer preferences.
#2 If i had 1000+ producsts i would problably need to use a database to store the products or implement data structure so i can iplement queries and make it more efficient. it is important to know that this code is useful with a small number of products but as the number of products increases the time it takes to run the code will also increase.
