def get_detections():
    detections = [("person", 0.92), ("car", 0.45), ("person", 0.78), ("bike", 0.31), ("car", 0.88)]
    return detections

def filter_detections(detections, threshold = 0.5):
    filtered_list = [i for i in detections if i[1] > threshold]
    return filtered_list

def display_detections(filtered_list):
    for detection in filtered_list:
        print(f'{detection[0]} : {detection[1]}')


detections = get_detections()
filtered_list = filter_detections(detections)
results = display_detections(filtered_list)


labels = [i[0] for i in filtered_list]
print(labels)

high_conf = [i[1] for i in filtered_list if i[1] > 0.7]
print(high_conf)



