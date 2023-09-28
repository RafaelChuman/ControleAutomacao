# pip install "git+https://github.com/alchemyst/Skogestad-Python"
# pip install matplotlib==3.1.3

import numpy as np
import robustcontrol
from robustcontrol import InternalDelay
from robustcontrol import utils
import matplotlib.pyplot as plt
from control import (TransferFunction, step_response, bode_plot, feedback)

# parâmetros usados na aproximação (slide 3 Aula 15 - Semana 6)
K = 2.5; # valor de regime permanente alcançado com a entrada degrau
L = 0.3; # tempo necessário entre o valor inicial e a intersecção da linha tangente
tau = 4.5; # tempo necessário entre a intersecção e o regime permanente

sys_id = utils.InternalDelay.from_tf_coefficients([1,5], [1,10,2], [0])
# função transferência do sistema original sem atraso
G_id = utils.InternalDelay.from_tf_coefficients([K], [tau,1], [L])
# função transferência do sistema aproximado com atraso

t = np.linspace(0, 20, 5000)
y = sys_id.simulate(lambda t: [1], t)
ydelay = G_id.simulate(lambda t: [1], t)

plt.figure(1)
plt.plot(t, y, 'b', linewidth=1.5, label='original')
plt.plot(t, ydelay, 'r--', linewidth=1.5, label='aproximado')
plt.xlabel('t(s)')
plt.ylabel('resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.show()



# parâmetros usados na aproximação (slide 3 Aula 15 - Semana 6)
K = 2.5; # valor de regime permanente alcançado com a entrada degrau
L = 0.3; # tempo necessário entre o valor inicial e a intersecção da linha tangente
tau = 4.5; # tempo necessário entre a intersecção e o regime permanente

G = TransferFunction([1,5],[1,10,2]);
# PID por Ziegler Nichols
Cpid = TransferFunction(0.6*tau*np.convolve([1,1/L],[1,1/L]),[1,0]);

MA = Cpid*G # malha aberta
MF = feedback(1*MA, 1) # malha fechada

w = np.linspace(0.1, 100, 1001)

plt.figure(2) # Diagrama de Bode da Malha Aberta
mag, phase, omega = bode_plot(MA, omega=w, dB=True)
plt.legend(["Malha Aberta"])
plt.show