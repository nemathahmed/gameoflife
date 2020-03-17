import tkinter as tk
import time
import json
import os 


def takedata(root,vars,rows_no,columns_no):
    #print('insidetakedata')
    var_dict = {}
    for i in range(rows_no):
        for j in range(columns_no):
            var_dict.update({"R-%s,C-%s"%(i,j) : vars[i][j].get()})
    with open('var_dict.json', 'w') as outfile:
        json.dump(var_dict, outfile)

    root.destroy()
    
    os.system('python3 goi-play.py')

def create(ro,col):

    vars=[]
    rows_no=ro
    columns_no=col
    root=tk.Tk()
    root.title("Game of Life | Enter the desired pattern and click Play")
 

    
    for i in range(rows_no):
        var_temp=[]
        for j in range(columns_no):
            var_temp.append(tk.IntVar())
        vars.append(var_temp)



    for i in range(rows_no):
        for j in range(columns_no):
            c1 = tk.Checkbutton(root, width=3, variable=vars[i][j], onvalue=1, offvalue=0).grid(row=i,column=j)
        

    b=tk.Button(root, width=3, text="Play", command=lambda : takedata(root,vars,rows_no,columns_no)).grid(row=rows_no+1,column=columns_no-1)

    root.mainloop()

