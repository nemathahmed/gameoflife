import tkinter as tk
import json
import time
import os
import sys

vars=[]
root=tk.Tk()
root.title("Game of Life-Play")
c1=[]

with open('var_dict.json') as f:
    data = json.load(f)
st=list(data.keys())[-1]
r=int(st[st.index('R')+2:st.index(',')])+1
c=int(st[st.index('C')+2:])+1
print(r,c)




def getvars(data,r,c):
    for i in range(r):
        var_temp=[]
        for j in range(c):
            #print(data['C-%s,R-%s'%(i,j)])
            l=tk.IntVar(root,value=data["R-%s,C-%s"%(i,j)])
            var_temp.append(l)
        vars.append(var_temp)

    return vars

vars=[]
def produce_next_gen(vars,c1):
    #print(c1)
    #endbutton=tk.Button(root, width=3, text="Done", command=root.destroy()).grid(row=r+1,column=c-1)
    vars_new=[]
    for i in range(r):
        vars_new_temp=[]
        for j in range(c):
            l=tk.IntVar(root,value=0)
            vars_new_temp.append(l)
        vars_new.append(vars_new_temp)
        

    print("##....Playing....##")
    sys.stdout.write("\033[F")
    for i in range(1,r-1):
        for j in range(1,c-1):

            if vars[i][j].get()==1:
                c1[i][j].select()
            else:
                c1[i][j].deselect()

            alive_n=0
            
            for r_num in range(-1,2):
                for c_num in range(-1,2):
                    if vars[i+r_num][j+c_num].get()==1:
                        alive_n+=vars[i+r_num][j+c_num].get()
            
            alive_n-=vars[i][j].get()
            
            
            if(vars[i][j].get()==1 and alive_n<2):
                vars_new[i][j]=tk.IntVar(root,value=0)
            elif(vars[i][j].get()==1 and alive_n>3):
                vars_new[i][j]=tk.IntVar(root,value=0)
            elif(vars[i][j].get()==0 and alive_n==3):
                vars_new[i][j]=tk.IntVar(root,value=1)
            else:
                vars_new[i][j]=tk.IntVar(root,value=vars[i][j].get())
            
            #print(alive_n,'i-j',i,j,vars[i][j].get(),vars_new[i][j].get())
    print    
    vars=vars_new
  
    root.after(1000,lambda: produce_next_gen(vars,c1))


def draw(vars):
    

    for i1 in range(r):
        c1_temp=[]
        for j1 in range(c):
            l1 = tk.Checkbutton(root, width='3',variable=vars[i1][j1],onvalue=1, offvalue=0)
            l1.grid(row=i1,column=j1)
            c1_temp.append(l1)
        c1.append(c1_temp)
    bu=tk.Button(root, width='3',text='Finish',command=root.destroy).grid(rows=r,column=c-1)
   
    
    produce_next_gen(vars,c1)
    



   
vars=getvars(data,r,c)
draw(vars)

root.mainloop()
#produce_next_gen(vars,num)



