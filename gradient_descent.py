

def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


def safe(f):

    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf') # infinity
    return safe_f

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0 #valor inicial
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]


        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        #para se a funcao estiver convergindo
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value
