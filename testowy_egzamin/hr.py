def calculate_velocity(distance, time):
    if not isinstance(distance, (int, float)) or not isinstance(time, (int,float)):
        return False
    else:
        return distance / time

calculate_velocity(54, 2)