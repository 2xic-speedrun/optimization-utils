import numpy as np

def cast_np_array(x):
    if type(x) == list:
        return np.asarray(x)
    return x

"""
class balancer written many years ago.
"""
def basic_split(X, y, shuffle=True, max_per_class=1000):
    X = cast_np_array(X)
    y = cast_np_array(y)

    classes = np.unique(y).shape[0]
    labels_split = np.arange(np.unique(y).shape[0] + 1)
    distr_classes = np.histogram(y, bins=labels_split)[0]
    lowest_class = min(max_per_class, np.min(distr_classes, axis=0))
    X_new = np.zeros((lowest_class * (classes), ) + X.shape[1:], dtype=X.dtype)
    y_new = np.zeros((lowest_class * (classes)))

    print(distr_classes)

    new_distr = np.zeros(((classes)))
    new_index = 0
    for index in range(X.shape[0]):
        class_id = int(y[index])
        if new_distr[class_id] < lowest_class:
            X_new[new_index] = X[index]
            y_new[new_index] = class_id
            new_distr[class_id] += 1
            new_index += 1
    print(np.histogram(y_new, bins=labels_split)[0])

    if shuffle:
        indices = np.arange(X_new.shape[0])
        np.random.shuffle(indices)
        X_new = X_new[indices]
        y_new = y_new[indices]

    return X_new, y_new
