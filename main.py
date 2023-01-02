from tkinter import *
from tkinter import messagebox, ttk

window = Tk()

staffs = ['Kayode', 'Collins', 'Kate']
salary = [50000,70000,40000]

def estimated_salary(event):
    if staff_name_entry.get() in staffs:
        pass
        # global staff_salary_entry
        #
        # index = staffs.index(staff_name_entry.get())
        # estimated_amount = salary[index]
        # print(estimated_amount)
        # staff_salary_entry.delete(0, END)
        # staff_salary_entry.insert(0, f'{estimated_amount}')
        # # staff_salary_entry = Entry(window, textvariable=estimated_amount).grid(row=1, column=1)


def calculation():
    print('a')
    print(staff_salary_entry.get())
    salary1 = int(staff_salary_entry.get())
    print('b')
    iou = int(staff_iou_entry.get())
    absent = int(staff_absent_entry.get())*salary1/31
    lateness = int(staff_late_entry.get())*200
    deduction = int(staff_deduction_entry.get())
    final_pay = salary1-(iou + absent + lateness + deduction)
    display = Label(window, text=final_pay).grid(row=6, column=0, columnspan=2)

# Labels
staff_name = Label(window, text='Staff Name',).grid(row=0, column=0, sticky='e')
staff_salary = Label(window, text='Salary',).grid(row=1, column=0 , sticky='e')
staff_iou = Label(window, text='IOU',).grid(row=2, column=0, sticky='e')
staff_absent = Label(window, text='Absent',).grid(row=3, column=0, sticky='e')
staff_late = Label(window, text='Lateneass',).grid(row=4, column=0, sticky='e')
staff_deduction = Label(window, text='Other deductions',).grid(row=5, column=0, sticky='e')

# Entry
staff_name_entry = ttk.Combobox(window, values=staffs)
staff_name_entry.grid(row=0, column=1)
staff_name_entry.bind('<<ComboboxSelected>>', estimated_salary)

staff_salary_entry = Entry(window)
staff_salary_entry.grid(row=1, column=1)

staff_iou_entry = Entry(window)
staff_iou_entry.grid(row=2, column=1)

staff_absent_entry = Entry(window)
staff_absent_entry.grid(row=3, column=1)

staff_late_entry = Entry(window)
staff_late_entry.grid(row=4, column=1)

staff_deduction_entry = Entry(window)
staff_deduction_entry.grid(row=5, column=1)

# Button
calculate_button = Button(window, text='Calculate', command=calculation).grid(row=7, column=0, columnspan=2)
window.mainloop()
