from scipy.stats import nanmean, gaussian_kde
from matplotlib import pyplot as plt
import numpy as np
def pdf(serie,nbins=100,zeros=True):
     'returns pdf (x,y) from a serie with nbins'
     k = gaussian_kde(serie) #kernel density
     m = k.dataset.min()
     M = k.dataset.max()
     x = np.arange(m,M,(M-m)/nbins)
     v = k.evaluate(x) #density curve
     if zeros:
         inter=x[1]-x[0]
         x=np.array([x[0]-inter]+list(x)+[x[-1]+inter])
         v=np.array([0]+list(v)+[0])
     return {'x':x,'v':v}


def violin_plot(axis,data,color='blue',alpha=1, x_offset=0):
     if len(data.shape)>1:
          data=data.reshape(data.size)
     density = pdf(data)
     axis.fill_betweenx(density['x']+x_offset,x1=density['v'],x2=-density['v'],facecolor=color,alpha=alpha)
    
