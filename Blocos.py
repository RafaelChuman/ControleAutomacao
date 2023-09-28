import matplotlib.pyplot as  plt
import numpy as np
import control as ctl
from control import (TransferFunction)




planta = ctl.TransferFunction(1, [1,5])  
print('Planta\n',planta)

# FT do controle 17.6
controle = ctl.TransferFunction(17.36, [1,0])  
print('Controle\n', controle)

t = np.linspace(0, 5, 101) # vetor tempo - integrar de t = 0 a t = 5


# Malha aberta L = Planta*Controle (ordem não atrapalha)
malhaAberta = ctl.series(planta, controle)

# Malha Fechada sys1 = Linha de cima e sys2 a linha de baixo da realimentação
malhaFechada = ctl.feedback(sys1= malhaAberta, sys2=1, sign=-1)
print("Malha Fechada\n", malhaFechada)

# Dados dos Polos
wn, damping, pole = ctl.damp(malhaFechada)

# Resposta ao Degrau
tOut, yOut = ctl.step_response(malhaFechada, t, X0=0)


#plot
plt.figure(1)
plt.plot(tOut, yOut, 'k', linewidth=1.5, label='resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show() 