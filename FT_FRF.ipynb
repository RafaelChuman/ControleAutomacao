import matplotlib.pyplot as plt
import numpy as np
import control as ctl
from control import (TransferFunction)

m = 1
c = 2
k = 4

# função tranferência
# sistema massa-mola-amortecedor
plantMalhaAberta = TransferFunction(1, [m, c, k])

# malha aberta (K(s)G(s))
#plantMalhaAberta = TransferFunction([1,6], [1,3,3,6]) # Exercício 1

# malha fechada com feedback
plantMalhaFechada = ctl.feedback(plantMalhaAberta, 1)

# malha fechada calculada com o diagrama de blocos
#plantMalhaFechada = TransferFunction([1,6], [1,3,3,6]) # Exercício 1
plantMalhaFechada = TransferFunction([1,-1], [1, 2.5, 4])

print('MA =', plantMalhaAberta)
print('MF =', plantMalhaFechada)

# polos do sistema
polos = ctl.pole(plantMalhaFechada)
print(polos)
zeros = ctl.zeros(plantMalhaFechada)
print(zeros)


ctl.bode_plot(plantMalhaFechada)

#Bode Plot
plt.figure(1)
plt.show()

ctl.nyquist(plantMalhaFechada)

#Nyquist Plot
plt.figure(2)
#plt.grid()
plt.show()

ctl.nichols_plot(plantMalhaFechada)

#Nichols Plot
plt.figure(3)
#plt.grid()
plt.show()

