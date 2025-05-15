import pulp
import numpy as np
import matplotlib.pyplot as plt

# Define the sets and parameters as before
candidates = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12']
plans = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
rival_plans = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']

C = {'v1': 14, 'v2': 10, 'v3': 20, 'v4': 12, 'v5': 10, 'v6': 14, 'v7': 16, 'v8': 18, 'v9': 18, 'v10': 18, 'v11': 14, 'v12': 18}
n = {'v1': 40, 'v2': 56, 'v3': 50, 'v4': 48, 'v5': 48, 'v6': 42, 'v7': 48, 'v8': 50, 'v9': 40, 'v10': 50, 'v11': 60, 'v12': 58}
Mp = {'p1': 2, 'p2': 2.5, 'p3': 2, 'p4': 3, 'p5': 2, 'p6': 1.5, 'p7': 1, 'p8': 3, 'p9': 1, 'p10': 1.5}
Vp = {'p1': 5.5, 'p2': 5.5, 'p3': 3.5, 'p4': 2.5, 'p5': 2, 'p6': 1, 'p7': 5.5, 'p8': 0, 'p9': 1, 'p10': 2}
MinSalary = 23.6

def optimize_model(C, n, Rq, Pq, Y):
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

# Define the parameters for rival company
Rq = {'r1': 0.8, 'r2': 0.5, 'r3': 0.8, 'r4': 0.8, 'r5': 1, 'r6': 0.6, 'r7': 1, 'r8': 0.6, 'r9': 0.9, 'r10': 0.7}
Pq = {'r1': 24, 'r2': 20, 'r3': 24, 'r4': 24, 'r5': 28, 'r6': 20, 'r7': 28, 'r8': 20, 'r9': 26, 'r10': 22}
Y = {
    ('v1', 'r1'): 33, ('v1', 'r2'): 33, ('v1', 'r3'): 38, ('v1', 'r4'): 42, ('v1', 'r5'): 45, ('v1', 'r6'): 31, ('v1', 'r7'): 36, ('v1', 'r8'): 39, ('v1', 'r9'): 39, ('v1', 'r10'): 28,
    ('v2', 'r1'): 43, ('v2', 'r2'): 28, ('v2', 'r3'): 32, ('v2', 'r4'): 34, ('v2', 'r5'): 33, ('v2', 'r6'): 37, ('v2', 'r7'): 27, ('v2', 'r8'): 45, ('v2', 'r9'): 39, ('v2', 'r10'): 26,
    ('v3', 'r1'): 40, ('v3', 'r2'): 32, ('v3', 'r3'): 39, ('v3', 'r4'): 26, ('v3', 'r5'): 33, ('v3', 'r6'): 32, ('v3', 'r7'): 26, ('v3', 'r8'): 38, ('v3', 'r9'): 40, ('v3', 'r10'): 26,
    ('v4', 'r1'): 35, ('v4', 'r2'): 26, ('v4', 'r3'): 40, ('v4', 'r4'): 33, ('v4', 'r5'): 31, ('v4', 'r6'): 44, ('v4', 'r7'): 42, ('v4', 'r8'): 36, ('v4', 'r9'): 28, ('v4', 'r10'): 25,
    ('v5', 'r1'): 26, ('v5', 'r2'): 34, ('v5', 'r3'): 31, ('v5', 'r4'): 40, ('v5', 'r5'): 39, ('v5', 'r6'): 29, ('v5', 'r7'): 44, ('v5', 'r8'): 34, ('v5', 'r9'): 41, ('v5', 'r10'): 38,
    ('v6', 'r1'): 38, ('v6', 'r2'): 36, ('v6', 'r3'): 36, ('v6', 'r4'): 30, ('v6', 'r5'): 27, ('v6', 'r6'): 44, ('v6', 'r7'): 45, ('v6', 'r8'): 36, ('v6', 'r9'): 41, ('v6', 'r10'): 39,
    ('v7', 'r1'): 44, ('v7', 'r2'): 34, ('v7', 'r3'): 25, ('v7', 'r4'): 34, ('v7', 'r5'): 42, ('v7', 'r6'): 41, ('v7', 'r7'): 34, ('v7', 'r8'): 29, ('v7', 'r9'): 25, ('v7', 'r10'): 37,
    ('v8', 'r1'): 37, ('v8', 'r2'): 34, ('v8', 'r3'): 39, ('v8', 'r4'): 31, ('v8', 'r5'): 43, ('v8', 'r6'): 37, ('v8', 'r7'): 31, ('v8', 'r8'): 29, ('v8', 'r9'): 43, ('v8', 'r10'): 32,
    ('v9', 'r1'): 45, ('v9', 'r2'): 40, ('v9', 'r3'): 30, ('v9', 'r4'): 43, ('v9', 'r5'): 33, ('v9', 'r6'): 41, ('v9', 'r7'): 43, ('v9', 'r8'): 25, ('v9', 'r9'): 34, ('v9', 'r10'): 40,
    ('v10', 'r1'): 30, ('v10', 'r2'): 43, ('v10', 'r3'): 29, ('v10', 'r4'): 41, ('v10', 'r5'): 27, ('v10', 'r6'): 38, ('v10', 'r7'): 44, ('v10', 'r8'): 35, ('v10', 'r9'): 44, ('v10', 'r10'): 30,
    ('v11', 'r1'): 45, ('v11', 'r2'): 31, ('v11', 'r3'): 42, ('v11', 'r4'): 36, ('v11', 'r5'): 34, ('v11', 'r6'): 30, ('v11', 'r7'): 45, ('v11', 'r8'): 35, ('v11', 'r9'): 41, ('v11', 'r10'): 39,
    ('v12', 'r1'): 42, ('v12', 'r2'): 34, ('v12', 'r3'): 29, ('v12', 'r4'): 26, ('v12', 'r5'): 33, ('v12', 'r6'): 31, ('v12', 'r7'): 44, ('v12', 'r8'): 32, ('v12', 'r9'): 30, ('v12', 'r10'): 36,
}

