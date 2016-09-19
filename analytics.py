# analytics.py
#
# sample analytics project
#
# LKS, September 2016, 1 week after defense
#
#
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
#
#
set1x=np.linspace(0,100, 250)
set1ya=list(np.random.normal(50, 20, 50))
set1yb=list(np.random.normal(80, 25, 50))
set1yc=list(np.random.normal(120, 30, 50))
set1yd=list(np.random.normal(80, 45, 50))
set1ye=list(np.random.normal(60, 25, 50))
set1y=set1ya+set1yb+set1yc+set1yd+set1ye
# add some noise
#datax=set1+(np.random.rand(100)*100.0) 
#
# make it a scatter plot
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(set1x, set1y,s=20, marker='x', color='violet')
ax.set_xlabel('Temperature (F)')
ax.set_ylabel('Sales')
os.chdir('/Users/loisks/Desktop')
plt.savefig('scatterAll.png')
plt.close()
#
# best fit line?
slope, intercept, r_value, p_value, std_err = stats.linregress(set1x,set1y)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(set1x, set1y,s=20, marker='x', color='violet')
ax.plot(set1x, (set1x*slope)+intercept, lw=2, c='blue')
ax.set_xlabel('Temperature (F)')
ax.set_ylabel('Sales')
os.chdir('/Users/loisks/Desktop')
plt.savefig('bestfitscatterAll.png')
plt.close()
#
# print the max sales here
print('max value is: '+str(np.max((set1x*slope)+intercept) )+' at location : '+
      str(set1x[np.argmax((set1x*slope)+intercept)]))

#
# now do a curve fit
z=np.polyfit(set1x, set1y,2)
p=np.poly1d(z)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(set1x, set1y,s=20, marker='x', color='violet')
plt.plot(set1x, p(set1x),lw=2, c='Orange')
ax.set_xlabel('Temperature (F)')
ax.set_ylabel('Sales')
os.chdir('/Users/loisks/Desktop')
plt.savefig('curvefitscatterAll.png')
plt.close()

print('max value of curve fit: ' +str(np.max((set1x*slope)+intercept) )+' at location : '+ str(set1x[np.argmax(p(set1x))]))
