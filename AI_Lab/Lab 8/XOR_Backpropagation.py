# ============================================================
# Backpropagation for XOR Gate
# Program by: Samip Khadka
# Roll No: 36
# ============================================================
import numpy as np

print("="*50)
print("  Backpropagation for XOR Gate")
print("  Program by: Samip Khadka")
print("  Roll No: 36")
print("="*50)

# 1. Activation Function (Sigmoid) and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 2. Dataset for XOR Gate
# Input datasets
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Output datasets
y = np.array([[0], [1], [1], [0]])

# 3. Hyperparameters
epochs = 10000
lr = 0.1  # Learning rate
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# 4. Weight and Bias Initialization
# Randomly initialize weights and biases
np.random.seed(42)  # For reproducible results
wh = np.random.uniform(size=(input_neurons, hidden_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))
wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# 5. Training Loop using Backpropagation
for epoch in range(epochs):
    # --- Forward Pass ---
    hidden_layer_input = np.dot(X, wh) + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_activations, wout) + bout
    predicted_output = sigmoid(output_layer_input)

    # --- Backward Pass (Backpropagation) ---
    # Compute error at output layer
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    # Compute error at hidden layer
    error_hidden_layer = d_predicted_output.dot(wout.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activations)

    # --- Updating Weights and Biases ---
    wout += hidden_layer_activations.T.dot(d_predicted_output) * lr
    bout += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hidden_layer) * lr
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

# 6. Test the Trained Network
print("Final Predicted Output after Training:")
for i in range(len(X)):
    print(f"Input: {X[i]} -> Predicted: {predicted_output[i][0]:.4f} (Target: {y[i][0]})")
