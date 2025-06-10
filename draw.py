from .parsers.qiskit_adapter import parse_qiskit_circuit
from .parsers.braket_adapter import parse_braket_circuit
from .renderers.matplotlib_drawer import render_matplotlib
from .renderers.latex_drawer import render_latex

def draw_circuit(circuit, backend="auto", renderer="mpl"):
    if backend == "auto":
        if "qiskit" in str(type(circuit)).lower():
            backend = "qiskit"
        elif "braket" in str(type(circuit)).lower():
            backend = "braket"
        else:
            raise ValueError("Unsupported circuit type")

    if backend == "qiskit":
        gates = parse_qiskit_circuit(circuit)
    elif backend == "braket":
        gates = parse_braket_circuit(circuit)
    else:
        raise ValueError("Unknown backend")

    if renderer == "mpl":
        return render_matplotlib(gates)
    elif renderer == "latex":
        return render_latex(gates)
    else:
        raise ValueError("Unsupported renderer")
