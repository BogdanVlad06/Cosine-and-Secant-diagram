import numpy as np
from matplotlib import pyplot as plt

y_lim = (-3, 3)
x_lim = (0, 2 * np.pi)

# generating points for Ox Axis
x_pts = np.linspace(start=0, stop=2, num=500)

x_pi = x_pts * np.pi

# generating points for Oy Axis
y_cos_pts =  np.cos(x_pi)
y_sec_pts =  1 / np.where(abs(y_cos_pts) < 0.02, np.nan, y_cos_pts) #handling where the function is discontinuous, for cosine values close or equal to 0

# print(y_cos_pts)
# print(y_sec_pts)

# Ensuring the secant function visually tends to infinity at discontinuities
nan_positions = np.where(np.isnan(y_sec_pts))[0]
y_sec_pts[nan_positions - 1] = 1e6 * y_sec_pts[nan_positions - 1]
y_sec_pts[nan_positions + 1] = 1e6 * y_sec_pts[nan_positions + 1]


plt.figure()

plt.title("Cosine and Secant")
plt.ylabel('f(x)')
plt.xlabel('x values')

plt.plot(x_pi, y_cos_pts, 'r', label= r'$\mathrm{cos}(x) = \frac{Adjacent}{Hypotenuse}$')
plt.plot(x_pi, y_sec_pts, 'b', label= r'$\mathrm{sec}(x) = \frac{Hypotenuse}{Adjacent}$')

# setting the step between written values below Ox and Oy Axis
plt.xticks(ticks=np.arange(x_lim[0], x_lim[1] + 0.1, step=np.pi/6), rotation=90)
#plt.yticks(ticks=np.arange(y_lim[0], y_lim[1], step=1), rotation=90)

# limit of values that range on the axes
plt.xlim(x_lim[0], x_lim[1])
plt.ylim(y_lim[0], y_lim[1])
plt.axhline(0, color='black', linewidth=0.8)

# important Ox points of Pi
plt.axvline(0, color='black', linestyle='dashed')
plt.axvline(np.pi / 2, color='blue', linestyle='dashed')
plt.axvline(np.pi, color='black', linestyle='dashed')
plt.axvline(3 * np.pi / 2, color='blue', linestyle='dashed')
plt.axvline(2 * np.pi, color='black', linestyle='dashed')

# important Oy points of cos
plt.axhline(1, color='black', linestyle='dotted')
plt.axhline(-1, color='black', linestyle='dotted')

# Quadrant highlight
plt.axvspan(0, np.pi / 2, facecolor="#3cf2ef", alpha=0.5, label='Quadrant 1')
plt.axvspan(np.pi / 2, np.pi, facecolor="#f23c42", alpha=0.5, label='Quadrant 2')
plt.axvspan(np.pi,3 * np.pi / 2, facecolor="#eff23c", alpha=0.5, label='Quadrant 3')
plt.axvspan(3 * np.pi / 2, 2 * np.pi, facecolor="#57f23c", alpha=0.5, label='Quadrant 4')
plt.legend(loc=(0, 0))
plt.grid()
plt.show()