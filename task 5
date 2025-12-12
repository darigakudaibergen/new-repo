def season_events(number_of_month):
    if not isinstance(number_of_month, int):
        print("You need to enter the real number of the month")
        return

    if number_of_month < 1 or number_of_month > 12:
        print("You need to enter the real number of the month")
        return

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    month_name = months[number_of_month - 1]

    if number_of_month in (12, 1, 2):
        event = "White snow fell outside the window"
    elif number_of_month in (3, 4, 5):
        event = "Birds sang beautiful songs"
    elif number_of_month in (6, 7, 8):
        event = "The sun shone brighter than ever"
    else:
        event = "The harvest was incredible"

    print(f"You were born in {month_name}. {event}.")
# Example usage:
season_events(3)
