with open("detections.txt", "w") as f:
    f.write("person,0.92\n")
    f.write("car,0.45\n")
    f.write("person,0.78\n")
    f.write("bike,0.31\n")
    f.write("car,0.88")


with open("detections.txt", "r" ) as f:
    for line in f:
        splitted = (line.strip().split(","))
        converted = float(splitted[1])
        if converted > 0.5:
            print(f"{splitted[0]} : {converted}")
        