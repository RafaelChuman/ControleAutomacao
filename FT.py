import matplotlib.pyplot as  plt
import numpy as np
import control as ctl
from control import (TransferFunction)


# parâmetros
m = 1 # massa
c = -0.5 # coef. amortecimento
k = 1 # coef. elasticidade


y0 = [0.0, 0.0]                 # cond. iniciais
t = np.linspace(0, 20, 1001)    # integrar de t = 0 a t = 20
u = np.ones(1001)               # entrada degrau unitário - no slide 6 da videoaula 4 u(t) = f(t)


# função transferência
# http://python-control.readthedocs.io/en/latest/generated/control.TransferFunction.html
plant_tf = TransferFunction(1, [m,c,k]) # (num, den)
print("plat_ft = \n", plant_tf);

# resposta forçada
xout, yout = ctl.forced_response(plant_tf, U=u, T=t)


zero = ctl.zeros(plant_tf) # zeros são as raízes do numerador
print('Zeros = ', zero)

polo = ctl.poles(plant_tf) # polos são as raízes do denominador
print('Polos = ', polo)

#plot
plt.plot(t, yout, 'k', linewidth=1.5, label='posição')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.1)
plt.xlabel('t')
plt.show()