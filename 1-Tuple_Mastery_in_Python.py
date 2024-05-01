# Task 1: Tuple Mastery in Python

def createFlightItineraries(flights): # Function to create flight itineraries
    for i, flight in enumerate(flights): # Loop through inputted list
        name, departure, destination = flight # Unpacking tuple for better formatting
        print(f"Itinerary {i + 1}: {name} - From {departure} to {destination}.") # Print each itinerary

flight_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")] # Given flight list
createFlightItineraries(flight_list)