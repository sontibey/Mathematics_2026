from pathlib import Path
import re
import sympy as s
R=Path(__file__).resolve().parents[1];M=s.Matrix
x=s.symbols('x',real=True);p=s.symbols('p',positive=True);t,k,a=s.symbols('t k a',real=True)
checks=0
def ck(actual,expected=0):
 global checks
 diff=actual-expected
 if isinstance(diff,s.MatrixBase):ok=all(s.simplify(v)==0 for v in diff)
 else:ok=s.simplify(diff)==0
 assert ok,(actual,expected,diff)
 checks+=1
# Exact matrix computations, including every inverse and right-hand side.
for A,B in [([[2,1],[1,1]],[[1,-1],[-1,2]]),([[3,2],[5,4]],[[2,-1],[-s.Rational(5,2),s.Rational(3,2)]]),([[1,2],[3,5]],[[-5,2],[3,-1]]),([[1,1,0],[0,1,1],[1,0,1]],[[s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2)],[s.Rational(1,2),s.Rational(1,2),-s.Rational(1,2)],[-s.Rational(1,2),s.Rational(1,2),s.Rational(1,2)]]),([[2,3],[0,3]],[[s.Rational(1,2),-s.Rational(1,2)],[0,s.Rational(1,3)]]),([[2,1],[0,1]],[[s.Rational(1,2),-s.Rational(1,2)],[0,1]])]:
 A=M(A);B=M(B);ck(A*B,s.eye(A.rows));ck(B*A,s.eye(A.rows))
ck(M([[1,t],[t,1]])*M([[1,-t],[-t,1]])/(1-t*t),s.eye(2))
ck(M([[2,1],[1,3]])*M([s.Rational(8,5),s.Rational(9,5)]),M([5,7]))
ck(M([[2,1],[1,3]])*M([s.Rational(13,5),s.Rational(9,5)]),M([7,8]))
ck(M([[1,2],[0,1]])*M([[-1,-7],[2,4]]),M([[3,1],[2,4]]))
ck(M([[2,-1],[-3,2]])**2,M([[7,-4],[-12,7]]))
# Systems: substitute every stated particular or parametric solution.
z=s.symbols('z')
for A,b,sol in [([[1,1,1],[2,-1,1],[1,2,-1]],[6,3,2],[1,2,3]),([[1,1,1],[2,2,2],[1,-1,1]],[2,4,0],[1-t,1,t]),([[1,2,-1],[0,1,2]],[3,1],[1+5*t,1-2*t,t]),([[1,1],[2,2]],[2,4],[2-t,t]),([[2,1],[1,-1]],[5,1],[2,1]),([[2,1],[1,-1]],[1,4],[s.Rational(5,3),-s.Rational(7,3)]),([[1,1],[2,5]],[10,32],[6,4]),([[1,1,1],[1,t,1],[1,1,t]],[1,2,3],[(t-4)/(t-1),1/(t-1),2/(t-1)]),([[1,2,-1],[2,4,-2],[1,-1,2]],[0,0,0],[-t,t,t]),([[1,1,0],[0,1,1],[1,0,-1]],[10,8,2],[10-t,t,8-t])]:ck(M(A)*M(sol),M(b))
# Vector answers and normals.
ck(M([1,2,0]).cross(M([0,1,3])),M([6,-3,1]));ck(M([2,1,0]).cross(M([1,3,2])),M([2,-4,5]))
ck(M([1,1,-2]).cross(M([-1,3,-1])),M([5,3,4]));ck(M([1,2,0]).cross(M([0,1,1])).dot(M([2,5,1])),0)
ck(M([1,1,-1]).cross(M([-1,2,-1])),M([1,2,3]));ck(M([1,1,1]).cross(M([1,-1,1])),M([2,0,-2]))
ck(M([1,2,2]).dot(M([s.Rational(28,9),s.Rational(2,9),s.Rational(2,9)])),4)
# Complete-square identities and cross-section reductions.
y,z=s.symbols('y z',real=True)
for old,new in [(x*x+y*y-6*x+4*y-3,(x-3)**2+(y+2)**2-16),(4*x*x+9*y*y-16*x+18*y-11,4*(x-2)**2+9*(y+1)**2-36),(x*x+y*y+z*z-4*x+2*y-6*z-2,(x-2)**2+(y+1)**2+(z-3)**2-16),(4*x*x+9*y*y-8*x+36*y+4,4*(x-1)**2+9*(y+2)**2-36)]:ck(old,new)
# All derivative formulas in the derivative sheet.
for func,der in [(3*x**5-2*x**3+7*x-4,15*x**4-6*x*x+7),(2*s.sqrt(p)-3/p**2+p**s.Rational(3,2),p**(-s.Rational(1,2))+6*p**-3+s.Rational(3,2)*s.sqrt(p)),((x*x+1)*s.exp(x),s.exp(x)*(x*x+2*x+1)),((x*x+1)/(x-1),(x*x-2*x-1)/(x-1)**2),((3*x*x-2*x+1)**5,5*(3*x*x-2*x+1)**4*(6*x-2)),(x*s.sin(x)+s.cos(x),x*s.cos(x)),(s.sin(x*x+1),2*x*s.cos(x*x+1)),(s.exp(2*x-3)+5**x,2*s.exp(2*x-3)+5**x*s.log(5)),(s.log(x*x+1),2*x/(x*x+1)),(x*x-3*x+1,2*x-3),((x*x+1)**3*s.exp(x),(x*x+1)**2*s.exp(x)*(x*x+6*x+1)),(s.exp(s.sin(x*x)),2*x*s.cos(x*x)*s.exp(s.sin(x*x)))]:
 var=p if p in func.free_symbols else x;ck(s.diff(func,var),der)
