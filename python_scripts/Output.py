import os


def P_inlet(path,Dir,  Lines):

    for i in range(len(Lines)):
        if Lines[i].find('    inlet')==0:
            start=i
        elif Lines[i].find('    outlet')==0:
            end=i
            break
        
    list_inlet=[]
    for i in range(start,end):
        list_inlet.append(Lines[i])
        
    inlet_number=[]
    for i in list_inlet:
        try:
            inlet_number.append(float(i))
        except:
            pass
      
    del inlet_number[0]
    
    P_i=sum(inlet_number) / len(inlet_number)
    return P_i

def P_outlet(path,Dir,  Lines): 
    
    for i in range(len(Lines)):
        if Lines[i].find('    outlet')==0:
            start=i
        elif Lines[i].find('    front')==0:
            end=i
            break
        
       
    list_outlet=[]
    for i in range(start,end):
        list_outlet.append(Lines[i])
        
    outlet_number=[]
    for i in list_outlet:
        try:
            outlet_number.append(float(i))
        except:
            pass
      
    del outlet_number[0]
    
    P_o=sum(outlet_number) / len(outlet_number)
    return P_o

def directory_and_read(path):
    Dirs=os.listdir(path)
    
    D_number=[]
    for D in Dirs:
        try:
            D_number.append(float(D))
        except:
            pass
        
    Dir=max(D_number)
    
        
    file1 = open(path + str(Dir) + '/totalPMean', 'r')
    Lines = file1.readlines()
    file1.close()
    
    
    return Dir, Lines
    

if __name__ == "__main__":
    
    path='/home/nicola/Desktop/delgosha/delgosha_m/'
    #Dir='1e-06'

    Dir, Lines=directory_and_read(path)  
 

    
    P_i=P_inlet(path,Dir,  Lines)
    P_o=P_outlet(path,Dir,  Lines)