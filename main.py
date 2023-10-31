import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data)

plt.scatter(data.studytime, data.score)

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score

        m_gradient += -(2 / n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2 / n) * (y - (m_now * x + b_now))
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    print(m_gradient)
    print(m)

    return m, b


m = 0
b = 0
L = 0.0001
epochs = 100

for i in range(epochs):
    m, b = gradient_descent(m, b, data, L)

print(m, b)

plt.scatter(data.studytime, data.score, color="black")
plt.plot(list(range(0, 60)), [m * x + b for x in range(0, 60)], color="red")
plt.show()
