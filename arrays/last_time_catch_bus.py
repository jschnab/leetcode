"""
leetcode 2332: the last time to catch a bus

We are given an integer array 'buses' of length n, where buses[i] is the
departure time of the ith bus. We are also given an integer array 'passengers'
of length m, where passengers[j] is the time at which the jth passenger arrives
at the bus station. All bus departures and passenger arrival times are unique.

We are also given an integer 'capacity' that represents the maximum number of
passengers that can get on each bus.

Wehn a passenger arrives, they will wait in line for the next available bus. We
can get on a bus that departs at x minutes we arrive at y minutes where y <= x,
and if the bus is not full. Passengers with the earliest arrival times get on
the bus first.

More formally when a bus leaves, either:
- if capacity of fewer passengers are waiting for a bus, they will all get on
  the bus, or
- the capacity passengers with the earliest arrival times will get on the bus

Return the latest time you may arrive at the bus station to catch a bus. You
cannot arrive at the same time as another passenger.
"""


def catch_bus(buses, passengers, capacity):
    """
    Find the latest time at which we can arrive to catch the bus.

    :param list(int) buses: Buses departure times.
    :param list(int) passengers: Passengers arrival times (at the station).
    :param int capacity: Bus capacity.
    :returns (int): Latest time we should arrive to catch the bus.
    """
    buses.sort()
    passengers.sort()
    i = j = start = 0

    # fill all buses but the last one with passengers
    while (i < len(buses) - 1 and j < len(passengers)):
        # fill one bus with passengers...
        if passengers[j] <= buses[i] and j - start < capacity:
            j += 1
        # ...then go to the next bus
        else:
            i += 1
            start = j

    # fill the last bus and keep track of how much space is left in the bus
    while j < len(passengers) and passengers[j] <= buses[-1] and capacity != 0:
        j += 1
        capacity -= 1

    # if the bus is not full, we may arrive just before the bus leaves
    if capacity != 0:
        latest = buses[-1]
    # otherwise we have to arrive earlier than the last passenger that caught
    # the last bus
    else:
        latest = passengers[j - 1]

    # we cannot arrive at the same time as another passenger, so we need to
    # find a "slot"
    j -= 1
    while j >= 0 and latest == passengers[j]:
        latest = passengers[j] - 1
        j -= 1

    return latest


def test1():
    assert catch_bus([10, 20], [2, 17, 18, 19], 2) == 16
    print("test 1 successful")


def test2():
    assert catch_bus([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2) == 20
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
