from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

import tkinter.messagebox as msgBox


# =================== G L O B A L   V A R I A B L E ===========================================================================================

rowNum = 1

row1 = []
allCredit = []
allSubject = []
allLGrade = []
allHGrade = []
allNo = []

havingP = False
finalHighGPA = 0
finalLowGPA = 0

# ========================================================== Function ========================================================================= 

# ------------------------------------------------------- get grade point --------------------------------------------------------------------

def aPlus():
    return 4.5

def a():
    return 4.0

def bPlus():
    return 3.5

def b():
    return 3.0

def cPlus():
    return 2.5

def c():
    return 2.0

def dPlus():
    return 1.5

def d():
    return 1.0

def f():
    return 0.0

def p():
    return 0.0

def getGradePoint(inputGrade):
    switcher = {
        
        "A+": aPlus(),
        "A": a(),
        "B+": bPlus(),
        "B": b(),
        "C+": cPlus(),
        "C": c(),
        "D+": dPlus(),
        "D": d(),
        "F": f(),
        "P": p()
               
     }

    inputGrade = switcher.get(inputGrade)
    return inputGrade

# --------------------------------------------------------- calculation -----------------------------------------------------------------------

def calGPA():
    global allCredit
    global allLGrade
    global allHGrade
    global finalHighGPA
    global finalLowGPA
    global row1

    totalHCredit = 0
    totalLCredit = 0
    totalLGradePoint = 0
    totalHGradePoint = 0
    times = 0

    row1.clear()

    row1.append(credit.get())
    row1.append(lGrade.get())
    row1.append(hGrade.get())

    a = row1[0]
    b = row1[1]
    c = row1[2]

    intCredit = int(a)
    totalHCredit += intCredit
    totalLCredit += intCredit

    strLGrade = str(b)
    if (strLGrade=="P"):
        totalLCredit -= intCredit
    getLPoint = getGradePoint(strLGrade)
    times = intCredit * getLPoint
    totalLGradePoint += times

    strHGrade = str(c)
    if (strHGrade=="P"):
        totalHCredit -= intCredit
    getHPoint = getGradePoint(strHGrade)
    times = intCredit * getHPoint
    totalHGradePoint += times

    for i in allCredit:      
        getCredit = i.get()
        intCredit = int(getCredit)
        totalLCredit += intCredit
        totalHCredit += intCredit # here get the total amount of credit

        for j in allLGrade:           
            if(allCredit.index(i)==allLGrade.index(j)):
                getLGrade = j.get()
                strLGrade = str(getLGrade)
                if(strLGrade == "P"):
                    totalLCredit -= intCredit
                getLPoint = getGradePoint(strLGrade)
                times = intCredit * getLPoint
                totalLGradePoint += times

        for k in allHGrade:
            if(allCredit.index(i)==allHGrade.index(k)):
                getHGrade = k.get()
                strHGrade = str(getHGrade)
                if(strHGrade == "P"):
                    totalHCredit -= intCredit
                getHPoint = getGradePoint(strHGrade)
                times = intCredit * getHPoint
                totalHGradePoint += times

    finalHighGPA = round(totalHGradePoint / totalHCredit, 2)
    finalLowGPA = round(totalLGradePoint / totalLCredit, 2)

    print(f"Total lowest credit: {totalLCredit}")

    print(f"Total lowest grade point: {totalLGradePoint}")

    print(f"Total highest credit: {totalHCredit}")

    print(f"Total highest grade point: {totalHGradePoint}")

    refreshGPA()

# --------------------------------------------------------- refreshGPA --------------------------------------------------------------------------

def refreshGPA():
    hGpa['text']=(finalHighGPA)
    lGpa['text']=(finalLowGPA)

# --------------------------------------------------------- show Warning ----------------------------------------------------------------------

def warning(): 
    ans = msgBox.askquestion("Warning", "Do you want to clear ALL?")

    if ans == "yes":
        clearAll()
        msgBox.showinfo("Message", "All cleared!")

# ----------------------------------------------------- add and delete row ---------------------------------------------------------------------

