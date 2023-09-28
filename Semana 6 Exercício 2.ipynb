import numpy as np
import robustcontrol
from robustcontrol import InternalDelay
from robustcontrol import utils
import matplotlib.pyplot as plt
from control import (TransferFunction, step_response, bode_plot, feedback)

# Função transferência do sistema a ser controlado (slide 9 - aula 15 - semana 6)
H = TransferFunction([10], np.convolve([1,10,0],[1,6]))
# convolve faz a multiplicação entre polinômios

Kc = 96 # por Critério de Rough-Hurwitz
MF = feedback(Kc*H, 1) # malha fechada com o ganho crítico

# resposta ao degrau da malha fechada com ganho crítico
t = np.linspace(0, 5, 1001) # vetor tempo

plt.figure(1) # resposta ao degrau da malha fechada com ganho crítico
tout, yout1 = step_response(MF, t, X0=0)
plt.plot(tout, yout1, 'b', linewidth=1.5, label='K=96')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t (s)')
plt.ylabel('resposta')
plt.show()


Kc = 96
Tc = 0.8
# Controlador PID de acordo com o Método Zielgler Nichols (ZN)
Cp = Kc/2;
print('Cp = ', Cp)
Cpi = TransferFunction([Tc*0.45*Kc,1.2*0.45*Kc],[Tc,0]);
print('Cpi = ', Cpi)
Cpid = TransferFunction(0.075*Kc*Tc*np.convolve([1,4/Tc],[1,4/Tc]),[1,0]);
print('Cpid = ', Cpid)

Lp = Cp*H # malha aberta com P
Lpi = Cpi*H # malha aberta com PI
Lpid = Cpid*H # malha aberta com PID 


w = np.linspace(0.1, 100, 1001)


plt.figure(2) # Diagrama de Bode da Malha aberta
mag, phase, omega = bode_plot(Lp, omega=w, dB=True, linestyle='solid', color='blue')
mag, phase, omega = bode_plot(Lpi, omega=w, dB=True, linestyle='dashdot', color='red')
mag, phase, omega = bode_plot(Lpid, omega=w, dB=True, linestyle='dashed', color='black')
plt.legend(["malha aberta com P", "malha aberta com PI", "malha aberta com PID"])
plt.show



sys_p = feedback(Lp, 1) # malha fechada com P
sys_pi = feedback(Lpi, 1) # malha fechada com PI
sys_pid = feedback(Lpid, 1) # malha fechada com PID

t = np.linspace(0, 20, 1001)
plt.figure(4) # Resposta ao Degrau da Malha Fechada
tout, yout1 = step_response(sys_p, t, X0=0)
tout, yout2 = step_response(sys_pi, t, X0=0)
tout, yout3 = step_response(sys_pid, t, X0=0)
plt.plot(tout, yout1, 'b', linewidth=1.5, label='malha aberta com P')
plt.plot(tout, yout2, 'r-.', linewidth=1.5, label='malha aberta com PI')
plt.plot(tout, yout3, 'k--', linewidth=1.5, label='malha aberta com PID')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show()