with open("training_log.txt", "w") as f:
    f.write("2024-01-15,skiing,120\n")
    f.write("2024-01-16,gym,45\n")
    f.write("2024-01-17,skiing,90\n")
    f.write("2024-01-18,rest,0\n")
    f.write("2024-01-19,gym,60")


added = 0  
with open("training_log.txt", "r") as f:
    for line in f:
        splitted = line.strip().split(",")
        duration_minutes = float(splitted[2])
        if duration_minutes > 0:
            print(f'{splitted[0]} - {splitted[1]} - {splitted[2]}')      
        added += duration_minutes

print(added)        