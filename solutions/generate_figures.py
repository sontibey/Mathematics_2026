import os
os.environ['MPLCONFIGDIR']='/tmp/workbook-mpl'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':10,'figure.dpi':120,'axes.grid':True,'grid.alpha':.25})
def axes2(ax,title,equal=False):
 ax.axhline(0,color='gray',lw=.7);ax.axvline(0,color='gray',lw=.7);ax.set(xlabel='x',ylabel='y',title=title)
 if equal: ax.set_aspect('equal',adjustable='box')
def save(fig,group,n):
 p=ROOT/group/'figures'/f'problem_{n:02}.png';p.parent.mkdir(exist_ok=True)
 fig.tight_layout();fig.savefig(p,bbox_inches="tight");plt.close(fig)
G='2_Geometry/03_second_degree_curves_and_surfaces'
t=np.linspace(0,2*np.pi,500)
fig,axs=plt.subplots(2,2,figsize=(10,8))
for ax in axs.flat: axes2(ax,'',True)
axs[0,0].plot(3*np.cos(t),3*np.sin(t));axs[0,0].set_title('Circle: radius 3')
axs[0,1].plot(4*np.cos(t),3*np.sin(t));axs[0,1].set_title('Ellipse: semiaxes 4 and 3')
y=np.linspace(-8,8,500);axs[1,0].plot(y*y/8,y);axs[1,0].set_title('Parabola: $y^2=8x$')
u=np.linspace(-1.5,1.5,300)
for sign in [-1,1]:axs[1,1].plot(sign*3*np.cosh(u),2*np.sinh(u),color='C0')
x=np.linspace(-8,8,100)
for sign in [-1,1]:axs[1,1].plot(x,sign*2*x/3,'--',color='gray')
axs[1,1].set_title('Hyperbola: vertices at $x=\\pm3$');save(fig,G,1)
for n in [3,4,5]:
 fig,ax=plt.subplots(figsize=(7,5));axes2(ax,'',True)
 if n==3:
  ax.plot(5*np.cos(t),3*np.sin(t));ax.scatter([5,-5,0,0],[0,0,3,-3]);ax.set_title('Ellipse: $x^2/25+y^2/9=1$')
 if n==4:
  y=np.linspace(-9,9,500);ax.plot(y*y/12,y);ax.scatter([0,3,3],[0,6,-6]);ax.set_title('Parabola: $y^2=12x$')
 if n==5:
  for sign in [-1,1]:ax.plot(sign*4*np.cosh(u),3*np.sinh(u),color='C0')
  x=np.linspace(-10,10,100)
  for sign in [-1,1]:ax.plot(x,sign*3*x/4,'--',color='gray')
  ax.scatter([-4,4],[0,0]);ax.set_title('Hyperbola and asymptotes')
 save(fig,G,n)
def surf_ax(fig,loc,title):
 ax=fig.add_subplot(loc,projection='3d');ax.set(xlabel='x',ylabel='y',zlabel='z',title=title);ax.view_init(24,-55);return ax
u,v=np.meshgrid(np.linspace(-2,2,45),np.linspace(-2,2,45))
fig=plt.figure(figsize=(11,5))
for loc,z,title in [(121,u*u+v*v,'Elliptic paraboloid'),(122,u*u-v*v,'Hyperbolic paraboloid')]:
 ax=surf_ax(fig,loc,title);ax.plot_surface(u,v,z,cmap='viridis',alpha=.85)
save(fig,G,10)
theta,z=np.meshgrid(np.linspace(0,2*np.pi,65),np.linspace(-2.5,2.5,55))
fig=plt.figure(figsize=(11,5));ax=surf_ax(fig,121,'One-sheet hyperboloid')
r=np.sqrt(1+z*z);ax.plot_surface(r*np.cos(theta),r*np.sin(theta),z,cmap='viridis',alpha=.85)
ax=surf_ax(fig,122,'Two-sheet hyperboloid')
for sign in [-1,1]:
 th,z0=np.meshgrid(np.linspace(0,2*np.pi,65),np.linspace(1,2.5,40));r=np.sqrt(z0*z0-1)
 ax.plot_surface(r*np.cos(th),r*np.sin(th),sign*z0,cmap='viridis',alpha=.85)
save(fig,G,11)
fig=plt.figure(figsize=(11,5))
for loc,title,r in [(121,'Double circular cone',np.abs(z)),(122,'Circular cylinder: radius 2',np.full_like(z,2))]:
 ax=surf_ax(fig,loc,title);ax.plot_surface(r*np.cos(theta),r*np.sin(theta),z,cmap='viridis',alpha=.8)
