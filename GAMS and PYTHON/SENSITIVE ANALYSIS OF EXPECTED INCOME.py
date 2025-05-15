import pulp
import numpy as np
import matplotlib.pyplot as plt

# Define the sets
candidates = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12']
our_plans = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
rival_plans = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']

# Define the parameters
Qp = {'p1': 0.8, 'p2': 0.9, 'p3': 0.8, 'p4': 1, 'p5': 0.8, 'p6': 0.7, 'p7': 0.6, 'p8': 1, 'p9': 0.6, 'p10': 0.7}
Rq = {'r1': 0.8, 'r2': 0.5, 'r3': 0.8, 'r4': 0.8, 'r5': 1, 'r6': 0.6, 'r7': 1, 'r8': 0.6, 'r9': 0.9, 'r10': 0.7}
Pq = {'r1': 24, 'r2': 20, 'r3': 24, 'r4': 24, 'r5': 28, 'r6': 20, 'r7': 28, 'r8': 20, 'r9': 26, 'r10': 22}
Vp = {'p1': 5.5, 'p2': 5.5, 'p3': 3.5, 'p4': 2.5, 'p5': 2, 'p6': 1, 'p7': 5.5, 'p8': 0, 'p9': 1, 'p10': 2}
d = {'v1': 0.8, 'v2': 0.8, 'v3': 0.8, 'v4': 1, 'v5': 0.9, 'v6': 0.7, 'v7': 1, 'v8': 0.6, 'v9': 0.9, 'v10': 0.9, 'v11': 0.6, 'v12': 0.9}
Sp = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 23.6, 'p9': 0, 'p10': 0}

X = {
    ('v1', 'p1'): 34, ('v1', 'p2'): 45, ('v1', 'p3'): 25, ('v1', 'p4'): 39, ('v1', 'p5'): 40, ('v1', 'p6'): 35, ('v1', 'p7'): 45, ('v1', 'p8'): 39, ('v1', 'p9'): 26, ('v1', 'p10'): 34,
    ('v2', 'p1'): 25, ('v2', 'p2'): 43, ('v2', 'p3'): 31, ('v2', 'p4'): 45, ('v2', 'p5'): 29, ('v2', 'p6'): 33, ('v2', 'p7'): 38, ('v2', 'p8'): 30, ('v2', 'p9'): 43, ('v2', 'p10'): 40,
    ('v3', 'p1'): 39, ('v3', 'p2'): 44, ('v3', 'p3'): 35, ('v3', 'p4'): 39, ('v3', 'p5'): 38, ('v3', 'p6'): 27, ('v3', 'p7'): 36, ('v3', 'p8'): 34, ('v3', 'p9'): 25, ('v3', 'p10'): 35,
    ('v4', 'p1'): 38, ('v4', 'p2'): 37, ('v4', 'p3'): 30, ('v4', 'p4'): 34, ('v4', 'p5'): 39, ('v4', 'p6'): 33, ('v4', 'p7'): 35, ('v4', 'p8'): 30, ('v4', 'p9'): 29, ('v4', 'p10'): 42,
    ('v5', 'p1'): 37, ('v5', 'p2'): 30, ('v5', 'p3'): 38, ('v5', 'p4'): 29, ('v5', 'p5'): 40, ('v5', 'p6'): 33, ('v5', 'p7'): 32, ('v5', 'p8'): 26, ('v5', 'p9'): 39, ('v5', 'p10'): 38,
    ('v6', 'p1'): 30, ('v6', 'p2'): 42, ('v6', 'p3'): 39, ('v6', 'p4'): 32, ('v6', 'p5'): 41, ('v6', 'p6'): 35, ('v6', 'p7'): 42, ('v6', 'p8'): 31, ('v6', 'p9'): 35, ('v6', 'p10'): 36,
    ('v7', 'p1'): 25, ('v7', 'p2'): 34, ('v7', 'p3'): 34, ('v7', 'p4'): 38, ('v7', 'p5'): 29, ('v7', 'p6'): 44, ('v7', 'p7'): 26, ('v7', 'p8'): 42, ('v7', 'p9'): 42, ('v7', 'p10'): 43,
    ('v8', 'p1'): 39, ('v8', 'p2'): 36, ('v8', 'p3'): 44, ('v8', 'p4'): 26, ('v8', 'p5'): 33, ('v8', 'p6'): 27, ('v8', 'p7'): 27, ('v8', 'p8'): 39, ('v8', 'p9'): 25, ('v8', 'p10'): 40,
    ('v9', 'p1'): 29, ('v9', 'p2'): 39, ('v9', 'p3'): 38, ('v9', 'p4'): 27, ('v9', 'p5'): 37, ('v9', 'p6'): 34, ('v9', 'p7'): 43, ('v9', 'p8'): 32, ('v9', 'p9'): 28, ('v9', 'p10'): 27,
    ('v10', 'p1'): 36, ('v10', 'p2'): 32, ('v10', 'p3'): 37, ('v10', 'p4'): 37, ('v10', 'p5'): 27, ('v10', 'p6'): 30, ('v10', 'p7'): 25, ('v10', 'p8'): 35, ('v10', 'p9'): 43, ('v10', 'p10'): 32,
    ('v11', 'p1'): 40, ('v11', 'p2'): 34, ('v11', 'p3'): 34, ('v11', 'p4'): 25, ('v11', 'p5'): 28, ('v11', 'p6'): 29, ('v11', 'p7'): 40, ('v11', 'p8'): 36, ('v11', 'p9'): 43, ('v11', 'p10'): 40,
    ('v12', 'p1'): 28, ('v12', 'p2'): 40, ('v12', 'p3'): 29, ('v12', 'p4'): 39, ('v12', 'p5'): 45, ('v12', 'p6'): 31, ('v12', 'p7'): 34, ('v12', 'p8'): 35, ('v12', 'p9'): 33, ('v12', 'p10'): 35,
}

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

