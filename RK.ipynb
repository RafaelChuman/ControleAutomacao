from scipy.integrate import odeint
import matplotlib.pyplot as  plt
import numpy as np

def EDO_mecanico(y, t, m, c, k, f):
    # substituição de variáveis
    # x1 -> posição
    # x2-> velocidade
    x1, x2 = y
    # sistema de ODEs de primeira ordem
    # x1' = y' = x2
    # x2' = y'' = - (b/m) x2 - (k/m) x1 + u/m
    dydt = [x2, -(c/m)*x2 -  (k/m)*x1 + (f/m)]
    return dydt


# parâmetros
m = 1 # massa
c = 2 # coef. amortecimento
k = 4 # coef. elasticidade
#f = 1 # força ext. - Entrada Unitária - degrau unitário / obs: no slide 6 da videoaula 4 u(t) = f(t)
f = 0 # força ext. - Entrada Nula

t = np.linspace(0, 2, 1001) # integrar de t = 0 a t = 20
u = np.ones(1001)               # entrada degrau unitário - no slide 6 da videoaula 4 u(t) = f(t)
y0 = [0.0, 0.0]                # cond. iniciais
#y0 = [0.0025, 0.0]             # cond. iniciais Posição Inicial 0.0025m
#y0 = [0.0, 1]                   # cond. iniciais Velocidade Inicial 1m/s

# integrar sistema de ODEs via odeint - https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
sol = odeint(EDO_mecanico, y0, t, args=(m, c, k, f))


#plot
plt.plot(t, sol[:, 0], 'b', label='x1(t) - posição')
plt.plot(t, sol[:, 1], 'g--', label='x2(t) - velocidade')
plt.legend(loc='best')
plt.xlabel('t (s)')
plt.grid()
plt.show()