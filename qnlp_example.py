from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

def quantum_nlp_circuit(input_text):
    # Initialize a quantum circuit with enough qubits for the input length
    n_qubits = len(input_text) * 8  # Each character is represented by 8 qubits (ASCII encoding)
    circuit = QuantumCircuit(n_qubits, n_qubits)

    # Encode each character into quantum states
    for i, char in enumerate(input_text):
        # ASCII encoding of the character
        ascii_value = ord(char)
        
        # Binary representation of the ASCII value
        binary_representation = format(ascii_value, '08b')
        
        # Apply X-gate to qubits in the |1⟩ state in the binary representation
        for j, bit in enumerate(binary_representation):
            if bit == '1':
                circuit.x(i * 8 + j)
    
    # Apply Hadamard gate to all qubits
    circuit.h(range(n_qubits))

    # Apply CNOT gates between neighboring qubits
    for i in range(n_qubits - 1):
        circuit.cx(i, i + 1)

    return circuit

# Example usage
input_text = "Hello, Quantum World!"
qc = quantum_nlp_circuit(input_text)

# Visualize the circuit
qc.draw(output='mpl', fold=-1)