gamma = {
    ('v1', 'p8'): 1, ('v2', 'p8'): 1, ('v3', 'p8'): 1, ('v4', 'p8'): 1, ('v5', 'p8'): 1,
    ('v6', 'p8'): 1, ('v7', 'p8'): 1, ('v8', 'p8'): 1, ('v10', 'p8'): 1, ('v11', 'p8'): 1, ('v12', 'p8'): 1,
}

def optimize_model(Qp, Rq, Pq, Vp, d, Sp, X, Y, gamma):
    # Initialize the model
    model = pulp.LpProblem("Bi-Level_Optimization", pulp.LpMinimize)

    # Define the decision variables
    alpha = pulp.LpVariable.dicts("alpha", [(i, j) for i in candidates for j in our_plans], lowBound=0, cat='Continuous')
    beta = pulp.LpVariable.dicts("beta", [(i, k) for i in candidates for k in rival_plans], lowBound=0, cat='Continuous')
    z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

    # Define the objective function
    model += z

    # Define the constraints
    for i in candidates:
        model += pulp.lpSum([alpha[i, j] * (X[i, j] - Qp[j] * (Vp[j] * gamma.get((i, j), 0) + Sp[j])) for j in our_plans]) + \
                 pulp.lpSum([beta[i, k] * (Y[i, k] - Rq[k] * Pq[k]) for k in rival_plans]) <= z

    for i in candidates:
        model += pulp.lpSum([alpha[i, j] for j in our_plans]) + pulp.lpSum([beta[i, k] for k in rival_plans]) == d[i]

    # Solve the model
    model.solve()

    return pulp.value(z)

# Sensitivity analysis for X
X_values = np.linspace(0.5, 1.5, 10)
profits_X = []

for scale in X_values:
    new_X = {(i, j): scale * X[i, j] for i in candidates for j in our_plans}
    profit = optimize_model(Qp, Rq, Pq, Vp, d, Sp, new_X, Y, gamma)
    profits_X.append(profit)

# Sensitivity analysis for Y
Y_values = np.linspace(0.5, 1.5, 10)
profits_Y = []

for scale in Y_values:
    new_Y = {(i, k): scale * Y[i, k] for i in candidates for k in rival_plans}
    profit = optimize_model(Qp, Rq, Pq, Vp, d, Sp, X, new_Y, gamma)
    profits_Y.append(profit)

# Plotting the sensitivity analysis
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(X_values, profits_X, marker='o')
plt.xlabel('Scale factor for X')
plt.ylabel('Optimal z')
plt.title('Sensitivity Analysis for X')

plt.subplot(1, 2, 2)
plt.plot(Y_values, profits_Y, marker='o')
plt.xlabel('Scale factor for Y')
plt.ylabel('Optimal z')
plt.title('Sensitivity Analysis for Y')

plt.tight_layout()
plt.show()
