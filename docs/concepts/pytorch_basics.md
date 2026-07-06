# PyTorch Basics

## Overview

PyTorch is an open-source deep learning framework developed by Meta AI. It provides an intuitive Python interface for building, training, and deploying machine learning and deep learning models.

PyTorch combines:

* Tensor computation
* Automatic differentiation (Autograd)
* Neural network modules
* Optimization algorithms
* GPU acceleration

It is the most widely used framework in AI research and is heavily used in industry for training and fine-tuning modern AI models.

---

# Why PyTorch?

Before learning PyTorch, we manually implemented:

* Linear Regression
* Mean Squared Error (MSE)
* Numerical Gradient
* Gradient Descent

Although this helped us understand the mathematics, manually computing gradients becomes impossible for large models.

For example:

| Model                | Approximate Parameters |
| -------------------- | ---------------------: |
| Linear Regression    |                      2 |
| Small Neural Network |              Thousands |
| BERT Base            |            110 Million |
| GPT-style Models     |               Billions |

Manually updating billions of parameters is impractical.

PyTorch automates this process.

---

# Where PyTorch Fits in AI

```text
Dataset
    │
    ▼
PyTorch
    │
    ▼
Neural Network
    │
    ▼
Training
    │
    ▼
Saved Model
```

PyTorch provides the tools to build and train neural networks.

---

# Tensors

A Tensor is the fundamental data structure in PyTorch.

Think of tensors as multidimensional arrays with additional capabilities such as:

* GPU execution
* Automatic differentiation
* Efficient numerical computation

Examples:

### Scalar (0D)

```python
torch.tensor(5)
```

### Vector (1D)

```python
torch.tensor([1,2,3])
```

### Matrix (2D)

```python
torch.tensor([
    [1,2],
    [3,4]
])
```

### Higher-Dimensional Tensor

Used for:

* Images
* Videos
* Audio
* Embeddings

---

# Tensor Shapes

Every tensor has a shape.

Example:

```python
x = torch.tensor([
    [1,2],
    [3,4]
])

print(x.shape)
```

Output:

```python
torch.Size([2,2])
```

Understanding tensor shapes is essential when building deep learning models.

---

# Tensor Operations

Common tensor operations include:

```python
a + b
```

Addition

```python
a * b
```

Element-wise multiplication

```python
torch.matmul(a,b)
```

Matrix multiplication

```python
torch.dot(a,b)
```

Dot product

These operations are highly optimized and can run efficiently on GPUs.

---

# Automatic Differentiation (Autograd)

One of PyTorch's most powerful features is **Autograd**.

Autograd automatically computes gradients required for optimization.

Example:

```python
x = torch.tensor(2.0, requires_grad=True)

y = x**2

y.backward()

print(x.grad)
```

Output:

```python
tensor(4.)
```

Explanation:

[
y=x^2
]

Derivative:

[
\frac{dy}{dx}=2x
]

At

[
x=2
]

Gradient = 4

PyTorch computed this automatically.

---

# Computation Graph

Whenever a tensor has:

```python
requires_grad=True
```

PyTorch records every mathematical operation performed on it.

Example:

```text
x
│
▼
Square
│
▼
Multiply
│
▼
Loss
```

This structure is called the **Computation Graph**.

During:

```python
loss.backward()
```

PyTorch traverses the graph backward to compute gradients for every parameter.

---

# Neural Network Layers

Instead of manually writing:

[
y = wx+b
]

PyTorch provides:

```python
torch.nn.Linear()
```

Example:

```python
layer = torch.nn.Linear(2,1)
```

Meaning:

* 2 input features
* 1 output neuron

PyTorch automatically initializes the weights and bias.

---

# Activation Functions

PyTorch includes common activation functions.

Examples:

### ReLU

```python
torch.nn.ReLU()
```

### Sigmoid

```python
torch.nn.Sigmoid()
```

### Tanh

