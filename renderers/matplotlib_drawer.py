# renderers/matplotlib_drawer.py
import matplotlib.pyplot as plt

def render_matplotlib(gates):
    max_qubit = max(q for g in gates for q in g["qubits"])
    depth = len(gates)

    fig, ax = plt.subplots(figsize=(depth + 2, max_qubit + 1))
    for i in range(max_qubit + 1):
        ax.hlines(i, 0, depth, color='black')
        ax.text(-0.5, i, f'q{i}', va='center')

    for i, gate in enumerate(gates):
        for q in gate["qubits"]:
            ax.add_patch(plt.Rectangle((i, q - 0.25), 0.8, 0.5, color='lightblue'))
            ax.text(i + 0.4, q, gate["name"].upper(), ha='center', va='center')
    ax.axis('off')
    plt.show()