# First/second derivatives used in analysis.
for func,d1,d2 in [(x**3-3*x*x+2,3*x*(x-2),6*x-6),((x+1)/(x-2),-3/(x-2)**2,6/(x-2)**3),(1/(x*x-1),-2*x/(x*x-1)**2,None),(x*s.exp(-x),(1-x)*s.exp(-x),None),(s.log(p)-p+1,1/p-1,None),(x**4-4*x*x,4*x*(x*x-2),12*x*x-8),(x/(1+x*x),(1-x*x)/(1+x*x)**2,2*x*(x*x-3)/(1+x*x)**3),(s.log(p)/p,(1-s.log(p))/p**2,(2*s.log(p)-3)/p**3)]:
 var=p if p in func.free_symbols else x;ck(s.diff(func,var),d1)
 if d2 is not None:ck(s.diff(func,var,2),d2)
ck((x**4-4*x*x).subs(x,s.sqrt(s.Rational(2,3)))+s.Rational(20,9))
# Every indefinite integral result, verified by differentiation.
for primitive,integrand,var in [(x**3-2*x*x+5*x,3*x*x-4*x+5,x),(s.Rational(4,3)*p**s.Rational(3,2)-3/p-s.Rational(3,4)*p**s.Rational(4,3),2*s.sqrt(p)+3/p**2-p**s.Rational(1,3),p),(2*s.exp(x)+3*s.sin(x)+4*s.cos(x),2*s.exp(x)+3*s.cos(x)-4*s.sin(x),x),((x*x+1)**5/5,2*x*(x*x+1)**4,x),(s.exp(x*x)/2,x*s.exp(x*x),x),(s.log(x*x+5),2*x/(x*x+5),x),((x-1)*s.exp(x),x*s.exp(x),x),(x*s.sin(x)+s.cos(x),x*s.cos(x),x),(-s.cos(3*x)/3,s.sin(3*x),x),(p*p*s.log(p)/2-p*p/4,p*s.log(p),p),(s.sqrt(x*x+1),x/s.sqrt(x*x+1),x),(x**3/3+x,x*x+1,x),(s.exp(x*x)+2,2*x*s.exp(x*x),x)]:ck(s.diff(primitive,var),integrand)
for func,lo,hi,answer in [(x,-1,2,s.Rational(3,2)),(x*x+1,0,2,s.Rational(14,3)),(x,-2,2,0),(s.Abs(x),-2,2,4),(x+1,-1,1,2),(x-x*x,0,1,s.Rational(1,6)),(4*x+2,0,5,60),(x*x,0,3,9),(100+20*x,0,5,750),(s.pi*x,0,4,8*s.pi)]:ck(s.integrate(func,(x,lo,hi)),answer)
# Limits: use exact symbolic computations independently of the written derivations.
for expr,var,point,answer in [((4*x*x-3*x+1)/(2*x*x+5*x-7),x,s.oo,2),((3*x+1)/(x*x+4),x,s.oo,0),((2*x**3-x)/(5*x*x+1),x,s.oo,s.oo),(s.sqrt(x*x+5*x)-x,x,s.oo,s.Rational(5,2)),((3*x*x-x+1)/(5*x*x+4*x-2),x,s.oo,s.Rational(3,5)),((x*x-4*x+3)/(x-3),x,3,2),((s.sqrt(x)-2)/(x-4),x,4,s.Rational(1,4)),((1+3*x)**(1/x),x,0,s.exp(3)),(s.sin(5*x)/x,x,0,5),(s.sin(2*x)/s.sin(3*x),x,0,s.Rational(2,3)),((1-s.cos(x))/x**2,x,0,s.Rational(1,2))]:
 actual=s.limit(expr,var,point)
 if answer==s.oo:assert actual==s.oo;checks+=1
 else:ck(actual,answer)
