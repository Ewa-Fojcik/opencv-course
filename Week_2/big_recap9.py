class Report():
    def __init__(self, report_id, crime_type, location, severity):
        self.report_id = report_id
        self.crime_type = crime_type
        self.location = location
        self.severity = severity
    def __repr__(self):
        return(f"Report({self.report_id}, {self.crime_type}, {self.location}, {self.severity})")
    def is_urgent(self):
        if self.severity>=8:
            return True
    def display(self):
        urgency = self.is_urgent()
        print(f"[{self.report_id}] {self.crime_type} - {self.location} - {'URGENT' if urgency else 'routine'}")
    def set_severity(self, value):
        if value < 1 or value > 10:
            raise ValueError('Severity must be between 1 and 10')
        self.severity = value


reports=[
    Report(18,'burglary','Warsaw',5),
    Report(19,'murder','Rybnik',9),
    Report(20,'shoplifting','Katowice',10),
    Report(21,'vandalism','Sosnowiec',2),
    Report(22,'theft','Bielsko',6)
]

def save_reports(reports, filename):
    with open(filename, 'w') as f:
        for i in reports:
            f.write(f"{i.report_id},{i.crime_type},{i.location},{i.severity}\n")

def load_reports(filename):
    report_objects = []
    with open(filename, 'r') as f:
        for i in f:
            splitted = i.strip().split(",")
            report = Report(int(splitted[0]), splitted[1], splitted[2], int(splitted[3]))
            report_objects.append(report)
    return report_objects
            

save_reports(reports, 'reports.txt')
loaded = load_reports('reports.txt')
for i in loaded:
    if i.is_urgent():
        i.display()

try:
    reports[0].set_severity(15)
except ValueError as e:
    print(e)