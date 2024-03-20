import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def speedtest():
    np_array1 = np.array(np.random.default_rng().standard_normal(10**6))
    np_array2 = np.array(np.random.default_rng().standard_normal(10**6))
    array1 = list(np.random.default_rng().standard_normal(10**6))
    array2 = list(np.random.default_rng().standard_normal(10**6))

    start_time = perf_counter()
    np.multiply(np_array1, np_array2)
    time1 = perf_counter() - start_time

    start_time = perf_counter()
    np.multiply(array1, array2)
    time2 = perf_counter() - start_time

    if time1 < time2:
        print(
            f"The multiplication time of NumPy arrays is {time1};"
            f"\nThe multiplication time of python arrays is {time2}, "
            f"that is {round(time2/time1)} time longer!"
        )
    else:
        print("No.")


def histogram():
    data = np.genfromtxt(
        "Lab-7\data2.csv", delimiter=",", missing_values="", filling_values=0.0
    )
    arr = data[:, 1]
    mean = round(np.mean(arr, axis=0), 2)
    std = round(np.nanstd(arr), 2)
    cols = int(np.round(len(arr) ** 0.5))

    plt.figure(figsize=(10, 7))
    plt.hist(
        arr,
        bins=cols,
        color="lightgreen",
        edgecolor="black",
        label="Number of measurements in the interval",
    )

    plt.fill(
        [mean - std, mean - std, mean + std, mean + std],
        [470, 0, 0, 470],
        color="lightblue",
        alpha=0.5,
        label="Confidence interval = Average±STD",
    )

    plt.axvline(mean, ls="dashed", color="r", label="Average value=" + str(mean))

    plt.xlabel("Interval")
    plt.ylabel("Measurments")
    plt.legend()
    plt.show()


def plot3d():
    np.random.seed(100)
    xs = np.linspace(0, -10, 10)
    ys = xs * np.cos(xs)
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, marker="o", c="red")
    plt.xlim = (-3 * np.pi, 3 * np.pi)
    plt.show()


if __name__ == "__main__":
    speedtest() #1
    histogram() #2
    plot3d()    #3