# Optimization identities, stationarity, and computer verification.
V=x*(30-2*x)*(40-2*x);xstar=(35-5*s.sqrt(13))/3
ck(s.diff(V,x).subs(x,xstar));print('Box optimum:',float(xstar),'cm; volume:',float(V.subs(x,xstar)),'cm^3')
C=2*s.sqrt(10000+x*x)+500-x;ck(s.diff(C,x).subs(x,100/s.sqrt(3)));ck(C.subs(x,100/s.sqrt(3)),500+100*s.sqrt(3))
A=60*x-s.Rational(6,5)*x*x;ck(A,750-s.Rational(6,5)*(x-25)**2);ck(s.diff(A,x).subs(x,25));ck(A.subs(x,25),750)
for v in [24,s.Rational(49,2),25,s.Rational(51,2),26]:print('Room x,y,area:',v,60-s.Rational(6,5)*v,A.subs(x,v))
# Structural checks apply to all assigned answers (including the previous 30).
assigned=[]
for sheet in (R/'exercises').rglob('*.md'):
 group=sheet.parent.name+'/'+sheet.stem.removesuffix('_en')
 for no in re.findall(r'^### (?:Exercise|Problem) (\d+)\.',sheet.read_text(),re.M):
  path=R/'solutions'/group/f'problem_{int(no):02}_solution.md';assert path.read_text().strip(),path;assigned.append(path)
assert len(assigned)==177
for path in assigned:
 text=path.read_text();assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',text),path
 for forbidden in [r'\operatorname',r'\text{',r'\boxed',r'\color',r'\hbox',r'\(',r'\[']:
  assert forbidden not in text,(path,forbidden)
 display=False;lines=text.splitlines()
 for i,line in enumerate(lines):
  assert line not in ['$', '='],(path,i,line)
  if line=='$$':
   if not display:assert i>0 and not lines[i-1],(path,i,'blank before')
   else:assert i+1==len(lines) or not lines[i+1],(path,i,'blank after')
   display=not display
  elif '$$' in line:raise AssertionError((path,i,'display not separate'))
  if r'\begin{pmatrix}' in line:assert display,(path,i,'matrix outside display')
 assert not display,path
 for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',text):
  if '://' not in target and not target.startswith('#'):assert (path.parent/target).exists(),(path,target)
print(f'PASS: {checks} exact symbolic assertions; all 177 assigned solutions populated; math delimiters/macros and figure links checked.')
