# generate_figure_2.py
import numpy as np
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19]
y_vals = np.ones_like(primes, dtype=float)

fig, ax = plt.subplots(figsize=(10, 4))
ax.stem(primes, y_vals, linefmt='b-', markerfmt='bo', basefmt='r-')
ax.set_title('Figure 2: Prime-Indexed Dual-Dilation Grid (D_k Channels)', fontsize=12, fontweight='bold')
ax.set_xlabel('Prime Index (p_k)', fontsize=10)
ax.set_ylabel('Quantized Resonance State', fontsize=10)
ax.set_ylim(0, 1.5)
ax.set_yticks([])

for p in primes:
    ax.text(p, 1.05, f'p={p}', ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('figure_2_prime_dilation_grid.png', dpi=300)
plt.show()
