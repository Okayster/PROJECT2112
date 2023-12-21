import os
from tkinter import *
from tkinter import ttk
#RAID 5 = S*(N-1)
#RAID 0 = N * S
#RAID 1+0 = (S*N)/2
#RAID 1 = S
def RAID_0():
     def answer0():
          N = DiskNumberEntry.get()
          Nn = int(N)
          numberdisk4 = (Nn * 3)
          numberdisk3 = (Nn * 2)
          numberdisk2 = Nn
          numberdisk = 1
          cordx = 50
          cordy = 100
          cordx1 = 110
          cordy1 = 200
          S = MinimumDiskSizeEntry.get()
          Answer = int(N)*int(S)
          Answer0Window = Canvas(bg = "white", width=(Nn*70)+120, height=250)
          Answer0Window.pack(anchor=CENTER, expand=0)
          Answer0Output = Label(Answer0Window, text = 'Ответ(Гб) - ', bg='white', font = 'Arial 15 bold').place(x = 0, y = 50)
          Answer0Output = Label(Answer0Window, text = Answer, bg = 'white', font = 'Arial 15 bold').place(x = 110, y = 50)
          Answer0Output = Label(Answer0Window, text = 'Гб', bg = 'white', font = 'Arial 15 bold').place(x = 15, y = 205)
          Answer0Output = Label(Answer0Window, text = S, bg='white',font = 'Arial 15 bold').place(x = cordx, y = 205)
          ExitButton = ttk.Button(Answer0Window, text="Закрыть", command=lambda: Answer0Window.destroy()).place(x = (Nn*70+100)-80, y = 0)
          while int(Nn) != 0:
               Answer0Window.create_rectangle(cordx, cordy, cordx1, cordy1)
               Answer0Window.create_line(cordx, 115, cordx1, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 102)
               Answer0Output = Label(Answer0Window, text = numberdisk, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
               numberdisk += 1
               numberdisk2 += 1
               Answer0Window.create_line(cordx, 130, cordx1, 130)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 117)
               Answer0Output = Label(Answer0Window, text = numberdisk2, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
               numberdisk3 += 1
               Answer0Window.create_line(cordx, 145, cordx1, 145)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 132)
               Answer0Output = Label(Answer0Window, text = numberdisk3, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
               numberdisk4 += 1
               Answer0Window.create_line(cordx, 160, cordx1, 160)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 147)
               Answer0Output = Label(Answer0Window, text = numberdisk4, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
               cordx += 70
               cordx1 += 70
               Nn = int(Nn)-1
     def checknum():
          N = DiskNumberEntry.get()
          S = MinimumDiskSizeEntry.get()
          try:
               Nn = int(N)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 60)
          try:
               Ss = int(S)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 100)
          znach = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
          if Nn in znach:
               answer0()
               ZeroWindow.destroy()
          else:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите правильные значения",fg='red').place(x = 40, y = 200)
     ZeroWindow = Tk()
     ZeroWindow.geometry("450x300")
     ZeroWindow.resizable(0,0)
     DiskNumberAsk = Label(ZeroWindow, text = "Количество дисков (от 2 до 20)").place(x = 40, y = 60)
     MinimumDiskSizeAsk = Label(ZeroWindow, text = "Минимальный объём диска").place(x = 40, y = 100)
     DiskNumberEntry = ttk.Entry(ZeroWindow, width = 3)
     DiskNumberEntry.place(x=220, y = 60)
     MinimumDiskSizeEntry = ttk.Entry(ZeroWindow, width = 10)
     MinimumDiskSizeEntry.place(x=220, y = 100)
     SubmitButton = Button(ZeroWindow, text = 'Бахнуть литруху Жигулёвского', command=checknum).place(x=40, y = 130)
