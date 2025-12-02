import matplotlib.pyplot as plt
import numpy as np

def main():
    x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    y = [0.0000277090, 0.0000182500, 0.000075625060, 0.0004205000, 0.0175267500, 0.0271735000, 0.3024626250, 3.1560173340, 38.1675244590, 490.7836712500, 9600.4881065830]
    for i in range(len(y)):
        y[i] = y[i] / 60

    plt.scatter(x, y)
    plt.title("Exact Solution Timing")
    plt.xlabel("Locations (n)")
    plt.xticks(x)
    plt.ylabel("Time (minutes)")
    plt.show()

    return

if __name__ == "__main__":
    main()
