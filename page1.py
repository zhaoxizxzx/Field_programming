from tkinter import *

root = Tk()
root.geometry('460x240')
root.title('自动转换大小写')
root.configure(bg='#F2F2F2')
lb1 = Label(root, text='请输入一串大写或小写数字：',font=('楷体',13))
lb1.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

# 调用转换函数
btn1 = Button(root, text='转换',font=('楷体',12),bg='#DFDFDF')
btn1.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root,bg='#FFFFFF')
txt.place(rely=0.6, relheight=0.4)

root.mainloop()