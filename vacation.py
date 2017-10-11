def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    fares = {"Charlotte": 183,
             "Tampa": 220,
             "Pittsburgh": 222,
             "Los Angeles": 475}
    return fares[city]


def rental_car_cost(days):
    daily_cost = 40
    if days >= 7:
        return (days * daily_cost) - 50
    elif days >= 3:
        return (days * daily_cost) - 20
    else:
        return days * daily_cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money


print(trip_cost("Los Angeles", 5, 600))