```python
torch.nn.Tanh()
```

These introduce non-linearity into neural networks.

---

# Loss Functions

A loss function measures prediction error.

Common PyTorch loss functions include:

### Mean Squared Error

```python
torch.nn.MSELoss()
```

Used for regression.

### Cross Entropy Loss

```python
torch.nn.CrossEntropyLoss()
```

Used for classification.

The objective during training is to minimize the loss.

---

# Optimizers

An optimizer updates model parameters using gradients.

Common optimizers:

### SGD

```python
torch.optim.SGD()
```

Implements Stochastic Gradient Descent.

### Adam

```python
torch.optim.Adam()
```

Adaptive optimizer that is widely used for modern deep learning models.

---

# Training Loop

The typical PyTorch training loop is:

```python
for epoch in range(epochs):

    prediction = model(X)

    loss = criterion(prediction, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

This consists of five steps:

1. Forward Pass
2. Compute Loss
3. Clear Previous Gradients
4. Backpropagation
5. Update Parameters

This workflow is common to almost all deep learning models.

---

# GPU Acceleration

PyTorch allows computations to run on GPUs.

Example:

```python
device = torch.device("cuda")

model.to(device)

data.to(device)
```

GPU execution significantly reduces training time for large models.

---

# Advantages of PyTorch

* Easy to learn
* Pythonic syntax
* Dynamic computation graph
* Excellent debugging support
* Strong research ecosystem
* Large community
* Native GPU support
* Hugging Face compatibility

---

# Limitations

* Large models require significant GPU memory
* Training can be computationally expensive
* Performance depends on hardware
* Requires understanding of tensor shapes

---

# Real-World Applications

PyTorch is used for:

* Computer Vision
* Natural Language Processing
* Robotics
* Autonomous Vehicles
* Medical Imaging
* Recommendation Systems
* Large Language Models
* Reinforcement Learning

---

# PyTorch in ResearchOS

PyTorch forms the AI foundation of ResearchOS.

It will be used for:

### Sentence Embedding Models

Converting document chunks into embeddings.

### Transformer Models

Understanding research papers.

### Reranking Models

Improving document retrieval quality.

### Future Fine-Tuning

Adapting pretrained models to domain-specific research collections.

---

# Best Practices

* Always check tensor shapes.
* Use `requires_grad=True` only when gradients are needed.
* Call `optimizer.zero_grad()` before `loss.backward()`.
* Switch to `model.eval()` during inference.
* Use GPUs when available for training.

---

# Interview Questions

## Beginner

1. What is PyTorch?
2. What is a tensor?
3. What is the difference between a NumPy array and a PyTorch tensor?
4. What is `requires_grad`?
5. What does `loss.backward()` do?

---

## Intermediate

6. What is a computation graph?
7. Why do we call `optimizer.zero_grad()`?
8. What is the role of an optimizer?
9. Why are tensors preferred over Python lists?
10. Why is GPU acceleration important?

---

## Advanced

11. Explain Automatic Differentiation.
12. Compare SGD and Adam.
13. What happens internally during `loss.backward()`?
14. Why does PyTorch use dynamic computation graphs?
15. How does PyTorch support Transformer training?

---

# Key Takeaways

* PyTorch is a deep learning framework, not an AI model.
* Tensors are the primary data structure.
* Autograd automatically computes gradients.
* Neural network layers are provided through `torch.nn`.
* Optimizers update model parameters using gradients.
* The training loop follows a consistent pattern: Forward Pass → Loss → Backpropagation → Parameter Update.
* PyTorch is the foundation of most modern deep learning systems.

---

# Connection to the Next Module

PyTorch gives us the tools to build neural networks efficiently.

The next step is understanding **why Transformer architectures outperform traditional neural networks for language tasks**.

Once we understand Transformers, we'll study **Sentence Transformers**, which generate the embeddings that power semantic search in ResearchOS.