# Ideal values for the new rival plan
ideal_quality = 1.0
ideal_salary = 100

# Sensitivity analysis for new rival plan's salary and quality
rival_quality_values = np.linspace(1.0, 0.5, 10)
rival_salary_values = np.linspace(50.0, 20.0, 10)
profits_quality = []
profits_salary = []

# Analyzing quality
for quality in rival_quality_values:
    Rq_new = Rq.copy()
    Pq_new = Pq.copy()
    Rq_new['r11'] = quality
    Pq_new['r11'] = ideal_salary
    # Update Y with the new rival plan
    new_Y = Y.copy()
    for i in candidates:
        new_Y[i, 'r11'] = 0  # Assume 0 salary to make rival plan more attractive
    profit = optimize_model(C, n, Rq_new, Pq_new, new_Y)
    profits_quality.append(profit)

# Analyzing salary
for salary in rival_salary_values:
    Rq_new = Rq.copy()
    Pq_new = Pq.copy()
    Rq_new['r11'] = ideal_quality
    Pq_new['r11'] = salary
    # Update Y with the new rival plan
    new_Y = Y.copy()
    for i in candidates:
        new_Y[i, 'r11'] = 0  # Assume 0 salary to make rival plan more attractive
    profit = optimize_model(C, n, Rq_new, Pq_new, new_Y)
    profits_salary.append(profit)

# Plotting the sensitivity analysis
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(rival_quality_values, profits_quality, marker='o')
plt.xlabel('New Rival Plan Quality')
plt.ylabel('Total Profit')
plt.title('Sensitivity Analysis for New Rival Plan Quality (Model 1)')

plt.subplot(1, 2, 2)
plt.plot(rival_salary_values, profits_salary, marker='o')
plt.xlabel('New Rival Plan Salary')
plt.ylabel('Total Profit')
plt.title('Sensitivity Analysis for New Rival Plan Salary (Model 1)')

plt.tight_layout()
plt.show()
