# renderers/latex_drawer.py
def render_latex(gates):
    lines = ["\\begin{quantikz}"]
    qubit_map = {}
    for g in gates:
        for q in g["qubits"]:
            qubit_map.setdefault(q, [])

    for i, gate in enumerate(gates):
        for q in qubit_map:
            if q in gate["qubits"]:
                qubit_map[q].append(f"\\gate{{{gate['name']}}}")
            else:
                qubit_map[q].append("\\qw")

    for q in sorted(qubit_map.keys()):
        lines.append(" & ".join(["\\lstick{q_" + str(q) + "}"] + qubit_map[q]) + " & \\qw \\\\")
    lines.append("\\end{quantikz}")
    return "\n".join(lines)
