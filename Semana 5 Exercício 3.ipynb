import matplotlib.pyplot as plt
import numpy as np
import control as ctl
from control import (TransferFunction, bode_plot, feedback, margin)
C = TransferFunction([1], [1])
H = TransferFunction(1, [1,0.5,0])
K = 0.06 # 0.148
L = K*C*H

# malha fechada
Y_R = feedback(L, 1)
print('MF = ',Y_R)
# polos da malha fechada - sistema estável
print('Polos = ',ctl.damp(Y_R))

# margens de ganho (gm) e fase (pm) e frequencias
gm, pm, wg, wp = margin(L)
(gm, pm, wg, wp)

print('margem de ganho', gm) # ctl.mag2db(gm)
print('margem de fase', pm)
print('freq de w_180', wg)
print('freq de w_c', wp)

plt.figure(2)
plt.title("Bode plot")
ctl.bode_plot(0.06*L,grid = True)
ctl.bode_plot(1.48*L,grid = True)
plt.show()