# -*- coding: utf-8 -*-
"""code_03_collatz3_shiftless_full
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


def generate_full_3adic(seed, max_steps=200):
    """
    Generate a full visualization matrix for the 3-adic Shiftless Collatz trajectory,
    explicitly separating the internal two-phase structure:

        1. Reach phase: n -> 4n
        2. Fill phase: 4n -> 4n + c * 3^v

    The output matrix uses:
        0 = padding (background)
        1 = trit '0'
        2 = trit '1'
        3 = trit '2'
    """

    n = seed
    history = [to_ternary(n)]

    # --- Step 1: Ascending (Reach + Fill) ---
    while True:

        # Stop BEFORE Reach phase
        if is_power_of_3(n) or len(history) > max_steps:
            break

        # Find lowest non-zero trit (NZT)
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

        # --- Reach phase ---
        n_quad = 4 * n
        history.append(to_ternary(n_quad))

        # --- Fill phase ---
        n = n_quad + c * weight
        history.append(to_ternary(n))

    # --- Step 2: Finale (visualization only) ---
    while n > 1:
        n //= 3
        history.append(to_ternary(n))

    # --- Convert history to matrix ---
    max_len = max(len(trits) for trits in history)
    matrix = np.zeros((len(history), max_len))

    for i, trits in enumerate(history):
        trits_rev = trits[::-1]  # LSB on the right
        for j, char in enumerate(trits_rev):
            if char == '0':
                matrix[i, j] = 1
            elif char == '1':
                matrix[i, j] = 2
            elif char == '2':
                matrix[i, j] = 3

    return matrix


def save_figure3_png(seed=28, png_path="figure3.png"):
    """Generate and save the Figure 3 PNG."""
    mat = generate_full_3adic(seed)

    fig, ax = plt.subplots(figsize=(6, 10))
    fig.patch.set_facecolor('#0a0a0a')
    ax.set_facecolor('#0a0a0a')

    cmap = ListedColormap(['#0a0a0a', '#333333', '#00ffcc', '#ff00ff'])

    ax.imshow(mat, cmap=cmap, aspect='auto', interpolation='nearest', vmin=0, vmax=3)
    ax.invert_xaxis()

    ax.set_title(f"3-adic Shiftless (Reach 4n → Fill c·3^v): Seed {seed}",
                 color='white', fontsize=12, fontweight='bold')
    ax.set_ylabel("Sub-steps (Time Flow Downward)", color='#dddddd')
    ax.set_xlabel("Trit Position (0 is LSB on the Right)", color='#dddddd')

    ax.tick_params(colors='gray')
    for spine in ax.spines.values():
        spine.set_color('#222222')

    plt.tight_layout()
    plt.savefig(png_path, dpi=200)
    plt.close()

    print(f"PNG saved to: {png_path}")


if __name__ == "__main__":
    save_figure3_png(seed=28)