def RAID_1():
     def answer0():
          N = DiskNumberEntry.get()
          Nn = int(N)
          numberdisk = 1
          cordx = 50
          cordy = 100
          cordx1 = 110
          cordy1 = 200
          S = MinimumDiskSizeEntry.get()
          Answer = int(S)
          Answer0Window = Canvas(bg = "white", width=(Nn*70)+120, height=250)
          Answer0Window.pack(anchor=CENTER, expand=0)
          Answer0Output = Label(Answer0Window, text = 'Ответ(Гб) - ', bg='white', font = 'Arial 15 bold').place(x = 0, y = 50)
          Answer0Output = Label(Answer0Window, text = Answer, bg = 'white', font = 'Arial 15 bold').place(x = 110, y = 50)
          Answer0Output = Label(Answer0Window, text = 'Гб', bg = 'white', font = 'Arial 15 bold').place(x = 15, y = 205)
          Answer0Output = Label(Answer0Window, text = S, bg='white',font = 'Arial 15 bold').place(x = cordx, y = 205)
          ExitButton = ttk.Button(Answer0Window, text="Закрыть", command=lambda: Answer0Window.destroy()).place(x = (Nn*70+100)-80, y = 0)
          while int(Nn) != 0:
               Answer0Window.create_rectangle(cordx, cordy, cordx1, cordy1)
               Answer0Window.create_line(cordx, 115, cordx1, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 102)
               Answer0Output = Label(Answer0Window, text = 1, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
               Answer0Window.create_line(cordx, 130, cordx1, 130)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 117)
               Answer0Output = Label(Answer0Window, text = 2, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
               Answer0Window.create_line(cordx, 145, cordx1, 145)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 132)
               Answer0Output = Label(Answer0Window, text = 3, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
               Answer0Window.create_line(cordx, 160, cordx1, 160)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 147)
               Answer0Output = Label(Answer0Window, text = 4, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
               cordx += 70
               cordx1 += 70
               Nn = int(Nn)-1
     def checknum():
          N = DiskNumberEntry.get()
          S = MinimumDiskSizeEntry.get()
          try:
               Nn = int(N)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 60)
          try:
               Ss = int(S)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 100)
          znach = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
          if Nn in znach:
               answer0()
               ZeroWindow.destroy()
          else:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите правильные значения",fg='red').place(x = 40, y = 200)
     ZeroWindow = Tk()
     ZeroWindow.geometry("450x300")
     ZeroWindow.resizable(0,0)
     DiskNumberAsk = Label(ZeroWindow, text = "Количество дисков (от 2 до 20)").place(x = 40, y = 60)
     MinimumDiskSizeAsk = Label(ZeroWindow, text = "Минимальный объём диска").place(x = 40, y = 100)
     DiskNumberEntry = ttk.Entry(ZeroWindow, width = 3)
     DiskNumberEntry.place(x=220, y = 60)
     MinimumDiskSizeEntry = ttk.Entry(ZeroWindow, width = 10)
     MinimumDiskSizeEntry.place(x=220, y = 100)
     SubmitButton = Button(ZeroWindow, text = 'Бахнуть литруху Жигулёвского', command=checknum).place(x=40, y = 130)
