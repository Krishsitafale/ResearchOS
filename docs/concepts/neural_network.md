# Neural Networks

## Overview

A Neural Network is a computational model inspired by the human brain. It consists of interconnected artificial neurons that learn complex patterns from data by adjusting their weights and biases during training.

Neural Networks are the foundation of modern Artificial Intelligence and power technologies such as:

* ChatGPT
* BERT
* GPT
* Gemini
* Claude
* Image Recognition
* Speech Recognition
* Autonomous Vehicles
* Recommendation Systems

Every modern Large Language Model (LLM) is ultimately a very large neural network.

---

# Why Do We Need Neural Networks?

Previously, we learned Linear Regression.

The model was:

[
y = wx + b
]

This model works well when the relationship between input and output is approximately linear.

However, real-world problems are rarely linear.

Examples:

* Recognizing handwritten digits
* Detecting cancer in X-rays
* Translating languages
* Understanding scientific papers
* Generating code
* Answering questions

These tasks require models capable of learning highly complex relationships.

Neural Networks were developed to solve these problems.

---

# Limitations of Linear Models

A linear model can only represent straight-line relationships.

Example:

```text
Input

↓

Linear Model

↓

Output
```

Even if multiple linear layers are stacked together, the result remains another linear function.

Therefore, stacking only linear transformations does not increase the expressive power of the model.

To model complex data, we need **non-linearity**.

---

# Artificial Neuron

The basic building block of a Neural Network is an **Artificial Neuron**.

A neuron receives inputs, performs a weighted sum, adds a bias, applies an activation function, and produces an output.

The mathematical model is:

[
z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
]

Where:

* (x_i) → Input feature
* (w_i) → Weight
* (b) → Bias
* (z) → Weighted sum

The output is then computed as:

[
a = f(z)
]

where:

* (f) = Activation Function
* (a) = Neuron output

---

# Components of a Neuron

## Inputs

The information provided to the neuron.

Example:

```text
Hours Studied

Attendance

Previous Marks
```

---

## Weights

Weights determine the importance of each input.

Larger weights have greater influence on the output.

Weights are learned automatically during training using Gradient Descent.

---

## Bias

Bias shifts the output of the neuron.

Without a bias, the neuron has limited flexibility and cannot represent many useful functions.

---

## Weighted Sum

The neuron combines all inputs into a single value.

[
z = \sum_{i=1}^{n} w_i x_i + b
]

This value is called the **pre-activation value**.

---

## Activation Function

The activation function introduces non-linearity.

Without activation functions, a Neural Network would behave like a single linear model regardless of its depth.

---

# Activation Functions

## Sigmoid

Formula:

[
\sigma(x)=\frac{1}{1+e^{-x}}
]

Output Range:

```
0 to 1
```

Applications:

* Binary classification
* Probability estimation

Limitations:

* Vanishing Gradient
* Slow convergence

---

## Tanh

Formula:

[
\tanh(x)
]

Output Range:

```
-1 to 1
```

Advantages:

* Zero-centered outputs

Limitations:

* Still suffers from Vanishing Gradient

---

## ReLU (Rectified Linear Unit)

Formula:

[
ReLU(x)=\max(0,x)
]

Properties:

If

[
x<0
]

Output:

```
0
```

If

[
x>0
]

Output:

```
x
```

Advantages:

* Computationally efficient
* Fast training
* Sparse activations
* Most widely used activation function in modern Deep Learning

---

# Neural Network Architecture

A Neural Network consists of multiple layers.

```text
Input Layer

↓

Hidden Layer

↓

Hidden Layer

↓

Output Layer
```

Each layer contains multiple neurons.

The output of one layer becomes the input of the next layer.

---

# Hidden Layers

Hidden layers learn intermediate representations of the input data.

Example:

Image Classification

Layer 1:

Edges

↓

Layer 2:

Corners

↓

Layer 3:

Shapes

↓

Layer 4:

Objects

↓

Output:

Cat

Similarly, Language Models learn increasingly abstract representations:

Characters

↓

Words

↓

Grammar

↓

Context

↓

Meaning

---

# Training a Neural Network

Training follows the same cycle introduced during Gradient Descent.

```text
Initialize Parameters

↓

Forward Pass

↓

Prediction

↓

Compute Loss

↓

Backpropagation

↓

Gradient Descent

↓

Update Weights

↓

Repeat
```

This process continues until the model converges.

---

# Forward Pass

The Forward Pass computes the prediction.

Flow:

Input

↓

Weighted Sum

↓

Activation

↓

Output

No learning occurs during the forward pass.

---

# Backpropagation

Backpropagation computes how much each weight contributed to the error.

It calculates gradients for every weight in the network.

Gradient Descent then updates those weights.

Backpropagation answers:

> Which weights should change?

Gradient Descent answers:

> How should they change?

---

# Why Neural Networks Work

Neural Networks work because they learn hierarchical representations.

Early layers detect simple patterns.

Later layers combine those simple patterns into increasingly abstract concepts.

This ability allows Neural Networks to solve problems that are impossible for linear models.

---

# Advantages

* Learns complex nonlinear relationships
* Automatic feature extraction
* Highly scalable
* Excellent performance on large datasets
* Foundation of Deep Learning

---

# Limitations

* Requires significant training data
* Computationally expensive
* Sensitive to hyperparameters
* Can overfit small datasets
* Often difficult to interpret

---

# Real-World Applications

Neural Networks power:

* Image Classification
* Speech Recognition
* Machine Translation
* Recommendation Systems
* Medical Diagnosis
* Autonomous Driving
* Fraud Detection
* Robotics
* Natural Language Processing
* Large Language Models

---

# Neural Networks in ResearchOS

Neural Networks are the core AI engine behind ResearchOS.

Examples include:

### Sentence Embedding Model

Converts text into numerical vectors.

### Reranking Model

Ranks retrieved research papers.

### Classification Model

Categorizes documents by topic.

### Summarization Model

Generates concise summaries.

### LLM

Reads retrieved research papers and generates answers.

Without Neural Networks, ResearchOS would be unable to understand or reason about language.

---

# Interview Questions

## Beginner

1. What is an Artificial Neuron?
2. Why do Neural Networks need activation functions?
3. What are weights and biases?
4. What is the difference between a neuron and a Neural Network?
5. What is a Hidden Layer?

---

## Intermediate

6. Why can't stacked linear layers solve complex problems?
7. Why is ReLU preferred over Sigmoid in hidden layers?
8. What is the Forward Pass?
9. What is Backpropagation?
10. How does Gradient Descent train a Neural Network?

---

## Advanced

11. Why do deep networks learn hierarchical features?
12. What causes the Vanishing Gradient problem?
13. Why are Transformers considered Neural Networks?
14. What role do feed-forward layers play inside Transformer blocks?
15. How do Neural Networks learn sentence embeddings?

---

# Key Takeaways

* A Neural Network is a collection of interconnected artificial neurons.
* Each neuron performs a weighted sum followed by an activation function.
* Activation functions introduce non-linearity.
* Neural Networks learn by adjusting weights and biases using Gradient Descent.
* Backpropagation computes gradients.
* Gradient Descent updates parameters.
* Modern AI systems, including Large Language Models, are extremely large Neural Networks.

---

# Connection to the Next Module

A single neuron is useful, but modern AI systems contain **millions or billions of neurons**.

The next module introduces **Backpropagation**, the algorithm that efficiently computes gradients for every weight in a Neural Network.

Backpropagation is the key algorithm that makes training deep neural networks computationally feasible.
