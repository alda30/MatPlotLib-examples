#  Subplots (important)
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(facecolor='white')

ax1 = plt.subplot(111, projection='polar')
# ax2 = plt.subplot(412, projection='polar')
# ax3 = plt.subplot(413, projection='polar')
# ax4 = plt.subplot(414, projection='polar')


shearDisp, angle, contactForce = np.loadtxt('polarForceData.0.csv', delimiter=' ', unpack=True, skiprows=1)

# All settings for AX1
ax1.bar(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)

ax1.set_xlabel('Normal force (N)')



# ax1.spines['left'].set_color('#3a3a3a')
# ax1.spines['right'].set_color('#3a3a3a')
# ax1.spines['bottom'].set_color('#3a3a3a')
# ax1.spines['top'].set_color('#3a3a3a')


# ax1.spines['left'].set_linewidth('2.5')
# ax1.spines['bottom'].set_linewidth('2.5')
# ax1.spines['right'].set_linewidth('2.5')
# ax1.spines['top'].set_linewidth('2.5')

ax1.tick_params(axis='x', colors='#3a3a3a')
ax1.tick_params(axis='y', colors='#3a3a3a')

plt.subplots_adjust(left=0.1, bottom= 0.12, right= 0.9, top=0.91, wspace=0.15, hspace= 0.2)

ax1.grid(True,color='grey', linestyle=':')
# ax1.set_xticks([0,30,60,90,120,150,180])

ax1.legend(loc = 'best')


plt.show()