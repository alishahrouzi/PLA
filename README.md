# Perceptron Learning Algorithm (PLA) Implementation

## Overview
This repository contains an implementation of the Perceptron Learning Algorithm (PLA) using Python and NumPy. The PLA is a fundamental algorithm in machine learning, used for binary classification problems.

## Features
- Matrix creation and initialization
- Training data input and processing
- Weight initialization
- Selection of activation functions:
  - Sign function (sgn)
  - Sigmoid function
  - Step function (stp)
- Iterative learning process with error correction
- Adjustable learning rate

## Requirements
This project requires:
- Python 3.x
- NumPy

Install dependencies using:
```bash
pip install numpy
```

## How It Works
1. **Initialize Matrices:** The program initializes matrices for input data, training data, and weights.
2. **User Input:** The user provides sample data, training labels, initial weights, and a learning rate.
3. **Computation:**
   - The dot product between input data and weights is computed.
   - An activation function is applied to determine the output.
   - The error between expected and actual output is calculated.
4. **Weight Adjustment:** If there is an error, the weights are updated using the learning rate and error values.
5. **Iteration:** The process repeats until the error is minimized or a predefined number of iterations is reached.

## Usage
To run the program, execute:
```bash
python pla.py
```
Then follow the prompts to input sample data, training labels, and parameters.

## Example
```bash
number of sample: 3
number of data: 2
Enter Number of Iterable: 10
please enter sample data:
Data (1,1) : 1
Data (1,2) : 2
...
please enter Learning Rate = 0.1
Choice Your Function: 1.sgn() 2.sigmoid() 3.stp()
1
...
final output = [1, -1, 1]
final error = [0, 0, 0]
```

## Future Improvements
- Support for multi-class classification
- Optimized matrix operations
- Visualization of decision boundaries

## License
This project is open-source and available under the MIT License.