save(fig,G,14)
fig=plt.figure(figsize=(11,5));ax=fig.add_subplot(121);axes2(ax,'Shifted ellipse',True)
ax.plot(1+3*np.cos(t),-2+2*np.sin(t));ax.scatter([1,-2,4,1,1],[-2,-2,-2,-4,0]);ax=surf_ax(fig,122,'Double elliptic cone')
r=np.abs(z);ax.plot_surface(r*np.cos(theta)/2,r*np.sin(theta),z,cmap='viridis',alpha=.85);save(fig,G,15)
G='3_Calculus/03_function_analysis'
for n in [1,3,8,10,12,13,14]:
 fig,ax=plt.subplots(figsize=(8,5));axes2(ax,'')
 if n==1:
  x=np.linspace(-1.5,3.5,700);ax.plot(x,x**3-3*x*x+2);ax.scatter([0,2,1],[2,-2,0]);ax.set_title('Cubic: extrema and inflection');ax.set_ylim(-5,5)
 if n==3:
  for x in [np.linspace(-7,1.96,400),np.linspace(2.04,9,400)]:ax.plot(x,(x+1)/(x-2),color='C0')
  ax.axvline(2,color='C3',ls='--');ax.axhline(1,color='C3',ls='--');ax.scatter([-1,0],[0,-.5]);ax.set_ylim(-8,8);ax.set_title('Rational function and asymptotes')
 if n==8:
  x=np.linspace(-2.5,2.5,700);ax.plot(x,x**4-4*x*x);a=np.sqrt(2/3);ax.scatter([-np.sqrt(2),0,np.sqrt(2)],[-4,0,-4],label='extrema');ax.scatter([-a,a],[-20/9,-20/9],label='inflections');ax.legend();ax.set_ylim(-5,8);ax.set_title('Quartic: extrema and inflection points')
 if n==10:
  x=np.linspace(-7,7,900);ax.plot(x,x/(x*x+1));a=np.sqrt(3);ax.scatter([-1,1],[-.5,.5],label='extrema');ax.scatter([-a,0,a],[-a/4,0,a/4],label='inflections');ax.legend();ax.set_title('$f(x)=x/(1+x^2)$')
 if n==12:
  x=np.linspace(-3.2,3.2,700);ax.plot(x,x*x-4,'--',alpha=.5,label='before absolute value');ax.plot(x,np.abs(x*x-4),label='after absolute value');ax.scatter([-2,0,2],[0,4,0]);ax.legend();ax.set_title('Reflection of the negative part')
 if n==13:
  x=np.linspace(.07,16,900);ax.plot(x,np.log(x)/x);e=np.e;ax.scatter([1,e,e**1.5],[0,1/e,1.5/e**1.5]);ax.set_ylim(-2,.6);ax.set_title('$f(x)=\\ln(x)/x$')
 if n==14:
  x=np.linspace(-4,3,700);ax.plot(x,x**3/3+x*x/2-2*x,label='$g(x)$');ax.plot(x,x**3/3+x*x/2-2*x+2,'--',label='$g(x)+2$');ax.scatter([-2,1],[10/3,-7/6]);ax.legend();ax.set_ylim(-6,7);ax.set_title('Same derivative, vertical translations')
 save(fig,G,n)
G='3_Calculus/01_limits'
fig,ax=plt.subplots(figsize=(7,5));axes2(ax,'One-sided limits at $x=2$')
for x in [np.linspace(-3,1.96,500),np.linspace(2.04,7,500)]:ax.plot(x,1/(x-2),color='C0')
ax.axvline(2,ls='--',color='C3');ax.set_ylim(-10,10);save(fig,G,9)
fig,axs=plt.subplots(1,2,figsize=(11,4))
n=np.arange(1,101);axs[0].plot(n,5/(np.sqrt(1+5/n)+1),'.',ms=3);axs[0].axhline(2.5,ls='--',color='C3');axs[0].set(xlabel='n',ylabel='sequence value',title='Approach to 5/2')
x=np.linspace(3,5,500);axs[1].plot(x,1/(np.sqrt(x)+2));axs[1].plot([4],[.25],marker='o',mfc='white',mec='C3');axs[1].axhline(.25,ls='--',color='C3');axs[1].set(xlabel='x',ylabel='f(x)',title='Approach to 1/4; hole at x=4');save(fig,G,15)
G='3_Calculus/04_integrals'
fig,axs=plt.subplots(1,2,figsize=(10,4));x=np.linspace(-2,2,500)
for ax,y,title in [(axs[0],x,'Signed integral: 0'),(axs[1],np.abs(x),'Geometric area: 4')]:
 axes2(ax,title);ax.plot(x,y);ax.fill_between(x,0,y,where=y>=0,alpha=.3);ax.fill_between(x,0,y,where=y<0,color='C3',alpha=.3)
save(fig,G,12)
fig,ax=plt.subplots(figsize=(7,4));axes2(ax,'Triangle area 2 + rectangle area 4 = 6')
x=np.linspace(-1,1,150);ax.plot(x,x+1);ax.fill_between(x,0,x+1,alpha=.3);x=np.linspace(1,3,150);ax.plot(x,0*x+2);ax.fill_between(x,0,0*x+2,alpha=.3);save(fig,G,14)
G='3_Calculus/05_applications'
fig,ax=plt.subplots(figsize=(8,5));x=np.linspace(0,50,500);ax.plot(x,60*x-1.2*x*x);ax.scatter([25],[750],color='C3');ax.annotate('Maximum: (25 m, 750 m²)',(25,750),xytext=(28,680),arrowprops={'arrowstyle':'->'});ax.set(xlabel='Perpendicular side x (m)',ylabel='Area (m²)',title='Exhibition room under a 30,000 PLN budget',xlim=(0,50),ylim=(0,820));save(fig,G,12)
print('Generated 20 referenced figures.')
