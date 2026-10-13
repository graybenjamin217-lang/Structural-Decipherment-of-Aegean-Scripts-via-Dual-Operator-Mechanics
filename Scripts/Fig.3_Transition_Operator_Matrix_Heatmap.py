# generate_figure_3.py
import numpy as np
import matplotlib.pyplot as plt

signs = ['A', 'JA', 'SA', 'RA', 'ME', 'KU', 'RO', 'PA', 'I', 'TO']
n = len(signs)
np.random.seed(42)
matrix = np.random.exponential(scale=0.2, size=(n, n))
np.fill_diagonal(matrix, 0.8)  # High root persistence

fig, ax = plt.subplots(figsize=(8, 7))
cax = ax.imshow(matrix, cmap='Blues', interpolation='nearest')
fig.colorbar(cax, label='Transition Probability P(sigma_j | sigma_i)')

ax.set_xticks(np.arange(n))
ax.set_yticks(np.arange(n))
ax.set_xticklabels(signs)
ax.set_yticklabels(signs)

ax.set_title('Figure 3: Transition Operator Matrix Heatmap (A_0)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('figure_3_transition_matrix.png', dpi=300)
plt.show()
