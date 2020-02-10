# leetcode problem 1344
# given a time in hours (1 to 12) and minutes, determine the smallest angle
# between the clock hands

def clock_angle(hours, minutes):
    minutes_angle = 360 / 60 * minutes
    hours_angle = 360 / 12 * (hours + minutes / 60)
    angle = abs(hours_angle - minutes_angle)
    answer = min(angle, 360 - angle)
    return answer
