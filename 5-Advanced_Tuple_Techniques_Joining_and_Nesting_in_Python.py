# Task 1: Product Catalog Merging

def joinCatalogs(*catalogs): # Function to join together 2 or more catalogs
    new_catalog =  ()
    for catalog in catalogs: # Loop through all provided catalogs
        new_catalog = new_catalog + catalog # Use '+' operator to combine each catalog provided
    return new_catalog # return new combined catalog

def displayCatalog(catalog): # Function to display each product in a catalog
    for product in catalog: # Loop through each product in the provided catalog
        name, price = product # Unpack tuple for easier formatting
        print(f"{name}: ${price}") # Print product name followed by price

#Testing
catalog1 = (("Laptop", 1000), ("Camera", 500)) # Given catalog
catalog2 = (("Smartphone", 800), ("Tablet", 450)) # Given catalog

big_catalog = joinCatalogs(catalog1, catalog2) # Join together catalog1 and catalog2
displayCatalog(big_catalog) # Display the new combined catalog