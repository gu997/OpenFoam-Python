import numpy as np
import os

from Input import V_inlet,Ps_outlet
from Output import directory_and_read, P_inlet, P_outlet

#path='/home/nicola/Desktop/delgosha/delgosha_m/'



"INPUT"
v_in=7.3  
Ps_out=66000

"COPIA"

path='/home/nicola/Desktop/delgosha/'      #qui ci metti il percorso
old_dir='delgosha_m'                       #qui ci metti il nome della cartella originale che non vuoi modificare

os.chdir(path)
new_dir=old_dir+'_v_in='+str(v_in)+'_Ps_out='+str(Ps_out)
import shutil
shutil.copytree(old_dir, new_dir)

path=path+new_dir+'/'

"MODIFICA INPUT"
V_inlet(path,v_in)
Ps_outlet(path,Ps_out)


"CALCOLA"

os.chdir(path)
os.system('./Allrun.sh')


"OUTPUT"

Dir, Lines=directory_and_read(path)  

P_i=P_inlet(path,Dir,  Lines)
P_o=P_outlet(path,Dir,  Lines)

"POSTPROCESSO"
rho=998
P_din=1/2*rho*v_in**2
eta=(P_i-P_o)/P_din
print('eta=',eta)
