# Gradient Descent

## Overview

Gradient Descent is one of the most fundamental optimization algorithms in Machine Learning and Deep Learning. It is used to minimize the loss (error) of a model by iteratively updating its parameters in the direction that most rapidly decreases the loss.

Almost every modern AI model—including Neural Networks, Convolutional Neural Networks (CNNs), Transformers, BERT, GPT, and diffusion models—uses Gradient Descent or one of its variants during training.

---

# Why Do We Need Gradient Descent?

Suppose we have a simple linear regression model:

[
y = wx + b
]

where:

* **x** → Input feature
* **y** → Predicted output
* **w** → Weight (parameter)
* **b** → Bias (parameter)

Initially, the values of **w** and **b** are random.

As a result, the predictions are poor.

Our objective is to automatically find better values of **w** and **b** so that the prediction error becomes as small as possible.

This optimization process is exactly what Gradient Descent performs.

---

# The Core Idea

Imagine standing somewhere on a mountain covered with dense fog.

Your goal is to reach the lowest point of the valley.

You cannot see the entire mountain.

Instead, you only know the slope where you are currently standing.

The strategy is simple:

1. Check the slope.
2. Walk downhill.
3. Repeat until the ground becomes flat.

Gradient Descent follows exactly the same idea.

Instead of walking on a mountain, it moves through the **loss landscape**.

---

# The Machine Learning Learning Cycle

```text
Initialize Parameters
        │
        ▼
Make Predictions
        │
        ▼
Compute Loss
        │
        ▼
Compute Gradient
        │
        ▼
Update Parameters
        │
        ▼
Repeat Until Convergence
```

This loop is repeated thousands or even millions of times during training.

---

# Loss Function

A loss function measures how far the model's predictions are from the actual values.

For Linear Regression, we commonly use the Mean Squared Error (MSE):

[
L=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
]

Where:

* (y_i) = Actual value
* (\hat y_i) = Predicted value
* (n) = Number of training samples

Our objective is to minimize this loss.

---

# What is a Gradient?

A gradient tells us how much the loss changes when a parameter changes slightly.

Think of it as the slope of the loss function.

* Positive gradient → Move left (decrease the parameter).
* Negative gradient → Move right (increase the parameter).
* Zero gradient → We are at or very near a stationary point (often a minimum).

The gradient tells us **which direction** reduces the loss.

---

# Gradient Descent Update Rule

The parameter update rule is:

[
w_{\text{new}}
==============

## w_{\text{old}}

\eta
\frac{\partial L}{\partial w}
]

Where:

* (w) = Current weight
* (\eta) = Learning rate
* (\frac{\partial L}{\partial w}) = Gradient of the loss with respect to the weight

Interpretation:

* Start with the current weight.
* Compute the gradient.
* Move a small step in the opposite direction of the gradient.
* Repeat.

---

# Learning Rate

The learning rate controls the size of each update.

### Very Small Learning Rate

```text
Slow Learning
```

Advantages:

* Stable learning
* Smooth convergence

Disadvantages:

* Takes a long time to train

---

### Very Large Learning Rate

```text
Large Jumps
```

Advantages:

* Faster updates

Disadvantages:

* May overshoot the minimum
* May never converge
* Can become unstable

---

### Good Learning Rate

A balanced learning rate allows the model to converge efficiently while maintaining stability.

Common values:

```python
0.1

0.01

0.001

0.0001
```

The optimal value depends on the dataset and model architecture.

---

# Analytical Gradient for Linear Regression

For the Mean Squared Error loss:

Weight gradient:

[
\frac{\partial L}{\partial w}
=============================

-\frac{2}{n}
\sum x_i(y_i-\hat y_i)
]

Bias gradient:

[
\frac{\partial L}{\partial b}
=============================

-\frac{2}{n}
\sum (y_i-\hat y_i)
]

These gradients tell the optimizer how the parameters should change.

