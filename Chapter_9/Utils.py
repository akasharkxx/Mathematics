def map_value(value, current_min, current_max, new_min, new_max):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)
