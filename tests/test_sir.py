"Test exponential convergence"
# from models.sir import SIR

from models.sir import SIR


def test_six_days():
    p = [0.95, 0.38]  # Default parameters from WHO
    nw0 = [341555, 445, 0]  # Ealing initial conditions
    t = 6  # 7 days
    my_sir = SIR()
    my_sir.set_params(p, nw0)
    my_sir.solve(t, t + 1)
    removed_end = my_sir.fetch()[-1, -1]

    assert abs(removed_end - 8360.68517) < 0.0001
