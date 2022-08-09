from tkinter import *
from tkinter import font

root = Tk()
root.title("Lee's Hospital")
root.minsize(height=900, width=1600)
root.geometry("+160+36")

frame1 = Frame(root, relief="solid", bd=2)
frame1.pack(side="top", padx=5, fill="both")
label_title = Label(frame1, text="환자 관리 시스템", font=("맑은고딕", 25))
label_title.pack(pady=5)

def tab1():        
    label_id = Label(frame3, text="환자 등록번호", font=("맑은고딕", 15))
    label_id.grid(row=0, column=0)
    label_id_entry = Entry(frame3)
    label_id_entry.grid(row=0, column=1)

    button_submit_tab1 = Button(frame4, text="등록", font=("맑은고딕", 20), width=20)
    button_submit_tab1.grid(row=0, column=0)
def tab2():
    label_id = Label(frame3, text="환자 정보 삭제", font=("맑은고딕", 15))
    label_id.grid(row=0, column=0)
    label_id_entry = Entry(frame3)
    label_id_entry.grid(row=0, column=1)

frame2 = Frame(root, relief="solid", bd=2)
frame2.pack(side="top", padx=5, pady=5, fill="both")
button_show_enroll = Button(frame2, text="환자 정보 등록", font=("맑은고딕", 15), command=tab1)
button_show_enroll.pack(side="left")
button_show_del = Button(frame2, text="환자 정보 삭제", font=("맑은고딕", 15), command=tab2)
button_show_del.pack(side="left")  

frame3 = Frame(root, relief="solid", bd=2)
frame3.pack(fill="both", padx=5)
frame4 = Frame(root, relief="solid", bd=2)
frame4.columnconfigure(0, weight=1)
frame4.rowconfigure(0, weight=1)
frame4.pack(side="bottom", fill="both", padx=5, pady=5)

root.mainloop()

# from cmath import exp
# from re import X
# import tkinter as tk
# import tkinter.font as tkFont

# win = tk.Tk()

# win.title("LeeHospital")
# win.geometry("1600x900+160+36")
# win.resizable(False, False)
# win.option_add("*Font", "맑은고딕 25")

# frame1 = tk.Frame(win, relief="solid", bd=2)
# frame1.pack(side="top", fill="x")
# frame2 = tk.Frame(win, relief="solid", bd=2)
# frame2.pack(side="top", fill="x", pady=2)
# frame3 = tk.Frame(win, relief="solid", bd=2)
# frame3.pack(side="top", fill="x", pady=2)

# def changepage(pagenum):
#     if pagenum == 1:
#         label=tk.Label(frame3, text="환자 정보 등록")
#     elif pagenum == 2:
#         label=tk.Label(frame3, text="환자 정보 삭제")
#     label.pack()

# label=tk.Label(frame1, text="LeeHospital 환자 관리 시스템")
# label['font'] = tkFont.Font(family="맑은고딕", size=30)
# label.pack()

# btn_add = tk.Button(frame2, text="환자 정보 등록")
# btn_add.config(command=changepage(1))
# btn_del = tk.Button(frame2, text="환자 정보 삭제")
# btn_del.config(command=changepage(2))
# btn_add.pack(side=tk.LEFT)
# btn_del.pack(side=tk.LEFT)

# win.mainloop()

