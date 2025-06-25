from braket.circuits import Circuit
from braket.devices import LocalSimulator
import numpy as np

# Create a quantum circuit with one qubit
circuit = Circuit()

# Initialize qubit in |0⟩ state (this is the default)
# Apply Hadamard gate to create superposition |+⟩ = (|0⟩ + |1⟩)/√2
circuit.h(0)

# Print the circuit
print("Quantum Circuit:")
print(circuit)

# Run on local simulator
device = LocalSimulator()
result = device.run(circuit, shots=1000).result()

# Get measurement counts
counts = result.measurement_counts
print(f"\nMeasurement results: {counts}")
