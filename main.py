from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk


root = Tk()
# root.geometry('500x300')
root.title('ASK DOC!')



im=Image.open("doctor.jpg")
# print(im.size)
im = im.resize((323,327),Image.ANTIALIAS)
img=ImageTk.PhotoImage(im)
doc_pic = Label(root, image=img )
doc_pic.pack()
def show_BMI_test():
    pass

def show_fat_test():
    function_selection_window.withdraw()
    fat_test_window = Toplevel(root)
    v_gender = StringVar()
    def change_variable_label():
        if v_gender.get() == 'Male':
            variable_label1['text'] = 'Input abdomen circumference:'
            variable_label2.grid_forget()
            variable_entry2.grid_forget()
        else:
            variable_label1['text'] = 'Input waist circumference:'
            variable_label2.grid(row=4, column=0)
            variable_entry2.grid(row=4, column=1, padx=10)
    def calc():
        #Err checking
        err_flag = False
        if v_height.get().isdigit():
            height = int(v_height.get())
            print(height)
        else:
            v_height.set('Height must be positive integer!')
            err_flag = True

        if v_neck.get().isdigit():
            neck = int(v_neck.get())
            print(neck)
        else:
            v_neck.set('Neck circumference must be positive integer!')
            err_flag = True

        if v_variable1.get().isdigit():
            variable1 = int(v_variable1.get())
            print(variable1)
        else:
            v_variable1.set('This must be positive integer!')
            err_flag = True

        if v_gender.get() == 'Female':
            if v_variable2.get().isdigit():
                variable2 = int(v_variable2.get())
                print(variable2)
            else:
                print(v_gender.get())
                v_variable2.set('This must be positive integer!')
                err_flag = True

        if err_flag:
            return

        if v_gender.get()=='Male':
            abdomen = variable1
            m1=86.01
            m2=70.041
            m3=36.76
            import math as m
            if abdomen - neck <= 0:
                showwarning('Warning', 'Abdomen circumference must be bigger than neck', parent=fat_test_window)
                return
            a=m.log10(abdomen - neck)
            b=m.log10(height)
            fat=m1 * a - m2 * b + m3
        else:
            waist = variable1
            hip = variable2
            f1=163.205
            f2=97.684
            f3=78.387
            import math as m
            if waist + hip - neck <= 0:
                showwarning('Warning','This is not a normal person!',parent=fat_test_window)
                return
            c=m.log10(waist + hip - neck)
            d=m.log10(height)
            fat=f1 * c -f2 * d - f3

    r1=Radiobutton(fat_test_window, text="Male", variable=v_gender, value='Male', command=change_variable_label)
    r1.grid(row=0, column=0)
    r1.select()
    r2=Radiobutton(fat_test_window, text="Female", variable=v_gender, value='Female', command=change_variable_label)
    r2.grid(row=0, column=1)

    v_height = StringVar()
    v_neck = StringVar()
    v_variable1 = StringVar()
    v_variable2 = StringVar()

    height_label = Label(fat_test_window, text='Input height:')
    height_label.grid(row=1, column=0)
    height_entry = Entry(fat_test_window, textvariable=v_height, width=35)
    height_entry.grid(row=1, column=1, padx=10)
    neck_label = Label(fat_test_window, text='Input neck circumference:')
    neck_label.grid(row=2, column=0)
    neck_entry = Entry(fat_test_window, textvariable=v_neck, width=35)
    neck_entry.grid(row=2, column=1, padx=10)

    variable_label1 = Label(fat_test_window, text='Input abdomen circumference:')
    variable_label1.grid(row=3, column=0)
    variable_entry1 = Entry(fat_test_window, textvariable=v_variable1, width=35)
    variable_entry1.grid(row=3, column=1, padx=10)

    variable_label2 = Label(fat_test_window, text='Input hip circumference:')
    variable_entry2 = Entry(fat_test_window, textvariable=v_variable2, width=35)

    submit_button = Button(fat_test_window, text='Submit', command=calc, width=10)
    submit_button.grid(row=5, columnspan=2)

    fat_test_window.mainloop()
        #TODO 回到主界面
def show_function_selection():
    print(language_selection.get(ACTIVE))

    language_selection_window.withdraw()
    global function_selection_window
    function_selection_window = Toplevel(root)
    BMI_button = Button(function_selection_window, text='Get BMI', command=show_BMI_test)
    BMI_button.pack(fill=X)
    fat_button = Button(function_selection_window, text='Get fate rate', command=show_fat_test)
    fat_button.pack(fill=X)

    function_selection_window.mainloop()
def show_language_selection():
    root.withdraw()
    global language_selection_window, language_selection
    language_selection_window = Toplevel(root)

    instruction = Label(language_selection_window, text='Please select language', font=('Calibri',15))
    instruction.pack()
    language_selection = Listbox(language_selection_window, font=('Calibri',12))
    language_selection.pack()

    # 往列表里添加数据
    for item in ["English", "中文", "español"]:
        language_selection.insert(END, item)
    language_selection.select_set(0)

    button_next_language = Button(language_selection_window, font=('Calibri',12), text='continue', command=show_function_selection)
    button_next_language.pack()

    language_selection_window.mainloop()
button_next_root = Button(root, text='Continue', command=show_language_selection, font=('Calibri',12))
button_next_root.pack()

if __name__ == '__main__':
    root.mainloop()