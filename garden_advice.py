<<<<<<< HEAD
def get_gardening_advice(month):
    if month == "January":
        return "Prune your fruit trees."
    elif month == "June":
        return "Water your plants frequently in the heat."
    else:
        return "Just enjoy your garden!"


month_input = input("Enter a month: ")
print(get_gardening_advice(month_input))
=======
def get_gardening_advice(month):
    """
    Provides seasonal gardening advice based on the input month.
    Uses a dictionary for efficient lookup.
    """
    # Dictionary mapping months to specific tasks
    advice_map = {
        "January": "Prune your fruit trees and plan your spring garden.",
        "February": "Start seeds indoors for tomatoes and peppers.",
        "March": "Prepare the soil and plant cool-weather crops like lettuce.",
        "April": "Plant your summer flowers and monitor for pests.",
        "May": "Mulch your beds to retain moisture for the coming heat.",
        "June": "Water your plants frequently and harvest early vegetables.",
        "July": "Stay on top of weeding and harvest summer fruits.",
        "August": "Collect seeds for next year and start fall plantings.",
        "September": "Plant spring-flowering bulbs like tulips and daffodils.",
        "October": "Harvest remaining crops and clear out dead plants.",
        "November": "Protect sensitive plants from frost and clean your tools.",
        "December": "Order seed catalogs and enjoy your winter rest.",
    }

    # Use .get() to provide a default message if the month isn't found
    return advice_map.get(month, "Just enjoy your garden and watch the seasons change!")


def main():
    """Main function to handle user input and display advice."""
    print("--- Professional Garden Advice App ---")
    user_month = input("Enter a month (e.g., January): ").capitalize().strip()

    advice = get_gardening_advice(user_month)
    print(f"\nAdvice for {user_month}: {advice}")


if __name__ == "__main__":
    main()
>>>>>>> b14fa26 (Complete refactor with dictionary and docs)
