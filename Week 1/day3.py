racer = {
    'name': 'Ewa',
    'bib' : 25,
    'time' : 37.65,
    'finished' : True
}

print(racer['name'])
print(racer['time'])

racer['country'] = 'Poland'

if racer['time'] < 80:
    print('podium'),
elif racer['time'] < 95:
    print('solid run'),
else:
    print('needs improvement')

for x, y in racer.items():
    print(x, y)