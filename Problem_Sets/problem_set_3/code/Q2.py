import numpy as np


def ReLU_activation(w, x, b):
    ReLU_values = []
    for wi, bi in zip(w, b):
        z = wi.dot(x) + bi

        if z > 0:
            value = (z + np.abs(z)) / 2
        else:
            value = 0

        ReLU_values.append(value)

    return np.array(ReLU_values)


def sigmoid_activation(w, x, b):
    sigmoid_values = []
    for wi, bi in zip(w, b):
        z = wi.dot(x) + bi

        value = 1 / (1 + np.exp(-z))
        sigmoid_values.append(value)

    return np.array(sigmoid_values)


def softmax_activation(x):
    softmax_values = []

    for xi in x:
        value = np.exp(xi) / np.sum(np.exp(x))
        softmax_values.append(value)

    return np.array(softmax_values)


def cross_entropy(px, softmax_values):
    loss_value = -1 * (px.dot(np.log(softmax_values)))

    return loss_value


def main():
    vi = np.array([[0.5, -0.1, -0.2, 0.1, -0.4],
                   [-0.9, 0.7, 0.7, -0.5, 0.2]])
    
    wi = np.array([[0.1, 0.6],
                   [0.8, 0.4],
                   [0.7, -0.2]])
    
    x = np.array([5, 7, 4, 3, 2])
    
    v_biases = np.array([0.02, -0.01])
    w_biases = np.array([0.0, 0.05, 0.04])

    # v_biases = np.array([0, 0])
    # w_biases = np.array([0, 0, 0])

    px = np.array([0, 0, 1])

    ReLU_values = ReLU_activation(vi, x, v_biases)
    sigmoid_values = sigmoid_activation(wi, ReLU_values, w_biases)
    softmax_values = softmax_activation(sigmoid_values)
    loss_value = cross_entropy(px, softmax_values)

    print(loss_value)

if __name__ == "__main__":
    main()