# Import necessary modules from Amazon Braket SDK
from braket.circuits import Circuit          # Main class for creating quantum circuits
from braket.devices import LocalSimulator    # Local quantum simulator for testing
import numpy as np                          # NumPy for mathematical operations

def create_pure_state_circuit():
    """
    Function to create various pure quantum state examples.
    Pure states are quantum states that can be described by a single state vector.
    Returns a list of circuits demonstrating different pure states.
    """
    
    # Example 1: |0⟩ state (computational basis)
    circuit1 = Circuit()                    # Create empty quantum circuit
    # Qubit starts in |0⟩ by default       # No gates needed - qubits initialize to |0⟩ state
    
    # Example 2: |1⟩ state
    circuit2 = Circuit()                    # Create new empty circuit
    circuit2.x(0)                          # Apply Pauli-X gate to qubit 0
                                          # X gate flips |0⟩ to |1⟩ (quantum NOT gate)
    
    # Example 3: |+⟩ state = (|0⟩ + |1⟩)/√2
    circuit3 = Circuit()                    # Create new empty circuit
    circuit3.h(0)                          # Apply Hadamard gate to qubit 0
                                          # H gate creates equal superposition of |0⟩ and |1⟩
                                          # Transforms |0⟩ → (|0⟩ + |1⟩)/√2
    
    # Example 4: |-⟩ state = (|0⟩ - |1⟩)/√2
    circuit4 = Circuit()                    # Create new empty circuit
    circuit4.x(0).h(0)                     # Chain operations: first X gate, then H gate
                                          # X flips |0⟩ to |1⟩, then H creates (|0⟩ - |1⟩)/√2
                                          # This is the |-⟩ state (minus state)
    
    # Example 5: Custom pure state |ψ⟩ = α|0⟩ + β|1⟩
    # Let's create |ψ⟩ = (√3/2)|0⟩ + (1/2)|1⟩
    circuit5 = Circuit()                    # Create new empty circuit
    theta = 2 * np.arccos(np.sqrt(3)/2)    # Calculate rotation angle for RY gate
                                          # For state α|0⟩ + β|1⟩, use θ = 2*arccos(α)
                                          # Here α = √3/2, so θ = 2*arccos(√3/2)
    circuit5.ry(theta, 0)                  # Apply RY rotation gate with calculated angle
                                          # RY(θ) rotates qubit around Y-axis by angle θ
                                          # Creates desired amplitude distribution
    
    # Return list of all created circuits
    return [circuit1, circuit2, circuit3, circuit4, circuit5]

# Main execution section
circuits = create_pure_state_circuit()     # Call function to get list of circuits
device = LocalSimulator()                  # Initialize local quantum simulator
                                          # This runs on your computer, not cloud

# Define descriptive names for each quantum state
state_names = ["|0⟩", "|1⟩", "|+⟩", "|-⟩", "Custom |ψ⟩"]

# Loop through each circuit and run simulation
for i, circuit in enumerate(circuits):     # enumerate() gives both index and circuit
    print(f"\n{state_names[i]} State Circuit:")  # Print state name with formatting
    print(circuit)                         # Display circuit diagram/structure
    
    # Run simulation with measurements
    result = device.run(circuit, shots=1000).result()  # Execute circuit 1000 times
                                                       # shots = number of measurements
                                                       # .result() waits for completion
    
    counts = result.measurement_counts      # Extract measurement statistics
                                          # Dictionary with '0' and '1' as keys
                                          # Values are number of times each was measured
    
    print(f"Measurement results: {counts}") # Display measurement statistics
                                          # Shows how many times |0⟩ and |1⟩ were observed
