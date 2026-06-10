import matplotlib.pyplot as plt

X1 = -5
X2 = 5
Z = range(10, 1001)
f = 1

X_length = abs(X1)+abs(X2)
lengths = []

for z in Z:
    x_length = X_length/z
    lengths.append(x_length)

plt.plot(Z, lengths)
plt.xlabel("f length = 1")
plt.ylabel("x lenght")
plt.title("Projection Simulation")
plt.show()