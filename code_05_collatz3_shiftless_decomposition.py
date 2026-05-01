# -*- coding: utf-8 -*-
"""code_05_collatz3_shiftless_decomposition
"""

# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT
# Author: Hiroshi Harada
# Date: May 2, 2026


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches


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


def generate_shiftless_decomposition_3adic(seed, max_steps=500):
    """
    Simulate the 3-adic Shiftless Collatz trajectory and decompose it into:

        A_k = 4^k * n_0  (Pure geometric expansion)
        B_k = n_k - A_k  (Cumulative effect of c * 3^v injections)

    The output matrix encodes structural overlap:
        0 = background
        1 = A_k only (seed contribution)
        2 = |B_k| only (injection contribution)
        3 = interference (A_k and |B_k| both non-zero)
    """

    n = seed
    history_n = [n]

    # --- Generate Shiftless trajectory ---
    while not is_power_of_3(n) and len(history_n) <= max_steps:

        # Extract NZT
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
        weight = 3 ** v

        n = 4 * n + c * weight
        history_n.append(n)

    steps = len(history_n)

    # Max width based on largest A_k
    max_ak = (4 ** (steps - 1)) * seed
    max_trits = len(to_ternary(max_ak)) + 2
    matrix = np.zeros((steps, max_trits))

    # --- Decompose each step ---
    for k in range(steps):

        ak = (4 ** k) * seed
        bk = history_n[k] - ak

        a_ter = to_ternary(ak)[::-1]
        b_ter = to_ternary(abs(bk))[::-1]  # abs: spatial structure only

        for j in range(max_trits):
            trit_a = int(a_ter[j]) if j < len(a_ter) else 0
            trit_b = int(b_ter[j]) if j < len(b_ter) else 0

            if trit_a > 0 and trit_b == 0:
                matrix[k, j] = 1
            elif trit_a == 0 and trit_b > 0:
                matrix[k, j] = 2
            elif trit_a > 0 and trit_b > 0:
                matrix[k, j] = 3

    return matrix


def save_figure5_png(seed=28, png_path="figure5.png"):
    """Generate and save the Figure 5 PNG."""
    mat = generate_shiftless_decomposition_3adic(seed)

    cmap = ListedColormap([
        "#000000",  # background
        "#00BFFF",  # A_k only
        "#FFD700",  # B_k only
        "#FF00FF"   # interference
    ])

    fig, ax = plt.subplots(figsize=(12, 14), facecolor="#000000")
    ax.set_facecolor("#000000")

    ax.imshow(mat, cmap=cmap, aspect="auto", interpolation="nearest", vmin=0, vmax=3)
    ax.invert_xaxis()

    ax.set_title(
        f"3-adic Shiftless Decomposition (Seed: {seed})",
        color="white", fontsize=20, pad=20, fontweight="bold"
    )
    ax.set_xlabel("Trit Position (MSB ← LSB)", color="#aaaaaa", fontsize=12)
    ax.set_ylabel("Evolution Steps (Time Flow)", color="#aaaaaa", fontsize=12)
    ax.tick_params(colors="#666666", labelsize=10)

    legend_items = [
        ("Background", "#000000"),
        ("Seed Contribution (A_k = 4^k n0)", "#00BFFF"),
        ("Injection Contribution (|B_k|)", "#FFD700"),
        ("Interference (A_k ∩ B_k)", "#FF00FF")
    ]
    patches = [mpatches.Patch(color=c, label=l) for l, c in legend_items]

    leg = plt.legend(
        handles=patches,
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        facecolor="#0a0a0a",
        edgecolor="#333333",
        labelcolor="white",
        fontsize=11
    )
    leg.get_frame().set_linewidth(0.5)

    plt.tight_layout()
    plt.savefig(png_path, dpi=200)
    plt.close()

    print(f"PNG saved to: {png_path}")


if __name__ == "__main__":
    save_figure5_png(seed=28)