def add():
    global rowNum
    global allCredit
    global allSubject
    global allLGrade
    global allHGrade
    global numBtn

    if(rowNum<7):
        rowNum += 1

        subject = Entry(rightBox, width=45)
        subject.grid(row=rowNum, column=1, padx= 5, pady=10)

        credit = Entry(rightBox, width=10, justify='center')
        credit.grid(row=rowNum, column=2, pady=5)

        lGrade = Entry(rightBox, width=10, justify='center')
        lGrade.grid(row=rowNum, column=3, pady=5)

        hGrade = Entry(rightBox, width=10, justify='center')
        hGrade.grid(row=rowNum, column=4, pady=5)

        allCredit.append(credit)
        allSubject.append(subject)
        allLGrade.append(lGrade)
        allHGrade.append(hGrade)

        no = Label(leftBar, text=rowNum, bg="#2bcbba", fg="#FFF", font=("consolas", 16, "bold"))
        no.grid(row=rowNum, pady=4)

        allNo.append(no)

def delete():
    global rowNum
    global numBtn
    global allCredit
    global allSubject
    global allLGrade
    global allHGrade
    
    if(rowNum!=1):
        a = rowNum-2
        for i in allSubject:
            if(allSubject.index(i)==a):
                i.destroy()
                allSubject.remove(i)

        for i in allCredit:
            if(allCredit.index(i)==a):
                i.destroy()
                allCredit.remove(i)

        for i in allLGrade:
            if(allLGrade.index(i)==a):
                i.destroy()
                allLGrade.remove(i)

        for i in allHGrade:
            if(allHGrade.index(i)==a):
                i.destroy()
                allHGrade.remove(i)

        for i in allNo:
            if(allNo.index(i)==a):
                i.destroy()
                allNo.remove(i)

        rowNum -= 1

def clearAll():

    global rowNum
    global allCredit
    global allSubject
    global allLGrade
    global allHGrade

    rowNum = 1

    for i in allCredit:
        i.destroy()

    allCredit.clear()

    for i in allSubject:
        i.destroy()

    allSubject.clear()

    for i in allLGrade:
        i.destroy()

    allLGrade.clear()

    for i in allHGrade:
        i.destroy()

    allHGrade.clear()

    for i in allNo:
        i.destroy()

    allNo.clear

# =========================================================== Window =================================================================

window = Tk()
window.title("GPA Calculator")
window.iconbitmap(r"D:\Media_inD\Document_inD\Programming\myProgram\python\GPA_cal\GPA_cal_v3.0\GPA_cal_icon.ico")

window.geometry('600x400') 
window.resizable(False, False)

window.configure(background="#d1d8e0")

# =========================================================== Menu Bar ==============================================================

menuBar = Menu(window)
window.config(menu=menuBar)

# File > New > Open > Save > Close
# Edit > Calculate > Clear All > Clear Selected

fileMenu = Menu(menuBar, bg="white")
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Close", command=window.quit)

editMenu = Menu(menuBar, bg="white")
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Calculate", command=calGPA)
editMenu.add_separator()
editMenu.add_command(label="Add", command=add)
editMenu.add_command(label="Delete", command=delete)
editMenu.add_command(label="Clear All", command=clearAll)

# ======================================================= Frame =====================================================================  

# ------------------ Frame ----------------------

topFrame = Frame(window, bg="#0fb9b1", borderwidth=2, padx=5, pady=5)
topFrame.pack(side=TOP, fill=X)

bottomFrame = Frame(window, bg="#778ca3")
bottomFrame.pack(side=BOTTOM, fill=X)

entryTitle = Frame(window, bg="#778ca3")
entryTitle.pack(side=TOP, fill=X)

titleFrame = Frame(window, bg="white")
titleFrame.pack(side=TOP, fill=X)

leftBar = Frame(window, bg="#2bcbba", width=50)
leftBar.pack(side=LEFT, fill=Y)

rightBox = Frame(window, bg="#d1d8e0")
rightBox.pack(side=TOP, fill=X)

