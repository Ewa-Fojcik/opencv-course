with open("race_results.txt", "w") as f:
    f.write("Michal,70.3\n") 
    f.write("Ewa,58.7\n")  
    f.write("Marc,82.3\n")
    f.write("Carlos,40.2\n")
    f.write("Kamil,60.2\n") 


time_list = []
fastest_name = None
fastest_time = None

def get_category(converted_time):
    if converted_time < 60:
        return("gold")
    elif converted_time < 75:
        return("silver")
    else:
        return("bronze")
            
with open("race_results.txt", "r") as f:
    for line in f:
        splitted = line.strip().split(",")
        converted_time = float(splitted[1])
        
        category = get_category(converted_time)
        print(f'{splitted[0]} - {splitted[1]} - {category}')   

        if fastest_time is None or converted_time < fastest_time:
            fastest_time = converted_time
            fastest_name = splitted[0]


print(f'{fastest_name} - {fastest_time}')