def RAID_5():
     def answer0():
          N = DiskNumberEntry.get()
          Nn = int(N)
          NNN = int(N)
          numstep = 0
          controlbit = 1
          Acheck = [0,1,5,9,13,17]
          Bcheck = [2,6,10,14,18,22,26,30,34,38]
          Ccheck = [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59]
          Dcheck = [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80]
          numberdisk4 = (Nn * 3)+1
          numberdisk3 = (Nn * 2)+1
          numberdisk2 = Nn+1
          numberdisk = 1
          vnumberdisk4 = (Nn * 3)
          vnumberdisk3 = (Nn * 2)
          vnumberdisk2 = Nn
          vnumberdisk = 1
          cordx = 50
          cordy = 100
          cordx1 = 110
          cordy1 = 200
          S = MinimumDiskSizeEntry.get()
          Answer = int(N)*int(S)
          Answer0Window = Canvas(bg = "white", width=(Nn*70)+120, height=250)
          Answer0Window.pack(anchor=CENTER, expand=0)
          Answer0Output = Label(Answer0Window, text = 'Ответ(Гб) - ', bg='white', font = 'Arial 15 bold').place(x = 0, y = 50)
          Answer0Output = Label(Answer0Window, text = Answer, bg = 'white', font = 'Arial 15 bold').place(x = 110, y = 50)
          Answer0Output = Label(Answer0Window, text = 'Гб', bg = 'white', font = 'Arial 15 bold').place(x = 15, y = 205)
          Answer0Output = Label(Answer0Window, text = S, bg='white',font = 'Arial 15 bold').place(x = cordx, y = 205)
          ExitButton = ttk.Button(Answer0Window, text="Закрыть", command=lambda: Answer0Window.destroy()).place(x = (Nn*70+100)-80, y = 0)
          while int(Nn) != 0:
               Answer0Window.create_rectangle(cordx, cordy, cordx1, cordy1)
               Answer0Window.create_line(cordx, 115, cordx1, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 102)
               if int(numberdisk) in Acheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
                    vnumberdisk += 1
               numberdisk += 1
               Answer0Window.create_line(cordx, 130, cordx1, 130)
               Answer0Output = Label(Answer0Window, text = 'B', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 117)
               if int(numberdisk2) in Bcheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk2, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
                    vnumberdisk2 += 1
               numberdisk2 += 1
               Answer0Window.create_line(cordx, 145, cordx1, 145)
               Answer0Output = Label(Answer0Window, text = 'C', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 132)
               if int(numberdisk3) in Ccheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk3, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
                    vnumberdisk3 += 1
               numberdisk3 += 1
               Answer0Window.create_line(cordx, 160, cordx1, 160)
               Answer0Output = Label(Answer0Window, text = 'D', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 147)
               if int(numberdisk4) in Dcheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk4, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
                    vnumberdisk4 += 1
               numberdisk4 += 1
               cordx += 70
               cordx1 += 70
               Nn = int(Nn)-1
     def checknum():
          N = DiskNumberEntry.get()
          S = MinimumDiskSizeEntry.get()
          try:
               Nn = int(N)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 60)
          try:
               Ss = int(S)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 100)
          znach = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
          if Nn in znach:
               answer0()
               ZeroWindow.destroy()
          else:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите правильные значения",fg='red').place(x = 40, y = 200)
     ZeroWindow = Tk()
     ZeroWindow.geometry("450x300")
     ZeroWindow.resizable(0,0)
     DiskNumberAsk = Label(ZeroWindow, text = "Количество дисков (от 3 до 20)").place(x = 40, y = 60)
     MinimumDiskSizeAsk = Label(ZeroWindow, text = "Минимальный объём диска").place(x = 40, y = 100)
     DiskNumberEntry = ttk.Entry(ZeroWindow, width = 3)
     DiskNumberEntry.place(x=220, y = 60)
     MinimumDiskSizeEntry = ttk.Entry(ZeroWindow, width = 10)
     MinimumDiskSizeEntry.place(x=220, y = 100)
     SubmitButton = Button(ZeroWindow, text = 'Бахнуть литруху Жигулёвского', command=checknum).place(x=40, y = 130)
