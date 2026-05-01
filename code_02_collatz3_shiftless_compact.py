# -*- coding: utf-8 -*-
"""code_02_collatz3_shiftless_compact
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


def generate_compact_3adic(seed, max_steps=200):
    """
    Generate a compact visualization matrix for the 3-adic Shiftless Collatz trajectory.

    The trajectory consists of:
        1. Ascending phase:
            n -> 4n + c * 3^v
            Repeated until n reaches a power of 3 (the Jackpot).
        2. Finale phase (visualization only):
            n -> n // 3
            Repeated until n = 1.

    Each step is recorded as a ternary string, aligned so that the LSB is on the right.
    Trit encoding:
        0 = padding (background)
        1 = trit '0'
        2 = trit '1'
        3 = trit '2'
    """

    n = seed
    history = [to_ternary(n)]

    # --- Step 1: Ascending (Shiftless) ---
    while True:

        # Stop before executing next jump
        if is_power_of_3(n) or len(history) > max_steps:
            break

        # Find lowest non-zero trit (NZT)
        temp = n
        v = 0
        while temp % 3 == 0:
            v += 1
            temp //= 3

        # NZT = 0 → Jackpot → stop ascending
        if temp == 1:
            break

        t = temp % 3
        c = -1 if t == 1 else 1
        weight = 3 ** v

        n = 4 * n + c * weight
        history.append(to_ternary(n))

    # --- Step 2: Finale (n // 3) ---
    # This phase is NOT part of the Shiftless model.
    # It is only for compact visualization of the 3-adic descent.
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


def save_figure2_png(seed=28, png_path="figure2.png"):
    """Generate and save the Figure 2 PNG."""
    mat = generate_compact_3adic(seed)

    fig, ax = plt.subplots(figsize=(6, 8))
    fig.patch.set_facecolor('#0a0a0a')
    ax.set_facecolor('#0a0a0a')

    # Ternary Cyberpunk color scheme:
    cmap = ListedColormap(['#0a0a0a', '#333333', '#00ffcc', '#ff00ff'])

    ax.imshow(mat, cmap=cmap, aspect='auto', interpolation='nearest', vmin=0, vmax=3)
    ax.invert_xaxis()  # LSB on the right

    ax.set_title(f"Compact 3-adic Shiftless Collatz: Seed {seed}",
                 color='white', fontsize=14, fontweight='bold')
    ax.set_ylabel("Steps (Ascend → Finale)", color='white')
    ax.set_xlabel("Trit Position (0 is LSB on the Right)", color='white')

    ax.tick_params(colors='gray')
    for spine in ax.spines.values():
        spine.set_color('#222222')

    plt.tight_layout()
    plt.savefig(png_path, dpi=200)
    plt.close()

    print(f"PNG saved to: {png_path}")


if __name__ == "__main__":
    save_figure2_png(seed=28)

