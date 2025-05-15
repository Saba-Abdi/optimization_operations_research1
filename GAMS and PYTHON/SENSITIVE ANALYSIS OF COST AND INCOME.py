import pulp
import numpy as np
import matplotlib.pyplot as plt

# Define the sets and parameters as before
candidates = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12']
plans = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']

C = {'v1': 14, 'v2': 10, 'v3': 20, 'v4': 12, 'v5': 10, 'v6': 14, 'v7': 16, 'v8': 18, 'v9': 18, 'v10': 18, 'v11': 14, 'v12': 18}
n = {'v1': 40, 'v2': 56, 'v3': 50, 'v4': 48, 'v5': 48, 'v6': 42, 'v7': 48, 'v8': 50, 'v9': 40, 'v10': 50, 'v11': 60, 'v12': 58}
Mp = {'p1': 2, 'p2': 2.5, 'p3': 2, 'p4': 3, 'p5': 2, 'p6': 1.5, 'p7': 1, 'p8': 3, 'p9': 1, 'p10': 1.5}
Vp = {'p1': 5.5, 'p2': 5.5, 'p3': 3.5, 'p4': 2.5, 'p5': 2, 'p6': 1, 'p7': 5.5, 'p8': 0, 'p9': 1, 'p10': 2}
MinSalary = 23.6

def optimize_model(C, n):
    # Initialize the model
    model = pulp.LpProblem("Bi-Level_Optimization", pulp.LpMaximize)

    # Define the decision variables
    Sp = pulp.LpVariable.dicts("Sp", [(i, j) for i in candidates for j in plans], lowBound=0, cat='Continuous')
    Op = pulp.LpVariable.dicts("Op", plans, cat='Binary')
    gamma = pulp.LpVariable.dicts("gamma", [(i, j) for i in candidates for j in plans], cat='Binary')

    # Define the objective function
    model += pulp.lpSum([gamma[i, j] * n[i] for i in candidates for j in plans]) \
             - pulp.lpSum([Sp[i, j] + gamma[i, j] * (C[i] + Vp[j]) for i in candidates for j in plans]) \
             - pulp.lpSum([Op[j] * Mp[j] for j in plans])

    # Define the constraints
    for i in candidates:
        model += pulp.lpSum([gamma[i, j] for j in plans]) <= 1

    model += pulp.lpSum([gamma[i, j] for i in candidates for j in plans]) >= 5

    for j in plans:
        model += pulp.lpSum([gamma[i, j] for i in candidates]) <= 12 * Op[j]

    for i in candidates:
        for j in plans:
            model += Sp[i, j] >= MinSalary * gamma[i, j]

    # Solve the model
    model.solve()
    
    return pulp.value(model.objective)

# Sensitivity analysis for n_i
n_values = np.linspace(min(n.values()) * 0.5, max(n.values()) * 1.5, 10)
profits_n = []

for scale in n_values:
    new_n = {i: scale for i in candidates}
    profit = optimize_model(C, new_n)
    profits_n.append(profit)

# Sensitivity analysis for C_i
C_values = np.linspace(min(C.values()) * 0.5, max(C.values()) * 1.5, 10)
profits_C = []

for scale in C_values:
    new_C = {i: scale for i in candidates}
    profit = optimize_model(new_C, n)
    profits_C.append(profit)

# Plotting the sensitivity analysis
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values, profits_n, marker='o')
plt.xlabel('n_i values')
plt.ylabel('Total Profit')
plt.title('Sensitivity Analysis for n_i')

plt.subplot(1, 2, 2)
plt.plot(C_values, profits_C, marker='o')
plt.xlabel('C_i values')
plt.ylabel('Total Profit')
plt.title('Sensitivity Analysis for C_i')

plt.tight_layout()
plt.show()