def RAID_50():
     def answer0():
          N = DiskNumberEntry.get()
          Nn = int(N)
          Acheck = [3,6,9,12,15,18]
          Bcheck = [1,4,7,10,13,16,19]
          Ccheck = [2,5,8,11,14,17]
          Dcheck = [3,6,9,12,15,18]
          numberdisk4 = 1
          numberdisk3 = 1
          numberdisk2 = 1
          numberdisk = 1
          vnumberdisk4 = 1
          vnumberdisk3 = 1
          vnumberdisk2 = 1
          vnumberdisk = 1
          cordx = 50
          cordy = 100
          cordx1 = 110
          cordy1 = 200
          S = MinimumDiskSizeEntry.get()
          Answer = (int(N)-1)*int(S)
          Answer0Window = Canvas(bg = "white", width=(Nn*70)+75, height=250)
          width=((Nn*70)+75)
          Nn = int(N)
          Answer0Window.pack(anchor=CENTER, expand=0)
          Answer0Output = Label(Answer0Window, text = 'Ответ(Гб) - ', bg='white', font = 'Arial 15 bold').place(x = 0, y = 50)
          Answer0Output = Label(Answer0Window, text = Answer, bg = 'white', font = 'Arial 15 bold').place(x = 110, y = 50)
          Answer0Output = Label(Answer0Window, text = 'Гб', bg = 'white', font = 'Arial 15 bold').place(x = 15, y = 205)
          Answer0Output = Label(Answer0Window, text = S, bg='white',font = 'Arial 15 bold').place(x = cordx, y = 205)
          ExitButton = ttk.Button(Answer0Window, text="Закрыть", command=lambda: Answer0Window.destroy()).place(x = width-80, y = 0)
          while int(Nn) != 0:
               Answer0Window.create_rectangle(cordx, cordy, cordx1, cordy1)
               Answer0Window.create_line(cordx, 115, cordx1, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 102)
               if int(numberdisk) in Acheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
                    vnumberdisk += 1
               numberdisk += 1
               Answer0Window.create_line(cordx, 130, cordx1, 130)
               Answer0Output = Label(Answer0Window, text = 'B', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 117)
               if int(numberdisk2) in Bcheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk2, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
                    vnumberdisk2 += 1
               numberdisk2 += 1
               Answer0Window.create_line(cordx, 145, cordx1, 145)
               Answer0Output = Label(Answer0Window, text = 'C', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 132)
               if int(numberdisk3) in Ccheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk3, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
                    vnumberdisk3 += 1
               numberdisk3 += 1
               Answer0Window.create_line(cordx, 160, cordx1, 160)
               Answer0Output = Label(Answer0Window, text = 'D', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 147)
               if int(numberdisk4) in Dcheck:
                    Answer0Output = Label(Answer0Window, text = 'p', bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
               else:
                    Answer0Output = Label(Answer0Window, text = vnumberdisk4, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
                    vnumberdisk4 += 1
               numberdisk4 += 1
               cordx += 70
               cordx1 += 70
               Nn = int(Nn)-1
     def checknum():
          N = DiskNumberEntry.get()
          S = MinimumDiskSizeEntry.get()
          try:
               Nn = int(N)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 60)
          try:
               Ss = int(S)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 100)
          znach = [6,9,12,15,18]
          if Nn in znach:
               answer0()
               ZeroWindow.destroy()
          else:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите правильные значения",fg='red').place(x = 40, y = 200)
     ZeroWindow = Tk()
     ZeroWindow.geometry("450x300")
     ZeroWindow.resizable(0,0)
     DiskNumberAsk = Label(ZeroWindow, text = "Количество дисков (Кратное 3. От 6 до 18)").place(x = 40, y = 60)
     MinimumDiskSizeAsk = Label(ZeroWindow, text = "Минимальный объём диска").place(x = 40, y = 100)
     DiskNumberEntry = ttk.Entry(ZeroWindow, width = 3)
     DiskNumberEntry.place(x=280, y = 60)
     MinimumDiskSizeEntry = ttk.Entry(ZeroWindow, width = 10)
     MinimumDiskSizeEntry.place(x=220, y = 100)
     SubmitButton = Button(ZeroWindow, text = 'Бахнуть литруху Жигулёвского', command=checknum).place(x=40, y = 130)
