# Task 1: Stock Market Data Analysis

stock_data = [ # Given data
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

def findAverageStockPrice(company): # Function to find companies average stock price from provided data
    count = 0
    total_price = 0.0

    for data_point in stock_data: # Loop through each data point
        if (data_point[0] == company): # Check if data point matches inputted company
            count += 1
            total_price += data_point[2]

    if (count == 0): # If no match was found to the inputted company
        return "No such company in the provided data"
    else:
        return total_price / count # Average

# Testing
print(findAverageStockPrice("AAPL")) # 131.0
print(findAverageStockPrice("MSFT")) # 220.0
print(findAverageStockPrice("AAAA")) # No such company
