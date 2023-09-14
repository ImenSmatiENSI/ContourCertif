import cmath
import pdb
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def any_number_range(a,b,s=1):
    result = []
    if (a == b):
        result.append(int(a))
        #print(type(result))
    else:
        mx = max(a,b)
        mn = min(a,b)
       
        # inclusive upper limit. If not needed, delete '+1' in the line below
        while(mn <= mx):
            # if step is positive we go from min to max
            if s > 0:
                result.append(int(mn))
                mn += s
            # if step is negative we go from max to min
            if s < 0:
                result.append(int(mx))
                mx += s
    #print(result)
    return result

def convolution_Lower_upper_360(cont,dim_x,dim2_x,dim_y,dim2_y):
    print ("start")
    
    x_cont=cont[0:120]
    y_cont=cont[120:240]
    x_list=np.concatenate([x_cont,x_cont,x_cont])
    y_list=np.concatenate([y_cont,y_cont,y_cont])
    x=np.array(x_list)
    y=np.array(y_list)
    print(x.shape)
    print(y.shape)
    #lx, ly = f.shape

    
    
    x_low_bound = np.zeros(360,)
    y_low_bound = np.zeros(360,)
    x_up_bound = np.zeros(360,)
    y_up_bound = np.zeros(360,)
    y2_low_bound = np.zeros(360,)
    y2_up_bound = np.zeros(360,)
    x2_low_bound = np.zeros(360,)
    x2_up_bound = np.zeros(360,)
    y_final_low = np.zeros(360,)
    y_final_up = np.zeros(360,)
    x_final_low = np.zeros(360,)
    x_final_up = np.zeros(360,)
    cont_low_bound = np.zeros(240,)
    cont_up_bound = np.zeros(240,)
         
    for i in range (1,len(x)):
        for j in range (1,len(y)):
            neighbor_x=[]
            neighbor_y=[]
            for t in any_number_range(-dim_x,dim_x):
                for t2 in any_number_range(-dim_y,dim_y):
                    if (i-t)<len(x) and (i-t)>0 :
                        neighbor_x.append(x[i-t])
                        if (j-t2)<len(y) and (j-t2)>0 :
                            neighbor_y.append(y[j-t2])
                            
                        else:
                            neighbor_y.append(0)
                    else :   
                        neighbor_x.append(0) 
                            
                #print('nei',neighbor)
            y_low = min(neighbor_y)
            y_up = max(neighbor_y)
            y_low_bound[j]=y_low
            y_up_bound[j]=y_up 
            x_low = min(neighbor_x)
            x_up = max(neighbor_x)  
            #x_filter = sum(np.multiply(neighbor,filt))
            #print(x_filter)
            x_low_bound[i]=x_low
            x_up_bound[i]=x_up   
            
                    
                  
            neighbor2_x=[]
            neighbor2_y=[]
            for t1 in any_number_range(-dim2_x,dim2_x):
                for t2 in any_number_range(-dim2_y,dim2_y):
                    if (i-t1)<len(x) and (i-t1)>0 :
                        neighbor2_x.append(x[i-t1])
                        if (j-t2)<len(y) and (j-t2)>0 :
                            neighbor2_y.append(y[j-t2]) 
                    
                        else:
                            neighbor2_y.append(0)
                    else:   
                        neighbor2_x.append(0)
                        
            y2_low = min(neighbor2_y)
            y2_up = max(neighbor2_y)
            y2_low_bound[j]=y2_low
            y2_up_bound[j]=y2_up 
            y_final_low[j] = min(y_low_bound[j],y2_low_bound[j])
            y_final_up[j] = max(y_up_bound[j],y2_up_bound[j]) 
            
            
            x2_low = min(neighbor2_x)
            x2_up = max(neighbor2_x) 
            x2_low_bound[i]=x2_low
            x2_up_bound[i]=x2_up                 
        x_final_low[i]= min(x_low_bound[i],x2_low_bound[i])
        x_final_up[i]=  max(x_up_bound[i],x2_up_bound[i]) 
        
        #print(x_filter.shape)    
        #print(y_filter.shape) 
        
    Lower_bound_final=np.concatenate([x_final_low[120:240],y_final_low[120:240]]) 
    Upper_bound_final=np.concatenate([x_final_up[120:240], y_final_up[120:240]])
  #  print(Lower_bound_final.shape)
 
                    
                    
    
    return (Lower_bound_final,Upper_bound_final)
