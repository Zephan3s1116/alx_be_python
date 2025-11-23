from datetime import datetime, timedelta

def display_current_datetime():
    """Gets and displays the current date and time in a specific format."""
    current_date = datetime.now()
   
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """Prompts for days to add and calculates the future date."""
    try:
        
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    time_difference = timedelta(days=days_to_add)

   
    future_date = current_date + time_difference

  
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    
    current = display_current_datetime()

    calculate_future_date(current)