#version 1.04
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import numpy as np
import os
import random

print('=-=-'*12)
print('VERSION 1.04')
print('=-=-'*12)

numberoffile = int(input('how many files?: '))
DATATOANALYZE = str(input('name of files: '))

lengtharq =0
analyze=list()

plt.xlabel('diameter of particle [nm]')
plt.ylabel('frequence')
#plt.title(f'Comparison between different doses')
#mudei aqui
for files in range(1,numberoffile+1):

	arq = pd.read_csv(f'{DATATOANALYZE}{files}.csv')

	mean = np.mean(arq['Length'])
	variance = np.var(arq['Length'])
	sigma = np.sqrt(variance)
	x = np.linspace(min(arq['Length']), max(arq['Length']),100)
	
	r = lambda: random.randint(0,255) #cor aleatória
	
	
	plt.hist(arq['Length'] , bins=20, rwidth=0.95 , color='#%02X%02X%02X' % (r(),r(),r()),alpha=0.05)
	#plt.plot(x,norm.pdf(x,mean,sigma))
	print(f'{mean}	{variance}	{sigma}')
plt.savefig('histparticle1.png')



