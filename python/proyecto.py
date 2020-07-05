import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

# FITNESS FUNCTION
# f(x,y) = x^2+y^y

axis_limits = (-100, 100)
max_velocity = 10
iterations = 0

def set_betters():
    global betters
    betters = np.array([values[0][i]**2+values[1][i]**2 for i in range(values.shape[1])])

def get_values():
    return np.random.randint(-100,100, size=(2,100))


def evaluate():
    new_values = get_values()

    index = 0
    for i in range(new_values.shape[1]):
        if (new_values[0][i]**2+new_values[1][i]**2) < betters[index]:
            values[0][i], values[1][i] = new_values[0][i], new_values[1][i]
        index += 1
    
    set_betters()
    better_index = np.argmin(betters)
    
    
def animate(i):
    evaluate()
    global iterations

    plt.clf()
    plt.title(f"Sample Graph iteration: {iterations}")
    plt.xlim(axis_limits)
    plt.ylim(axis_limits)
    plt.scatter(values[0], values[1], 20, "k")
    iterations += 1

def main():
    #DEFINITION OF THE INITIAL RANDOM VALUES AND THE INITIAL BETTER SET
    global values
    values = get_values()
    set_betters()
    velocities = np.random.randint(1,max_velocity, size=(100,1))

    # CREATION AND STYLING OF THE CHART
    plt.scatter(values[0], values[1], 20, "k")
    plt.title("Initial Sample Graph")
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.xlim(axis_limits)
    plt.ylim(axis_limits)

    # SETING  THE FUNCANIMATION FUNTCION
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()

if __name__ == "__main__":
    main()