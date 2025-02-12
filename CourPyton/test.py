EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_time):
    time = EXPECTED_BAKE_TIME - elapsed_time
    return time 
bake_time_remaining(30)

def preparation_time_in_minutes(number_of_layers):
    prepa = number_of_layers * 2
    return prepa
preparation_time_in_minutes(2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    preparation_time = number_of_layers * 2
    total_time = preparation_time + elapsed_bake_time
    return total_time

elapsed_time_in_minutes(3, 20)