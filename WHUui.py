from tkinter import *
from tkinter.messagebox import showerror, showinfo
from WHUqk import WHU
from PIL import Image, ImageTk
from PIL import *
from WHUerror import *


class QkUi:
    def __init__(self):
        self.is_setted = False

        self.root = Tk()
        self.root.title(('Anti-WHU-ISE'))
        self.root.geometry('512x256')
        self.root.resizable(False, False)

        self.stuIdLabel = Label(master=self.root)
        self.stuIdEntry = Entry(master=self.root)
        self.pwdLabel = Label(master=self.root)
        self.pwdEntry = Entry(master=self.root, show='*')
        self.leftBtn = Button(master=self.root)

        self.infoList = Listbox(master=self.root)

        self.rightLabel1 = Label(master=self.root)
        self.rightLabel2 = Label(master=self.root)

        self.rightList1 = Listbox(master=self.root)
        self.rightList2 = Listbox(master=self.root)

        self.rightEntry1 = Entry(master=self.root)
        self.rightEntry2 = Entry(master=self.root)

        self.rightBtnDel1 = Button(master=self.root)
        self.rightBtnDel2 = Button(master=self.root)
        self.rightBtnAdd1 = Button(master=self.root)
        self.rightBtnAdd2 = Button(master=self.root)

        self.rightEntry3 = Entry(master=self.root)
        self.rightEntry4 = Entry(master=self.root)
        self.rightLabel3 = Label(master=self.root)
        self.rightLabel4 = Label(master=self.root)

        self.rightImg1 = Button(master=self.root)
        self.rightImg2 = Button(master=self.root)

        self.rightBtn1 = Button(master=self.root)
        self.rightBtn2 = Button(master=self.root)

        self.stuIdLabel.config(
            {
                'text': '学号',
                'width': 5,
            }
        )
        self.stuIdEntry.config(
            {
                'width': 16,
                'bd': 1,
            }
        )
        self.pwdLabel.config(
            {
                'text': '密码',
                'width': 5,
            }
        )
        self.pwdEntry.config(
            {
                'width': 16,
                'bd': 1,
            }
        )
        self.leftBtn.config(
            {
                'text': '确认',
                'bd': 1,
                'command': self.leftBtnCmd,
                'width': 5,
            }
        )

        self.infoList.config(
            {
                'bd': 0,
                'width': 17,
                'height': 5,
                'fg': 'red',
            }
        )

        self.rightLabel1.config(
            {
                'text': '公选',
                'bd': 1,
                'width': 5,
            }
        )
        self.rightLabel2.config(
            {
                'text': '公必',
                'bd': 1,
                'width': 5,
            }
        )

        self.rightEntry1.config(
            {
                'width': 16,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightEntry2.config(
            {
                'width': 16,
                'bd': 1,
                'state': 'disabled',
            }
        )

        self.rightList1.config(
            {
                'height': 5,
                'width': 16,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightList2.config(
            {
                'height': 5,
                'width': 16,
                'bd': 1,
                'state': 'disabled',
            }
        )

        self.rightBtnAdd1.config(
            {
                'text': '新增',
                'command': self.rightBtnAdd1Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightBtnAdd2.config(
            {
                'text': '新增',
                'command': self.rightBtnAdd2Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightBtnDel1.config(
            {
                'text': '删除',
                'command': self.rightBtnDel1Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightBtnDel2.config(
            {
                'text': '删除',
                'command': self.rightBtnDel2Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled',
            }
        )

        self.rightEntry3.config(
            {
                'width': 8,
                'bd': 1,
                'state': 'disabled',
            }
        )
        self.rightEntry4.config(
            {
                'width': 8,
                'bd': 1,
                'state': 'disabled',
            }
        )

        self.rightLabel3.config(
            {
                'text': '验证码',
                'bd': 1,
                'width': 5,
            }
        )
        self.rightLabel4.config(
            {
                'text': '验证码',
                'bd': 1,
                'width': 5,
            }
        )

        self.rightImg1.config(
            {
                'command': self.rightImg1Cmd,
                'bd': 0,
                'state': 'disabled',
                'text': '获取验证码',
            }
        )
        self.rightImg2.config(
            {
                'command': self.rightImg2Cmd,
                'bd': 0,
                'state': 'disabled',
                'text': '获取验证码',
            }
        )

        self.rightBtn1.config(
            {
                'text': '开始',
                'command': self.rightBtn1Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled'
            }
        )
        self.rightBtn2.config(
            {
                'text': '开始',
                'command': self.rightBtn2Cmd,
                'width': 5,
                'bd': 1,
                'state': 'disabled'
            }
        )

        self.stuIdLabel.place(x=0, y=0)
        self.stuIdEntry.place(x=1, y=30)
        self.pwdLabel.place(x=0, y=60)
        self.pwdEntry.place(x=1, y=90)
        self.leftBtn.place(x=64, y=120)

        self.infoList.place(x=1, y=155)

        self.rightLabel1.place(x=128, y=4)
        self.rightLabel2.place(x=128, y=132)

        self.rightList1.place(x=128, y=32)
        self.rightList2.place(x=128, y=160)

        self.rightEntry1.place(x=256, y=32)
        self.rightEntry2.place(x=256, y=160)

        self.rightBtnDel1.place(x=260, y=64)
        self.rightBtnAdd1.place(x=320, y=64)

        self.rightBtnDel2.place(x=260, y=192)
        self.rightBtnAdd2.place(x=320, y=192)

        self.rightLabel3.place(x=400, y=4)
        self.rightEntry3.place(x=400, y=32)
        self.rightLabel4.place(x=400, y=132)
        self.rightEntry4.place(x=400, y=160)

        self.rightImg1.place(x=380, y=60)
        self.rightImg2.place(x=380, y=188)

        self.rightBtn1.place(x=420, y=96)
        self.rightBtn2.place(x=420, y=224)

    def leftActive(self):
        self.leftBtn.config(text='确认')
        self.stuIdEntry.config(state='normal')
        self.pwdEntry.config(state='normal')
        self.is_setted = False

    def leftDisabled(self):
        self.leftBtn.config(text='修改')
        self.stuIdEntry.config(state='disabled')
        self.pwdEntry.config(state='disabled')
        self.is_setted = True

    def rightActive1(self):
        self.rightList1.config(state='normal')
        self.rightEntry1.config(state='normal')
        self.rightEntry3.config(state='normal')
        self.rightBtnAdd1.config(state='active')
        self.rightBtnDel1.config(state='active')
        self.rightImg1.config(state='active')
        self.rightBtn1.config(state='active')

    def rightDisabled1(self):
        self.rightList1.config(state='disabled')
        self.rightEntry1.config(state='disabled')
        self.rightEntry3.config(state='disabled')
        self.rightBtnAdd1.config(state='disabled')
        self.rightBtnDel1.config(state='disabled')
        self.rightImg1.config(state='disabled')
        self.rightBtn1.config(state='disabled')

    def rightActive2(self):
        self.rightList2.config(state='normal')
        self.rightEntry2.config(state='normal')
        self.rightEntry4.config(state='normal')
        self.rightBtnAdd2.config(state='active')
        self.rightBtnDel2.config(state='active')
        self.rightImg2.config(state='active')
        self.rightBtn2.config(state='active')

    def rightDisabled2(self):
        self.rightList2.config(state='disabled')
        self.rightEntry2.config(state='disabled')
        self.rightEntry4.config(state='disabled')
        self.rightBtnAdd2.config(state='disabled')
        self.rightBtnDel2.config(state='disabled')
        self.rightImg2.config(state='disabled')
        self.rightBtn2.config(state='disabled')

    def leftBtnCmd(self):
        if not self.is_setted:
            self.pubWHU = WHU(self.stuIdEntry.get(), self.pwdEntry.get())
            self.pubRequiredWHU = WHU(
                self.stuIdEntry.get(), self.pwdEntry.get())
            self.leftDisabled()
            self.rightActive1()
            self.rightActive2()
            self.rightEntry3.delete(0, END)
            self.rightEntry4.delete(0, END)
        else:
            self.leftActive()
            self.rightDisabled1()
            self.rightDisabled2()

    def rightBtnAdd1Cmd(self):
        if self.rightEntry1.get():
            self.rightList1.insert(END, self.rightEntry1.get())
        self.rightEntry1.delete(0, END)

    def rightBtnAdd2Cmd(self):
        if self.rightEntry2.get():
            self.rightList2.insert(END, self.rightEntry2.get())
        self.rightEntry2.delete(0, END)

    def rightBtnDel1Cmd(self):
        self.rightList1.delete(ANCHOR)

    def rightBtnDel2Cmd(self):
        self.rightList2.delete(ANCHOR)

    def rightImg1Cmd(self):
        try:
            self.pubWHU.loadVerifyCodeImg('pcode.jpeg')
        except ServerError as error:
            self.infoList.insert(0, error)
        else:
            self.rightEntry3.delete(0, END)
            self.pcode = ImageTk.PhotoImage(Image.open('pcode.jpeg'))
            self.rightImg1.config(image=self.pcode)

    def rightImg2Cmd(self):
        try:
            self.pubRequiredWHU.loadVerifyCodeImg('prcode.jpeg')
        except ServerError as error:
            self.infoList.insert(0, error)
        else:
            self.rightEntry4.delete(0, END)
            self.prcode = ImageTk.PhotoImage(Image.open('prcode.jpeg'))
            self.rightImg2.config(image=self.prcode)

    def rightBtn1Cmd(self):
        #这两个按钮的事件可以改成无限循环，直到选课成功
        #但是要把对应的showinfo和showerror注释掉，防止弹出来一堆窗口
        self.pubWHU.setVerifyCode(self.rightEntry3.get())
        self.pubWHU.setCourses('pub', self.rightList1.get(0, END))
        self.pubWHU.startThread(name='公选')

    def rightBtn2Cmd(self):
        self.pubRequiredWHU.setVerifyCode(self.rightEntry4.get())
        self.pubRequiredWHU.setCourses(
            'pub_required', self.rightList2.get(0, END))
        self.pubRequiredWHU.startThread(name='公必')

    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    test = QkUi()
    test.mainloop()