---

# Complete Training Algorithm

```text
Initialize w and b

Repeat:

    Predict

    Compute Loss

    Compute Gradient

    Update Parameters

Until Loss Stops Decreasing
```

---

# Algorithm Pseudocode

```python
Initialize w, b

for each epoch:

    predictions = model(X)

    loss = Loss(y, predictions)

    gradient_w = ...

    gradient_b = ...

    w = w - learning_rate * gradient_w

    b = b - learning_rate * gradient_b
```

---

# Visualization

The training process can be visualized as moving downhill on a loss curve.

```text
Loss
 ▲
 |
 |                ●
 |             ●
 |          ●
 |       ●
 |    ●
 |  ●
 |●__________________________► Weight

           Minimum
```

Each update moves the parameters closer to the minimum.

---

# Advantages

* Simple to understand
* Memory efficient
* Works for very large datasets
* Scales to deep neural networks
* Forms the basis of modern AI training

---

# Limitations

* Sensitive to the learning rate
* Can converge slowly
* May get stuck in local minima or saddle points
* Performance depends on feature scaling

---

# Variants of Gradient Descent

### Batch Gradient Descent

Uses the entire dataset for each update.

Pros:

* Stable updates

Cons:

* Slow for large datasets

---

### Stochastic Gradient Descent (SGD)

Uses one training example at a time.

Pros:

* Fast updates
* Escapes some local minima

Cons:

* Noisy optimization

---

### Mini-Batch Gradient Descent

Uses small batches of data (commonly 32–512 samples).

Pros:

* Faster
* More stable than SGD
* Efficient on GPUs

This is the most commonly used variant in modern Deep Learning.

---

# Real-World Applications

Gradient Descent is used to train:

* Linear Regression
* Logistic Regression
* Neural Networks
* CNNs
* RNNs
* LSTMs
* Autoencoders
* Transformers
* BERT
* GPT
* Vision Transformers (ViTs)
* Diffusion Models

---

# Gradient Descent in ResearchOS

Within ResearchOS, Gradient Descent is not used directly for semantic search.

Instead, it is responsible for training the models that ResearchOS relies on.

For example:

* Sentence embedding models
* Transformer models
* Reranking models
* Classification models
* Recommendation models

Every embedding generated by a pretrained model exists because Gradient Descent optimized millions (or billions) of parameters during training.

---

# Complexity

Time Complexity (per epoch)

[
O(n)
]

where (n) is the number of training examples.

Memory Complexity

[
O(1)
]

for simple linear regression (excluding dataset storage).

---

# Interview Questions

### Basic

1. What is Gradient Descent?
2. Why is it used?
3. What is a loss function?
4. What is a gradient?
5. Why do we move opposite to the gradient?

---

### Intermediate

6. What happens if the learning rate is too large?
7. What happens if it is too small?
8. What is the difference between Batch, SGD, and Mini-Batch Gradient Descent?
9. Why do we initialize parameters randomly?

---

### Advanced

10. Why does Gradient Descent work well for deep learning?
11. What are saddle points?
12. Why are optimizers like Adam often preferred over vanilla Gradient Descent?
13. How is Gradient Descent used to train Transformer models?

---

# Key Takeaways

* Machine Learning is an optimization problem.
* The objective is to minimize the loss function.
* The gradient indicates the direction of the steepest increase in loss.
* Gradient Descent moves in the opposite direction of the gradient.
* The learning rate controls the step size.
* Nearly every modern AI model is trained using Gradient Descent or one of its variants.

---

# Connection to the Next Module

Gradient Descent teaches us **how a model learns**.

The next question is:

> **What exactly are we updating?**

In Linear Regression, we update only two parameters (**w** and **b**).

In a Neural Network, we update **thousands or millions of weights** simultaneously.

The next module introduces **Neural Networks**, where Gradient Descent becomes even more powerful through **Backpropagation**.
