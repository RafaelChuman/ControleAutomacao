import matplotlib.pyplot as plt
import numpy as np
import control as ctl
from control import (TransferFunction)

#ver mais sobre o comando rlocus em 
# https:/python-control.readthedocs.io/en/latest/generated/control.matlab.rlocus.html

# rlocus exemplo 1 (slide 5 Aula 7 Semana 3)
# argumento da função rlocus H(s) da equação catacteristica 1+CH(s)=0
#ex1 = TransferFunction(1, [1,10,0]) #função transferência de H(s)
ex1 = TransferFunction([1,-1], [1, 2.5, 4])
out = ctl.rlocus(ex1, kvect=None, xlim=None, ylim=None, plotstr=None, plot=True, print_gain=None, grid=None)

print(ex1)

#plot
plt.figure(1)
plt.plot(out[0], out[1] , 'k', linewidth=1.5, label='resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=1)
plt.xlabel('t')
plt.show() 



# rlocus exemplo 2 (slide 8 Aula 7 Semana 3)
# argumento da função rlocus H(s) da equação catacteristica 1+CH(s)=0
#ex2 = TransferFunction([1,-4,20], [1,6,8]) #função transferência de 1+kH(s)
ex2 = TransferFunction([1,-1], [1, 2.5, 4])
out = ctl.rlocus(ex2, kvect=None, xlim=None, ylim=None, plotstr=None, plot=True, print_gain=None, grid=None)

k= -1
# Malha fechada sys1 = linha de cima e sys2 a linha de baixo da realimentação
malha_fechada = ctl.feedback(sys1= k*ex2, sys2=1, sign=-1)
print(malha_fechada)

# dados do polos
wn, damping, pole = ctl.damp(malha_fechada)

#plot
plt.figure(1)
plt.plot(out[0], out[1] , 'k', linewidth=1.5, label='resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show() 

t = np.linspace(0,5,101)

# Resposta ao degrau do exemplo 2 com ganho crítico
tout, yout = ctl.step_response(malha_fechada, t, X0=0)

# T, yout = step_response(sys, T, X0)
plt.plot(tout, yout , 'k', linewidth=1.5, label='resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show() 
