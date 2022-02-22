import time
import numpy as np
import matplotlib.pyplot as plt

# Solving via recursion
price = [1, 5, 8, 9, 10, 17, 17, 20]
length = [1, 2, 3, 4, 5, 6, 7, 8]


def recurse_cut(n):
    if n == 0:
        return 0
    fin = -99999
    for i in range(1, min(n, len(price))):
        fin = max(fin, price[i] + recurse_cut(n - length[i]))
    return fin


def dynamic_cut(n):
    DP = []
    BT = []
    DP.append(0)
    BT.append(0)

    for j in range(n):
        vals = []
        for i in range(min(len(price), len(DP))):
            vals.append(price[i] + DP[(len(DP) - 1) - i])
        DP.append(max(vals))
        BT.append(vals.index(max(vals)) + 1)
    return DP[len(DP) - 1]


if __name__ == '__main__':
    nums = [5, 10, 16]
    recurse_times = []
    dp_times = []
    for num in nums:
        start = time.time()
        print("Recurse cut result: ", recurse_cut(num))  # Fix this function
        end = time.time()
        final = end - start
        recurse_times.append(final)
        print("Runtime of the program is: ", final)

        start = time.time()
        print("DP cut result: ", dynamic_cut(num))
        end = time.time()
        final = end - start
        dp_times.append(final)
        print("Runtime of the program is: ", final)

    # Graphing
    br1 = np.arange(len(recurse_times))
    br2 = [x + 0.25 for x in br1]

    plt.bar(br1, recurse_times, color="red", width=0.25, label="Recursive")
    plt.bar(br2, dp_times, color="blue", width=0.25, label="Dynamic")
    plt.xlabel("Values of n")
    plt.ylabel("Times")
    plt.title("Comparing runtimes of recursive and DP solutions.")
    plt.xticks([r + 0.125 for r in range(len(recurse_times))], nums)
    ax = plt.gca()
    ax.set_ylim([0, 0.0001])

    plt.legend()
    plt.show()
