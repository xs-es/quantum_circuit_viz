# parsers/qiskit_adapter.py
def parse_qiskit_circuit(circuit):
    parsed = []
    for instr, qargs, _ in circuit.data:
        parsed.append({
            "name": instr.name,
            "qubits": [q.index for q in qargs],
            "params": instr.params
        })
    return parsed
