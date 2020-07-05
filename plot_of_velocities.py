import numpy as np
import matplotlib.pylab as plt

# FORMULAS
# cos(teta) = adjacent/hypotenuse
# sin(teta) = opposite/hypotenuse
# np.sin(np.deg2rad(90))

def main():
    v_magnitude = 5
    v_direction = 45

    plt.scatter(2,2, 20, "k")
    vx = np.cos(np.deg2rad(v_direction)) * v_magnitude
    vy = np.sin(np.deg2rad(v_direction)) * v_magnitude
    plt.plot([2,vx], [2, 2], "b")
    plt.plot([vx,vx], [2, vy], "b")
    # print(vx, vy)
    plt.arrow(2, 2, vx/2, vy/2, fc="k", ec="k", head_width=0.2, head_length=0.2, )

    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()