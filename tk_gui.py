import tkinter as tk

app = tk.Tk()
app.title("警告")
app.geometry("500x500")

# 添加 label
lb = tk.Label(app, text="你被绿了", width="20", height="10", fg="green")
lb.pack()

# 添加 label2  1-9乘法表
txt = "\n".join([' '.join(['%sx%s=%s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)])
lb2 = tk.Label(app, text = txt)
lb2.pack()

def change_label():
    lb.config(text = "对不起，我错了", fg="black")
# 添加 button
bt = tk.Button(text="滚", width="10", bg="pink", command=change_label)
bt.pack()

tk.mainloop()