def RAID_10():
     def answer0():
          N = DiskNumberEntry.get()
          Nn = int(N)
          numberdisk4 = (Nn * 3)
          numberdisk3 = (Nn * 2)
          numberdisk2 = Nn
          numberdisk = 1
          cordx = 50
          cordy = 100
          cordx1 = 110
          cordy1 = 200
          S = MinimumDiskSizeEntry.get()
          Answer = int(N)*int(S)
          Answer0Window = Canvas(bg = "white", width=(Nn*70)+75, height=250)
          width=((Nn*70)+75)
          Nn = int(N)/2
          Nn = int(Nn)
          Answer0Window.pack(anchor=CENTER, expand=0)
          Answer0Output = Label(Answer0Window, text = 'Ответ(Гб) - ', bg='white', font = 'Arial 15 bold').place(x = 0, y = 50)
          Answer0Output = Label(Answer0Window, text = Answer, bg = 'white', font = 'Arial 15 bold').place(x = 110, y = 50)
          Answer0Output = Label(Answer0Window, text = 'Гб', bg = 'white', font = 'Arial 15 bold').place(x = 15, y = 205)
          Answer0Output = Label(Answer0Window, text = S, bg='white',font = 'Arial 15 bold').place(x = cordx, y = 205)
          ExitButton = ttk.Button(Answer0Window, text="Закрыть", command=lambda: Answer0Window.destroy()).place(x = width-80, y = 0)
          while int(Nn) != 0:
               Answer0Window.create_rectangle(cordx, cordy, cordx1, cordy1)
               Answer0Window.create_rectangle(cordx+65, cordy, cordx1+65, cordy1)
               Answer0Window.create_line(cordx, 115, cordx1, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 102)
               Answer0Output = Label(Answer0Window, text = numberdisk, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 102)
               Answer0Window.create_line(cordx+65, 115, cordx1+65, 115)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+90, y = 102)
               Answer0Output = Label(Answer0Window, text = numberdisk, bg = 'white', font = 'Arial 5').place(x = cordx+97, y = 102)
               numberdisk += 1
               numberdisk2 += 1
               Answer0Window.create_line(cordx, 130, cordx1, 130)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 117)
               Answer0Output = Label(Answer0Window, text = numberdisk2, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 117)
               Answer0Window.create_line(cordx+65, 130, cordx1+65, 130)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+90, y = 117)
               Answer0Output = Label(Answer0Window, text = numberdisk2, bg = 'white', font = 'Arial 5').place(x = cordx+97, y = 117)
               numberdisk3 += 1
               Answer0Window.create_line(cordx, 145, cordx1, 145)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 132)
               Answer0Output = Label(Answer0Window, text = numberdisk3, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 132)
               Answer0Window.create_line(cordx+65, 145, cordx1+65, 145)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+90, y = 132)
               Answer0Output = Label(Answer0Window, text = numberdisk3, bg = 'white', font = 'Arial 5').place(x = cordx+97, y = 132)
               numberdisk4 += 1
               Answer0Window.create_line(cordx, 160, cordx1, 160)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+25, y = 147)
               Answer0Output = Label(Answer0Window, text = numberdisk4, bg = 'white', font = 'Arial 5').place(x = cordx+32, y = 147)
               Answer0Window.create_line(cordx+65, 160, cordx1+65, 160)
               Answer0Output = Label(Answer0Window, text = 'A', bg = 'white', font = 'Arial 5').place(x = cordx+90, y = 147)
               Answer0Output = Label(Answer0Window, text = numberdisk4, bg = 'white', font = 'Arial 5').place(x = cordx+97, y = 147)
               cordx += 135
               cordx1 += 135
               Nn = int(Nn)-1
     def checknum():
          N = DiskNumberEntry.get()
          S = MinimumDiskSizeEntry.get()
          try:
               Nn = int(N)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 60)
          try:
               Ss = int(S)
          except:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите число", fg='Red').place(x = 300, y = 100)
          znach = [4,6,8,10,12,14,16,18,20]
          if Nn in znach:
               answer0()
               ZeroWindow.destroy()
          else:
               DiskSizeError = Label(ZeroWindow, text = "Ахтунг, введите правильные значения",fg='red').place(x = 40, y = 200)
     ZeroWindow = Tk()
     ZeroWindow.geometry("450x300")
     ZeroWindow.resizable(0,0)
     DiskNumberAsk = Label(ZeroWindow, text = "Количество дисков (Кратное 2. От 4 до 20)").place(x = 40, y = 60)
     MinimumDiskSizeAsk = Label(ZeroWindow, text = "Минимальный объём диска").place(x = 40, y = 100)
     DiskNumberEntry = ttk.Entry(ZeroWindow, width = 3)
     DiskNumberEntry.place(x=280, y = 60)
     MinimumDiskSizeEntry = ttk.Entry(ZeroWindow, width = 10)
     MinimumDiskSizeEntry.place(x=220, y = 100)
     SubmitButton = Button(ZeroWindow, text = 'Бахнуть литруху Жигулёвского', command=checknum).place(x=40, y = 130)
def main():
     root = Tk()
     root.geometry('1650x500')
     root.resizable(0, 0)
     Welcome = Label(root, font = 'Arial 60 bold', text = "ЗДРАВСТВУЙТЕ", compound=(CENTER)).place(x=500, y = 0)
     Welcome1 = Label(root, font = 'Arial 30 bold', text = "Выберите тип RAID").place(x=600, y = 100)
     btnRAID0 = Button(root, height=5, text='RAID0', font='Arial 15 bold', compound=LEFT, command=RAID_0).place(x=100, y = 210)
     btnRAID1 = Button(root, height=5, text='RAID1', font='Arial 15 bold', compound=LEFT, command=RAID_1).place(x=400, y = 210)
     btnRAID5 = Button(root, height=5, text='RAID5', font='Arial 15 bold', compound=LEFT, command=RAID_5).place(x=700, y = 210)
     btnRAID10 = Button(root, height=5, text='RAID 1+0', font='Arial 15 bold', compound=LEFT, command=RAID_10).place(x=1000, y = 210)
     btnRAID50 = Button(root, height=5, text='RAID 5+0', font='Arial 15 bold', compound=LEFT, command=RAID_50).place(x=1300, y = 210)
     root.mainloop()

main()
print(os.listdir())
os.system('cls')