# ====================================================== topFrame  ============================================================

plusImg = PhotoImage(file="D:\Media_inD\Document_inD\Programming\myProgram\python\GPA_cal\img\plus.png", width=20, height=20)
minusImg = PhotoImage(file="D:\Media_inD\Document_inD\Programming\myProgram\python\GPA_cal\img\minus.png", width=20, height=20)

plus = Button(topFrame, image=plusImg, bg="#2bcbba", fg="white", font=("Arial", 10, "bold"), command=add)
plus.pack(side=LEFT, padx=5)

minus = Button(topFrame, image=minusImg, bg="#2bcbba", fg="white", font=("Arial", 10), command=delete)
minus.pack(side=LEFT, padx=5)

calBtn = Button(topFrame, text="Calculate", bg="#2bcbba", fg="white", font=("Arial", 10, "bold"), command=calGPA)
calBtn.pack(side=LEFT, padx=5)

clearBtn = Button(topFrame, text="Clear All", bg="#2bcbba", fg="white", font=("Arial", 10, "bold"), command=warning)
clearBtn.pack(side=LEFT, padx=5)

# ====================================================== leftBar  ============================================================

no = Label(leftBar, text=rowNum, bg="#2bcbba", fg="#FFF", font=("consolas", 16, "bold"))
no.grid(row=1, pady=4)

# ==================================================== entryTitle (Frame) =======================================================

titleText = Label(entryTitle, text="Title: ", bg="#778ca3", fg="#FFF", font=("arial", 10, "bold"), pady=2)
titleText.grid(row=1, column=1, sticky=W)

titleEntry = Entry(entryTitle, bg="white", width=72, bd=1)
titleEntry.grid(row=1, column=2, sticky=W)

# =================================================== titleFrame  ===============================================================

hGradeText = Label(titleFrame , text="Highest \nGrade", width=8, padx=3,  bg="#FFF", fg="#a5b1c2", font=("arial", 10))
hGradeText.grid(row=1, column=5)

lGradeText = Label(titleFrame , text="Lowest \nGrade", width=8, padx=3, bg="#FFF", fg="#a5b1c2", font=("arial", 10))
lGradeText.grid(row=1, column=4)

creditText = Label(titleFrame , text="Credit", bg="#FFF", width=8, padx=3, fg="#a5b1c2", font=("arial", 10))
creditText.grid(row=1, column=3)

subjectText = Label(titleFrame , text="Subject", bg="#FFF", width=43, padx=0, fg="#a5b1c2", font=("arial", 10))
subjectText.grid(row=1, column=1, columnspan=2)

# ===================================================== rightBox =============================================================

subject = Entry(rightBox, width=45)
subject.grid(row=1, column=1, padx= 5, pady=10)

credit = Entry(rightBox, width=10, justify='center')
credit.grid(row=1, column=2, pady=5)

lGrade = Entry(rightBox, width=10, justify='center')
lGrade.grid(row=1, column=3, pady=5)

hGrade = Entry(rightBox, width=10, justify='center')
hGrade.grid(row=1, column=4, pady=5)

# =================================================== bottomFrame  ===============================================================

hGpa = Label(bottomFrame, text="0.0", bg="#778ca3", fg="white", relief=FLAT, font=("Arial", 10))
hGpa.pack(side=RIGHT, fill=X, padx=6)

hGpaLabel = Label(bottomFrame, text="(Highest) GPA: ", bg="#778ca3", fg="white", relief=FLAT, font=("Arial", 10))
hGpaLabel.pack(side=RIGHT, fill=X, padx=6)

lGpa = Label(bottomFrame, text="0.0", bg="#778ca3", fg="white", relief=FLAT, font=("Arial", 10))
lGpa.pack(side=RIGHT, fill=X, padx=6)

lGpaLabel = Label(bottomFrame, text="(Lowest) GPA: ", bg="#778ca3", fg="white", relief=FLAT, font=("Arial", 10))
lGpaLabel.pack(side=RIGHT, fill=X, padx=6)

window.mainloop()
