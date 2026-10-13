# generate_figure_1.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.05, 2.0, 400)
with np.errstate(divide='ignore', invalid='ignore'):
    fx = x ** (-(1.0 - 1.0 / x))

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, fx, label='f(x) = x^-(1 - 1/x)', color='navy', lw=2)
ax.plot(x, x, linestyle='--', color='gray', label='Identity Line (f(x) = x)')

# Mark fixed points
ax.scatter([1.0], [1.0], color='red', s=100, zorder=5, label='Identity Attractor (x* = 1)')
ax.scatter([0.5], [0.5], color='darkorange', s=100, zorder=5, label='Phase-Gate Repeller (x* = 0.5)')

ax.set_title('Figure 1: Phase Portrait of Operator Attractor Dynamics', fontsize=12, fontweight='bold')
ax.set_xlabel('State Space x', fontsize=10)
ax.set_ylabel('Transition Mapping f(x)', fontsize=10)
ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figure_1_phase_portrait.png', dpi=300)
plt.show()
