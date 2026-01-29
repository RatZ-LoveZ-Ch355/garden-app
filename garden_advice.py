def get_gardening_advice(month):
    if month == "January":
        return "Prune your fruit trees."
    elif month == "June":
        return "Water your plants frequently in the heat."
    else:
        return "Just enjoy your garden!"


month_input = input("Enter a month: ")
print(get_gardening_advice(month_input))
