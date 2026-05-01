# -*- coding: utf-8 -*-
"""code_04_collatz3_shiftless_comparison
"""

# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT
# Author: Hiroshi Harada
# Date: May 2, 2026


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def to_ternary(n):
    """Convert an integer to a ternary (base 3) string."""
    if n == 0:
        return '0'
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res


def is_power_of_3(n):
    """Check if n is a perfect power of 3 (the 3-adic Jackpot)."""
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def get_shiftless_steps_3adic(seed, max_limit=500):
    """
    Compute the number of steps required for the 3-adic Shiftless trajectory
    (n -> 4n + c * 3^v) to reach a power of three.
    """
    n = seed
    steps = 0

    if is_power_of_3(n):
        return steps

    while steps < max_limit:
        temp = n
        v = 0
        while temp % 3 == 0:
            v += 1
            temp //= 3

        # NZT = 0 → Jackpot
        if temp == 1:
            break

        t = temp % 3
        c = -1 if t == 1 else 1
        n = 4 * n + c * (3 ** v)
        steps += 1

        if is_power_of_3(n):
            break

    return steps


def generate_matrix_synced_3adic(seed, mode, total_steps):
    """
    Generate a ternary matrix representing the evolution of:
        - '4n'         : pure geometric expansion
        - '4n+1'       : fixed scalar addition
        - '4n+c*3^v'   : 3-adic Shiftless Collatz
    """
    n = seed
    history = [to_ternary(n)]

    for _ in range(total_steps):

        if mode == "4n":
            n = 4 * n

        elif mode == "4n+1":
            n = 4 * n + 1

        elif mode == "4n+c*3^v":
            temp = n
            v = 0
            while temp % 3 == 0:
                v += 1
                temp //= 3

            # NZT = 0 → Jackpot → stop
            if temp == 1:
                break

            t = temp % 3
            c = -1 if t == 1 else 1
            n = 4 * n + c * (3 ** v)

        history.append(to_ternary(n))

    # Convert history to matrix
    max_len = max(len(trits) for trits in history)
    matrix = np.zeros((len(history), max_len))

    for i, trits in enumerate(history):
        trits_rev = trits[::-1]
        for j, char in enumerate(trits_rev):
            if char == '0':
                matrix[i, j] = 1
            elif char == '1':
                matrix[i, j] = 2
            elif char == '2':
                matrix[i, j] = 3

    return matrix


def save_figure4_png(seed=28, png_path="figure4.png"):
    """Generate and save the Figure 4 PNG."""
    max_steps = get_shiftless_steps_3adic(seed)

    mat_4n = generate_matrix_synced_3adic(seed, "4n", max_steps)
    mat_4n1 = generate_matrix_synced_3adic(seed, "4n+1", max_steps)
    mat_shiftless = generate_matrix_synced_3adic(seed, "4n+c*3^v", max_steps)

    fig, axes = plt.subplots(1, 3, figsize=(16, 8), facecolor="#0a0a0a")

    cmap = ListedColormap(["#0a0a0a", "#333333", "#00ffcc", "#ff00ff"])
    titles = [
        "Pure Expansion: 4n",
        "Fixed Addition: 4n + 1",
        "3-adic Shiftless: 4n + c·3^v"
    ]
    matrices = [mat_4n, mat_4n1, mat_shiftless]

    for ax, matrix, title in zip(axes, matrices, titles):
        ax.set_facecolor("#0a0a0a")
        ax.imshow(matrix, cmap=cmap, aspect="auto", interpolation="nearest", vmin=0, vmax=3)
        ax.invert_xaxis()

        ax.set_title(title, color="white", fontsize=14, pad=15)
        ax.set_xlabel("Trit Position (0 is LSB on Right)", color="#dddddd")
        ax.tick_params(colors="gray")

        for spine in ax.spines.values():
            spine.set_color("#222222")

    axes[0].set_ylabel(
        f"Steps (Synchronized to {max_steps} jumps)",
        color="white"
    )

    fig.suptitle(
        f"Ternary Dynamics Comparison (Time-Synced): Seed {seed}",
        color="white",
        fontsize=20,
        fontweight="bold"
    )

    plt.tight_layout()
    plt.savefig(png_path, dpi=200)
    plt.close()

    print(f"PNG saved to: {png_path}")


if __name__ == "__main__":
    save_figure4_png(seed=28)

