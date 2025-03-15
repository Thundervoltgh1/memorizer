from tkinter import*
from tkinter.filedialog import*
root=Tk()
root.title("memorizer")

def add_item():
    listbox.insert(END,item.get())
    item.delete(0,END)

def delete_item():
    index=listbox.curselection()
    if index:
        listbox.delete(index)

def open_file():
    f=askopenfile(title="open_file")                   
    if f is not None:
        listbox.delete(0,END)
        items=f.readlines()
        for item in items:
            listbox.insert(END,item.strip())

def save_file():
    f1=asksaveasfile(defaultextension=".txt")
    if f1 is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=f1)
        listbox.delete(0,END)

open=Button(root,text="Open",width=10,command=open_file)
open.pack(side=LEFT,padx=5,pady=5)
delete=Button(root,text="Delete",width=10,command=delete_item)
delete.pack(side=RIGHT,padx=5,pady=5)
save=Button(root,text="Save",width=10,command=save_file)
save.pack(padx=5,pady=5)
add=Button(root,text="Add",width=10,command=add_item)
add.pack(padx=5,pady=5)
item=Entry(root,width=20)
item.pack(padx=5,pady=5)
frame=Frame(root)
scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar2=Scrollbar(frame,orient="horizontal")
scrollbar2.pack(side=BOTTOM,fill=X)
listbox=Listbox(frame,width=30,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar2.set,bg="cyan")

for i in range(1,10):
    listbox.insert(END,"eniola"+str(i))
    
listbox.pack(side=LEFT,padx=5,pady=5)
scrollbar.config(command=listbox.yview)
scrollbar2.config(command=listbox.xview)
frame.pack(side=RIGHT)

root.mainloop()
