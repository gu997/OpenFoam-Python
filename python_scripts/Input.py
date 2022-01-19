def V_inlet(path,v_in):
    file1 = open(path + '0/U_original', 'r')
    Lines = file1.readlines()
    file1.close()
    
    
    for i in range(len(Lines)):
        if Lines[i].find('    inlet')==0:
            start=i
        elif Lines[i].find('    outlet')==0:
            end=i
            break
     
    
    v_inlet=['    inlet\n','    {\n','        type            fixedValue;\n','        value           uniform ('+str(v_in)+' 0 0);\n','    }\n']
    
    
    L=Lines[:start]+v_inlet+Lines[end:]    
    
    file1 = open(path + '0/U', 'w')
    file1.writelines(L)
    file1.close()
    
def Ps_outlet(path,Ps_out):
    file1 = open(path + '0/p_rgh_original', 'r')
    Lines = file1.readlines()
    file1.close()
    
    
    for i in range(len(Lines)):
        if Lines[i].find('    outlet')==0:
            start=i
        elif Lines[i].find('    front')==0:
            end=i
            break
     
    
    ps_outlet=['    outlet\n','    {\n','        type            prghPressure;\n','        p               uniform '+str(Ps_out)+';\n','        value           uniform '+str(Ps_out)+';\n','    }\n']
    
    
    L=Lines[:start]+ps_outlet+Lines[end:]    
    
    file1 = open(path + '0/p_rgh', 'w')
    file1.writelines(L)
    file1.close()
    
if __name__ == "__main__":
    
    path='/home/nicola/Desktop/delgosha/delgosha_m/'



    v_in=7.4  
    Ps_out=66000
    
    V_inlet(path,v_in)
    Ps_outlet(path,Ps_out)