from mv import *
from graph import *


def f(x, A, b):
    return 0.5 * x.T @ A @ x - x.T @ b


def grad_f(x, A, b):
    return x.T @ A - b


def conjugate_gradient(f, grad_f, A, b, x0):
    N = A.shape[0]
    zeros = np.zeros(N)
    rho_0 = -grad_f(x0, A, b)

    if np.isclose(rho_0, zeros).all():
        return x0

    omega_k = rho_0.copy()
    alpha_0 = (rho_0.T @ rho_0) / (omega_k.T @ A @ omega_k)
    xk = x0 + alpha_0 * omega_k

    for k in range(1, N):
        rho_k = -grad_f(xk, A, b)  # rho(k) = ...
        if np.isclose(rho_k, zeros).all():
            return xk
        lambda_k = -(rho_k.T @ A @ omega_k) / (
            omega_k @ A @ omega_k
        )  # lamba(k-1) = ...
        omega_k = rho_k + lambda_k * omega_k  # omega(k) = ... + ...*omega(k-1)
        alpha_k = (rho_k.T @ rho_k) / (omega_k.T @ A @ omega_k)  # alpha(k) =
        xk = xk + alpha_k * omega_k  # x(k+1) = xk + ...

    return xk


if __name__ == "__main__":
    N = 15
    string = "3D"
    X = np.linspace(0, 1, N + 2)[1:-1]
    A, b, x0 = example2(N, string)
    U = conjugate_gradient(f, grad_f, A, b, x0)
    graph(X, U, string)
