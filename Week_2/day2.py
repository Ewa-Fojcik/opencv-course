class Detection:
    def __init__(self, label, confidence):
        self.label = label
        self.confidence = confidence

    def __repr__(self):
        return f"Detection({self.label}, {self.confidence})"

class TrackedDetection(Detection):
    def __init__(self, label, confidence, track_id):
        super().__init__(label, confidence)
        self.track_id = track_id

    def __repr__(self):
        return f"TrackedDetection({self.label}, {self.confidence}, id={self.track_id})"
    

d1 = Detection("person1", 23)
d2 = Detection("person2", 64)
d3 = TrackedDetection("person3", 49, 13)
d4 = TrackedDetection("person4", 92, 14)    

print(d1,d2,d3,d4)




            
        