# generate_figure_4.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

ax.text(0.5, 0.85, 'Word Token: JA-SA-SA-RA-ME-TE', fontsize=12, fontweight='bold', ha='center', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black'))

ax.annotate('', xy=(0.2, 0.6), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(0.8, 0.6), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle='->', lw=1.5))

ax.text(0.2, 0.52, 'Prefix (Phase-Gate)\n[JA-] (x* = 0.5)', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='black'))
ax.text(0.5, 0.52, 'Invariant Root (Attractor)\n[SA-SA-RA-ME] (x* = 1.0)', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', edgecolor='black'))
ax.text(0.8, 0.52, 'Suffix (Phase-Gate)\n[-TE] (x* = 0.5)', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='black'))

ax.set_title('Figure 4: Agglutinative Root-Affix Decomposition Architecture', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('figure_4_decomposition_tree.png', dpi=300)
plt.show()
