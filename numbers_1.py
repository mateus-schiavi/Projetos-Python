import matplotlib.pyplot as plt

for i in range(10):
    plt.plot([0,1], [i,i], label=f"Série {i+1}")
plt.legend()
plt.show()
