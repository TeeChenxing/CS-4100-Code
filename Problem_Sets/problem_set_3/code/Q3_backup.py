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


def ReLU_derivative(vi, xi):
    z = vi.dot(xi)
    
    return (z > 0).astype(int)


def sigmoid_derivative(sigmoid_values):
    derivative = sigmoid_values * (1 - sigmoid_values)

    return derivative


def softmax_derivative(S):
    derivative = np.zeros((len(S), len(S)))

    for i in range(len(S)):
        for j in range(len(S)):
            if i == j:
                derivative[i, j] = S[i] * (1 - S[i])
            else:
                derivative[i, j] = -S[i] * S[j]
                
    return derivative


def compute_w_gradient(yi, S, sig_val, ReLU_val):
    first_layer = yi * -1
    second_layer = 1 / S
    third_layer = softmax_derivative(S)
    fourth_layer = sigmoid_derivative(sig_val)
    fifth_layer = 1
    sixth_layer = ReLU_val

    print("Respect to W nodes")
    print(f"First Layer: {first_layer}")
    print(f"Second Layer: {second_layer}")
    print(f"Third Layer: {third_layer}")
    print(f"Fourth Layer: {fourth_layer}")
    print(f"Fifth Layer: {fifth_layer}")
    print(f"Sixth Layer: {sixth_layer}")

    result = first_layer * second_layer
    result = result.dot(third_layer)
    result = result * fourth_layer
    result = np.outer(result, sixth_layer)

    print(f"Result: {result}")
    print()
    return 0


def compute_v_gradient(yi, S, w, sig_val, ReLU_val, vi, xi):
    first_layer = yi * -1
    second_layer = 1 / S
    third_layer = softmax_derivative(S)
    fourth_layer = sigmoid_derivative(sig_val)
    fifth_layer = 1
    sixth_layer = w
    seventh_layer = ReLU_derivative(vi, xi)
    eigth_layer = 1
    ninth_layer = xi

    print("Respect to V nodes")
    print(f"First Layer: {first_layer}")
    print(f"Second Layer: {second_layer}")
    print(f"Third Layer: {third_layer}")
    print(f"Fourth Layer: {fourth_layer}")
    print(f"Fifth Layer: {fifth_layer}")
    print(f"Sixth Layer: {sixth_layer}")
    print(f"Seventh Layer: {seventh_layer}")
    print(f"Eight Layer: {eigth_layer}")
    print(f"Ninth Layer: {ninth_layer}")

    result = first_layer * second_layer
    result = result.dot(third_layer)
    result = result * fourth_layer
    result = result.dot(sixth_layer)
    result = result * seventh_layer
    result = np.outer(result, ninth_layer)

    return result


def main():
    vi = np.array([[0.5, -0.1, -0.2, 0.1, -0.4],
                   [-0.9, 0.7, 0.7, -0.5, 0.2]])
    
    wi = np.array([[0.1, 0.6],
                   [0.8, 0.4],
                   [0.7, -0.2]])
    
    x = np.array([5, 7, 4, 3, 2])

    # we can set biases to 0, essentially ignoring them
    v_biases = np.array([0, 0])
    w_biases = np.array([0, 0, 0])

    px = np.array([0, 0, 1])

    ReLU_values = ReLU_activation(vi, x, v_biases)
    sigmoid_values = sigmoid_activation(wi, ReLU_values, w_biases)
    softmax_values = softmax_activation(sigmoid_values)
    loss_value = cross_entropy(px, softmax_values)

    w_gradient = compute_w_gradient(px, softmax_values, sigmoid_values, ReLU_values)
    v_gradient = compute_v_gradient(px, softmax_values, wi, sigmoid_values, ReLU_values, vi, x)

if __name__ == "__main__":
    main()