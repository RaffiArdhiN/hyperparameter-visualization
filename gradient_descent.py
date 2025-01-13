import numpy as np

def data_example():
    return np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])

def line_example(data):
    x1, y1 = data[0]
    x2, y2 = data[1]
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return m, c

def grad_descent(data, line, learning_rate=0.01, iterations=100):
    m, c = line
    history = []
    for i in range(iterations):
        grad_m = 0
        grad_c = 0
        
        for x, y in data:
            grad_m += -2 * x * (y - (m * x + c))
            grad_c += -2 * (y - (m * x + c))
            
        m -= learning_rate * grad_m
        c -= learning_rate * grad_c
        
        # rss = sum((y - (m * x + c))**2 for x, y in data)
        # print(f"Iteration: RSS={rss:.4f}, m={m:.4f}, c={c:.4f}")
        loss = sum((y - (m * x + c))**2 for x, y in data)
        history.append({'m' : m, 'c' : c, 'loss' : loss})
        print(f"Iteration {i + 1}: m={m}, c={c}, loss={loss}")
    
    return history, m, c
        
if __name__ == '__main__':
    data = data_example()
    initial_line = line_example(data)
    final_m, final_c = grad_descent(data, initial_line, learning_rate=0.01, iterations=100)
    print(f"Final Line: y = {final_m:.4f}x + {final_c:.4f}")