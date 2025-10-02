import math
import random
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] 
                                   for _ in range(input_size)] # Initialize weights randomly
        self.weights_hidden_output = [[random.uniform(-1, 1) for _ in range(output_size)] 
                                    for _ in range(hidden_size)]
        self.hidden_bias = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.output_bias = [random.uniform(-1, 1) for _ in range(output_size)]
    def forward(self, inputs):
        self.hidden = [] # Hidden layer
        for j in range(len(self.weights_input_hidden[0])):
            activation = sum(inputs[i] * self.weights_input_hidden[i][j] 
                           for i in range(len(inputs))) + self.hidden_bias[j]
            self.hidden.append(sigmoid(activation))
        outputs = [] # Output layer
        for j in range(len(self.weights_hidden_output[0])):
            activation = sum(self.hidden[i] * self.weights_hidden_output[i][j] 
                           for i in range(len(self.hidden))) + self.output_bias[j]
            outputs.append(sigmoid(activation))
        return outputs
    def train(self, training_data, epochs=1000, learning_rate=0.5):
        for epoch in range(epochs):
            for inputs, targets in training_data:
                outputs = self.forward(inputs)
                # Backpropagation (simplified)
                output_errors = [targets[i] - outputs[i] for i in range(len(outputs))]
                # Update weights (simplified gradient descent)
                for i in range(len(self.weights_hidden_output)):
                    for j in range(len(self.weights_hidden_output[0])):
                        self.weights_hidden_output[i][j] += learning_rate * output_errors[j] * self.hidden[i]
if __name__ == "__main__":
    training_data = [
        ([0, 0], [0]),
        ([0, 1], [1]),
        ([1, 0], [1]),
        ([1, 1], [0])
    ]
    nn = NeuralNetwork(2, 3, 1)
    nn.train(training_data, epochs=5000)
    print("Neural Network XOR Results:")
    for inputs, expected in training_data:
        output = nn.forward(inputs)
        print(f"Input: {inputs}, Expected: {expected[0]}, Got: {output[0]:.3f}")