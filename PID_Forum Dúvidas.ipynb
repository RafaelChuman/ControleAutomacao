import control
import numpy as np
from scipy.optimize import minimize

# Sistema a ser controlado: G(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
G = control.TransferFunction(num, den)

# Função objetivo a ser minimizada
def objective(params):
    Kp, Ki, Kd = params
    C = Kp + Ki * control.tf([1], [1, 0]) + Kd * control.tf([1, 0], 1) # Controlador PID
    T = control.feedback(C*G)  # Sistema em malha fechada
    
    # Aqui você pode adicionar várias métricas de desempenho
    t, y = control.step_response(T)
    overshoot = np.max(y) - 1  # para uma resposta ao degrau unitário
    settling_time_index = np.where(y < 1.02)[0][-1]
    settling_time = t[settling_time_index]
    
    # Simples exemplo: combinando overshoot e settling_time
    J = overshoot + settling_time
    return J

# Restrições
def constraint1(params):
    Kp, Ki, Kd = params
    C = Kp + Ki * control.tf([1], [1, 0]) + Kd * control.tf([1, 0], 1) # Controlador PID
    T = control.feedback(C*G)
    poles = control.pole(T)
    
    # garantindo que todos os polos estão no semiplano esquerdo
    return np.min(poles.real)

# Restrições e limites
cons = [{'type': 'ineq', 'fun': constraint1}]
bnds = [(0, 10), (0, 10), (0, 10)]  # Limites para Kp, Ki, Kd

# Otimização
result = minimize(objective, [1, 1, 1], bounds=bnds, constraints=cons)

print("Optimized Kp, Ki, Kd:", result.x)