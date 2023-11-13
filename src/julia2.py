import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def fractal(x, y, threshold):
    c = complex(-0.2, 0.7)
    z = complex(x, y)

    for i in range(threshold):
        z = z**2 + c
        if abs(z) >= 4:  # divergió
            return i

    return threshold - 1  # no divergió


x_start, y_start = -2, -2  # una región interesante comienza aquí
width, height = 4, 4  # para 3 unidades hacia arriba y hacia la derecha
density_per_unit = 150  # cuántos píxeles por unidad

# eje real e imaginario
re = np.linspace(x_start, x_start + width, int(width * density_per_unit))
im = np.linspace(y_start, y_start + height, int(height * density_per_unit))

fig = plt.figure(figsize=(10, 10))  # instanciar una figura para dibujar
ax = plt.axes()  # crear un objeto de ejes


def animate(i):
    ax.clear()  # limpiar objeto de ejes
    ax.set_xticks([])  # limpiar ticks del eje x
    ax.set_yticks([])  # limpiar ticks del eje y

    X = np.empty((len(re), len(im)))  # reinicializar la imagen similar a una matriz
    threshold = round(1.15 ** (i + 1))  # calcular el umbral actual

    # iteraciones para el umbral actual
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = fractal(re[i], im[j], threshold)

    # asociar colores a las iteraciones con una interpolación
    img = ax.imshow(X.T, interpolation="bicubic", cmap="magma")
    text = ax.text(
        0.02,
        0.02,
        f"nombre d'iteracions: {threshold}",
        transform=ax.transAxes,
        color="red",
    )

    # ax.axhline(y=len(im) / 2, color="black", linestyle="--")
    # ax.axvline(x=len(re) / 2, color="black", linestyle="--")

    ax.set_xlim(0, len(re))
    ax.set_ylim(0, len(im))

    # ax.axhline(y=0, color='black', linestyle='--')
    # ax.axvline(x=0, color='black', linestyle='--')

    # for i in range(1, 4):
    #     ax.axhline(y=len(im) / 3 * i, color='black', linestyle=':')
    #     ax.axvline(x=len(re) / 3 * i, color='black', linestyle=':')

    # for i in range(1, 4):
    #     ax.text(-0.02, len(im) / 3 * i, f'{int(len(im) / 3 * i)}', color='black', ha='right')
    #     ax.text(len(re) / 3 * i, -0.02, f'{int(len(re) / 3 * i)}', color='black', va='top')

    return [img, text]


anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save("animacio6.gif", writer="pillow", fps=10)
