import tkinter
from tkinter import ttk
from modules import fanwei
from modules import lanling
from modules import yongyou
from modules import zhiyuan

windows = tkinter.Tk()
windows.title("OA综合利用工具1.3  By lnsmile！")
windows.geometry('800x500')
windows.resizable(0,0)
images =tkinter.PhotoImage(file='.\\images\\1.jpg')
windows.iconphoto(False,images)

l = tkinter.Label(windows,text="Url:",width=5,height=2,justify='left')
l.place(x=0,y=5)

cv = tkinter.StringVar()
e = tkinter.Entry(windows,show = None,justify = 'left',bd=2,textvariable=cv)
e.place(x=45,y=10,width=200,height=32)

cho = ttk.Combobox(windows,values=['泛微OA','用友OA','致远OA','蓝凌OA'],state='readonly')
cho.place(x=260,y=10,width=200,height=32)
cho.current(0) #设置默认为第一个泛微OA
t = tkinter.Text(windows)
t.place(x=18,y=100,width=763,height=350)

def func(event):
	if cho.get() =="泛微OA" and e.get() !='':
		t.delete('1.0','end')
		res = fanwei.run(e.get())
		t.insert('insert',"开始检测泛微OA ..."+"\n")
		#泛微poc1
		t.insert('insert',str(res[0])+"\n"+"\n")
		#泛微poc2
		t.insert('insert',str(res[1])+"\n"+"\n")
		#泛微poc3
		t.insert('insert',str(res[2])+"\n"+"\n")		
		#泛微poc4
		t.insert('insert',str(res[3])+"\n"+"\n")		
		#泛微poc5
		t.insert('insert',str(res[4])+"\n"+"\n")	


	if cho.get() =="致远OA" and e.get() !='':
		t.delete('1.0','end')
		res = zhiyuan.run(e.get())
		t.insert('insert',"开始检测致远OA ..."+"\n")
		t.insert('insert',str(res[0])+"\n"+"\n")
		t.insert('insert',str(res[1])+"\n"+"\n")
		t.insert('insert',str(res[2])+"\n"+"\n")
		t.insert('insert',str(res[3])+"\n"+"\n")
		t.insert('insert',str(res[4])+"\n"+"\n")
		t.insert('insert',str(res[5])+"\n"+"\n")
		t.insert('insert',str(res[6])+"\n"+"\n")
		t.insert('insert',str(res[7])+"\n"+"\n")

	if cho.get() =="用友OA" and e.get() !='':
		t.delete('1.0','end')
		res = yongyou.run(e.get())
		t.insert('insert',"开始检测用友OA ..."+"\n")
		t.insert('insert',str(res[0])+"\n"+"\n")
		t.insert('insert',str(res[1])+"\n"+"\n")
		t.insert('insert',str(res[2])+"\n"+"\n")
		t.insert('insert',str(res[3])+"\n"+"\n")
		t.insert('insert',str(res[4])+"\n"+"\n")
		t.insert('insert',str(res[5])+"\n"+"\n")

	if cho.get() =="蓝凌OA" and e.get() !='':
		t.delete('1.0','end')
		res = lanling.runall(e.get())
		t.insert('insert',"开始检测蓝凌OA ..."+"\n")
		t.insert('insert',str(res)+"\n"+"\n")


b1 = tkinter.Button(windows,text='Start',width=4,height=0)
b1.place(x=500,y=10)
b1.bind("<Button-1>",func)
windows.mainloop()
