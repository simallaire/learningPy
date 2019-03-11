import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h,w,maxit=40):
    y,x = np.ogrid[-1.4:1.3:h*1j,-2:0.8:w*1j]
    c = x+y*1j
    z=c
    divtime = maxit + np.zeros(z.shape,dtype=int)

    for i in range(maxit):
        z= z**2+c
        diverge=z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge]=2

    return divtime


for i in range(1,101):
    plt.imshow(mandelbrot(100*i,100*i,i))
    plt.delaxes
    fn = 'fractal/img'+str(i)+'.png'
    dpi = 100*i
    plt.savefig(fn,dpi=dpi)
    plt.close
    print(fn+" - "+str(100*i)+"X"+str(100*i)+", "+str(dpi)+"dpi")

