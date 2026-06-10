def get_detections():
    detections = [("person", 0.92), ("car", 0.45), ("person", 0.78), ("bike", 0.31), ("car", 0.88)]
    return detections

def filter_detections(detections, threshold = 0.5):
    filtered_list = []
    for i in detections:
        if i[1] > threshold:
            filtered_list.append(i)
            
    return filtered_list

def display_detections(filtered_list):
    for detection in filtered_list:
        print(f'{detection[0]} : {detection[1]}')


detections = get_detections()
filtered_list = filter_detections(detections)
results = display_detections(filtered_list)


