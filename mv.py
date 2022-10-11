import numpy as np


def sys_2D(N):
    A = np.zeros((N, N))
    A[np.arange(N), np.arange(N)] = np.array(-2).repeat(N)
    A[np.arange(N - 1), np.arange(1, N)] = np.ones(N - 1)
    A[np.arange(1, N), np.arange(N - 1)] = np.ones(N - 1)
    return -((N + 1) ** 2) * A


def sys_3D(N):
    N2 = N * N
    A = np.zeros((N2, N2))
    A[np.arange(N2), np.arange(N2)] = np.array(-4).repeat(N2)
    A[np.arange(N2 - 1), np.arange(1, N2)] = np.tile(
        np.concatenate((np.ones(N - 1), np.zeros(1))), N
    )[:-1]
    A[np.arange(1, N2), np.arange(N2 - 1)] = np.tile(
        np.concatenate((np.ones(N - 1), np.zeros(1))), N
    )[:-1]
    A[np.arange(N * (N - 1)), np.arange(N, N2)] = np.ones(N * (N - 1))
    A[np.arange(N, N2), np.arange(N * (N - 1))] = np.ones(N * (N - 1))
    return -((N + 1) ** 2) * A


def sys(N, string):
    if string == "2D":
        return sys_2D(N)
    elif string == "3D":
        return sys_3D(N)
    else:
        print("string is not define")
        exit()


def vector_1(N, string):
    if string == "2D":
        N_ = N
    elif string == "3D":
        N_ = N * N
    else:
        print("string is not define")
        exit()
    return np.ones(N_)


def vector_charge(N, string):
    n, p = divmod(N, 2)
    if string == "2D":
        N_ = 1
    elif string == "3D":
        N_ = N
    else:
        print("string is not define")
        exit()
    return np.concatenate(
        (np.zeros(N_).repeat(n), np.ones(N_), np.zeros(N_).repeat(n - 1 + p))
    )


def init(N, string):
    if string == "2D":
        N_ = N
    elif string == "3D":
        N_ = N * N
    else:
        print("string is not define")
        exit()
    return np.random.normal(0, 1, N_)


def example1(N, string):
    return sys(N, string), vector_1(N, string), init(N, string)


def example2(N, string):
    return sys(N, string), vector_charge(N, string), init(N, string)
