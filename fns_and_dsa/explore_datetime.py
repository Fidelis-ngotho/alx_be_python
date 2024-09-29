from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate Future Date
def calculate_future_date():
    try:
        # Get user input for the number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=number_of_days)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid number of days.")

# Main script execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
