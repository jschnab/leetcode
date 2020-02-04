# leetcode 1333
# filter and sort restaurants by vegan-friendly, price and distance

# given a List[List[int]] of restaurants where a restaurant is described
# as [id, ranking, vegan_friendly, price, distance], filter the restaurants
# by vegan_friendly, price and distance and sort by decreasing ranking and
# decreasing id to distinguish ties


def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance):
    restaurants.sort(key=lambda r: (-r[1], -r[0]))
    return [
        i for i, r, v, p, d in restaurants
        if v >= vegan_friendly and p <= max_price and d <= max_distance
    ]

def filter_restaurants2(restaurants, vegan_friendly, max_price, max_distance):
    """
    Step 1: filter restaurants by vegan-friendliness, price and distance
    Step 2: sort restaurants by decreasing ranking
    Step 3: discriminate ties in ranking based on id

    This function does not sort in place, it returns filtered and sorted
    restaurants.
    """
    filtered = [
        r for r in restaurants
        if r[3] >= vegan_friendly
        and r[4] <= max_price
        and r[5] <=max_distance
    ]

    # sort restaurants by ranking, here we use insertion sort
    for i in range(1, len(filtered)):
        current = filtered[i]
        while i > 0 and filtered[i-1][1] < current[1]:
            filtered[i] = filtered[i-1]
            i -= 1
        filtered[i] = current

    # discriminate ranking ties by id
    for i in range(1, len(filtered)):
        current = filtered[i]

        while i > 0 and
        filtered[i-1][1] == current[1] and
        filtered[i-1][0] < current[0]:
            filtered[i] = filtered[i-1]
            i -= 1
        filtered[i] = current

    return filtered

