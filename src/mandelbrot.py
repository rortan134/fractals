import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fractal(x, y, threshold):
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # divergió
            return i

    return threshold - 1  # no divergió

x_start, y_start = -2, -1.5  # una región interesante comienza aquí
width, height = 3, 3  # para 3 unidades hacia arriba y hacia la derecha
density_per_unit = 250  # cuántos píxeles por unidad

# eje real e imaginario
re = np.linspace(x_start, x_start + width, width * density_per_unit )
im = np.linspace(y_start, y_start + height, height * density_per_unit)

fig = plt.figure(figsize=(10, 10))  # instanciar una figura para dibujar
ax = plt.axes()  # crear un objeto de ejes

def animate(i):
    ax.clear()  # limpiar objeto de ejes
    ax.set_xticks([])  # limpiar ticks del eje x
    ax.set_yticks([])  # limpiar ticks del eje y
    
    X = np.empty((len(re), len(im)))  # reinicializar la imagen similar a una matriz
    threshold = round(1.15**(i + 1))  # calcular el umbral actual
    
    # iteraciones para el umbral actual
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = fractal(re[i], im[j], threshold)
    
    # asociar colores a las iteraciones con una interpolación
    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save('animacio.gif',writer='imagemagick')