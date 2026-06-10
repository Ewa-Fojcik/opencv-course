def get_racer():
    name = input(f'whats your name? ')
    finish_time = float(input(f'whats your time? '))
    return name, finish_time

def get_category(time):
    if time < 60:
        return "gold" 
    elif time <75:
        return "silver" 
    else:
        return "bronze" 
    
def display_result(name, time, category):
    print(f'{name} - {time} - {category}')


name, finish_time = get_racer()
time = get_category(finish_time)
results = display_result(name, finish_time, time)