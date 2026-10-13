# generate_figure_5.py
import matplotlib.pyplot as plt

eras = ['Cretan Hieroglyphic', 'Linear A', 'Phaistos Disc']
error_bounds = [0.00008, 0.00002, 0.00012]

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(eras, error_bounds, color=['coral', 'skyblue', 'mediumseagreen'], width=0.5)
ax.axhline(y=0.0001, color='red', linestyle='--', label='Error Bound Threshold (epsilon = 10^-4)')

ax.set_title('Figure 5: Spectral Footprint Convergence Across Script Eras', fontsize=12, fontweight='bold')
ax.set_ylabel('Eigenvalue Residual Error (epsilon)', fontsize=10)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figure_5_cross_era_convergence.png', dpi=300)
plt.show()
