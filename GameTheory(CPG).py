import numpy as np

# Матрицы выигрышей для полицейского и преступника
payoff_matrix_police = np.array([
    [3, -1],
    [2, -2]
])

payoff_matrix_criminal = np.array([
    [-3, 1],
    [-2, 2]
])

# Вероятности выбора стратегий для полицейского и преступника
probabilities_police = np.array([0.6, 0.4])
probabilities_criminal = np.array([0.5, 0.5])

# Вычисление ожидаемого выигрыша для полицейского
expected_payoff_police = np.dot(probabilities_police, payoff_matrix_police)
print("Ожидаемый выигрыш полицейского:", expected_payoff_police)

# Вычисление ожидаемого выигрыша для преступника
expected_payoff_criminal = np.dot(probabilities_criminal, payoff_matrix_criminal)
print("Ожидаемый выигрыш преступника:", expected_payoff_criminal)

# Оптимизация стратегий
from scipy.optimize import linprog

# Задача линейного программирования для минимизации потерь полицейского
objective_function = [1, 1]
constraints = [
    (-payoff_matrix_police[0], -1),
    (-payoff_matrix_police[1], -1)
]
bounds = [(0, None), (0, None)]
result = linprog(objective_function, constraints, bounds=bounds)
optimal_probabilities_police = result.x

# Задача линейного программирования для максимизации выигрыша преступника
objective_function = [1, 1]
constraints = [
    (payoff_matrix_criminal[0], 1),
    (payoff_matrix_criminal[1], 1)
]
bounds = [(0, None), (0, None)]
result = linprog(objective_function, constraints, bounds=bounds)
optimal_probabilities_criminal = result.x

# Печать оптимальных стратегий
print("\nОптимальные вероятности выбора стратегий для полицейского:", optimal_probabilities_police)
print("Оптимальные вероятности выбора стратегий для преступника:", optimal_probabilities_criminal)