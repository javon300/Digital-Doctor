from tkinter import *
import tkinter.messagebox


# person class variable used to store information on all person objects
class Person:
    def __init__(self):
        self.f_name = "fname"
        self.l_name = "lname"
        self.age = 0
        self.gender = "male"
        self.ethnicity = "black"
        self.weight = 0.0
        self.temperature_cel = 0
        self.temperature_for = 0
        self.total_points = 0

global person
person = Person()

class RegistrationWindow:
    def __init__(self, registration_window):
        # declaration of variables for the registration window
        self.fn_lbl = Label(registration_window, text="First Name")
        self.f_name_entry = Entry(registration_window, bd=3)
        self.ln_lbl = Label(registration_window, text="Last Name")
        self.l_name_entry = Entry(registration_window, bd=3)
        self.w_lbl = Label(registration_window, text="Weight")
        self.weight_entry = Entry(registration_window, bd=3)
        self.a_lbl = Label(registration_window, text="Age")
        self.age_entry = Entry(registration_window, bd=3)
        self.g_lbl = Label(registration_window, text="Gender")
        self.gender_entry = Entry(registration_window, bd=3)
        self.e_lbl = Label(registration_window, text="Ethnicity")
        # drop down menu variable creation
        self.tkvar = StringVar(registration_window)  # created tk_variable
        self.e_choices = {'Black', 'White', 'Asian', 'Chinese', 'Japanese'}  # choices for dropdown menu
        self.tkvar.set('Black')  # default option for dd_menu
        self.ethnicity_dd_menu = OptionMenu(registration_window, self.tkvar, *self.e_choices)

        self.t_lbl = Label(registration_window, text="Temperature(celcius)")
        self.temperature_entry = Entry(registration_window, bd=3)
        self.register_btn = Button(registration_window, text="Finish", command=self.add_person)

        # place butttons in window to be created on keypress in main menu
        self.fn_lbl.pack()
        self.f_name_entry.pack()
        self.ln_lbl.pack()
        self.l_name_entry.pack()
        self.w_lbl.pack()
        self.weight_entry.pack()
        self.a_lbl.pack()
        self.age_entry.pack()
        self.g_lbl.pack()
        self.gender_entry.pack()
        self.e_lbl.pack()
        self.ethnicity_dd_menu.pack()
        self.t_lbl.pack()
        self.temperature_entry.pack()
        self.register_btn.pack()

    def write_to_file(self):  # called at the end of the add_person method
        outputFile = open("patients.txt", "a+")  # Open a file for appending
        # Write record to file
        person_record = person.f_name + "\t" + person.l_name + "\t" + str(person.weight) + "\t" + \
                        str(person.age) + "\t" + person.gender + "\t" + person.ethnicity + "\t" + \
                        str(person.temperature_cel) + "\t" + str(person.temperature_for) + "\t" +\
                        str(person.total_points)
        outputFile.write("%s" % person_record)
        outputFile.close()  # Close the file
        tkinter.messagebox.showinfo("Data written")

    def add_person(self):  # saves all data entered to the global person variable
        try:
            person.f_name = self.f_name_entry.get()
            person.l_name = self.l_name_entry.get()
            string_weight = self.weight_entry.get()
            person.weight = float(string_weight)
            string_age = self.age_entry.get()
            person.age = int(string_age)
            person.gender = self.gender_entry.get()
            person.ethnicity = self.tkvar.get()
            string_temp_c = self.temperature_entry.get()
            person.temperature_cel = float(string_temp_c)

            # test entered values and assign points
            print(" ")
            print("**************JahMedicare****************")
            # points acoording to weight
            if person.weight > 200:
                person.total_points += 4
                print("sorry to break it to you but, you are waaay overweight.")
            else:
                if 100 <= person.weight <= 200:
                    person.total_points += 2
                    print("congrats you fat :).")
            # points acoording to age
            if person.age > 65:
                person.total_points += 3
            if person.age < 3:
                person.total_points += 2
            # points according to temperature
            if 37.2 <= person.temperature_cel <= 100:
                person.total_points += 2
                print("burning up bro:).")
                # calculates forenheight
            person.temperature_for = (person.temperature_cel * (9 / 5)) + 32

            tkinter.messagebox.showinfo("well done", "record added succesfully")
            print("name: " + person.f_name)
            print("name: " + person.l_name)
            print("weight " + str(person.weight))  # converts weight back to string for output
            print("age: " + str(person.age))
            print("gender: " + person.gender)
            print("ethnicity: " + str(person.ethnicity))
            print("temperature: " + str(person.temperature_cel) + " C")
            print("temperature: " + str(person.temperature_for) + " F")
            print("total Points: " + str(person.total_points))
            self.write_to_file()
        except ValueError:
            tkinter.messagebox.showerror("please enter valid numbers in the number fields")
            print("That is not a number")
        except FileNotFoundError:
            tkinter.messagebox.showerror("file could not be found")
            print("file not found")

class ReportWindow:
    def __init__(self, report_window):
        self. spacer = Label(report_window, height=4, text="    ")
        self.text = Text(report_window, height=30, width=80)
        self.spacer.pack()
        self.text.pack()
        self.build_report()
        self.text.config(state=DISABLED)
    def build_report(self):
        try:
            file_handle = open('patients.txt', "r")
            if file_handle.mode =="r":
                records = file_handle.readlines()
                file_handle.close()
                heading ="First  " + "\t" +"Last  " + "\t" +"Weight" + "\t" +"Age " + "\t" +"Gender" + \
                         "\t" +"Ethinic" + "\t" +"Temp C" + "\t" +"Temp F" + "\t" +"Points" + "\n"
                print("The last line is:")
                print(records[len(records) - 1])
                self.text.insert('end', "Record Result"+"\n")
                self.text.insert('end', heading)
                self.text.insert('end', records[len(records) - 1])

        except FileNotFoundError:
            tkinter.messagebox.showerror("file not found")

class AdminReportWindow:
    def __init__(self, report_window):
        self. spacer = Label(report_window, height=4, text="    ")
        self.text = Text(report_window, height=30, width=80)
        self.spacer.pack()
        self.text.pack()
        self.build_report()
        self.text.config(state=DISABLED)
    def build_report(self):
        try:
            file_handle = open("patients.txt", "r")
            if file_handle.mode =="r":
                records = file_handle.read()
                file_handle.close()
                heading ="First  " + "\t" +"Last  " + "\t" +"Weight" + "\t" +"Age " + "\t" +"Gender" + \
                         "\t" +"Ethinic" + "\t" +"Temp C" + "\t" +"Temp F" + "\t" +"Points" + "\n"
                self.text.insert('end',heading)
                print(records)
                self.text.insert('end', records)
                record = records[len(records) - 1]
                self.text.insert('end', record)
                # self.text.insert("Record Result")
        except FileNotFoundError:
            tkinter.messagebox.showerror("file not found")

class DiagnosisWindow:
    def __init__(self, diagnosis_win):
        self.count =0
        self.questions = ["do you have a cold", "Do you cough a lot", "do you have the flu",
                          "Do you have any other bacterial/fungal", "has the infection lasted more than three weeks.",
                          "Are you experiencing chest pain", "Do you often feel more fatigue than you normally would",
                          "Have you been vomiting", "experiencing Nausea", "Have you been having diarrhea",
                          "Have you been wheezing or experiencing shortness of breath"]
        self.answer = [None]*11
        self.spacer1 = Label(diagnosis_win, height=4)
        self.question_area = Entry(diagnosis_win, justify='center', relief='solid', font="Times 13", width=60)
        self.spacer2 = Label(diagnosis_win)
        self.answer_area = Entry(diagnosis_win,justify='center', relief='solid', font="Times 11", width=30)
        self.spacer3 = Label(diagnosis_win)
        self.submit_btn = Button(diagnosis_win, text="submit", command=self.question_changer)
        #pack created variables to window
        self.spacer1.pack()
        self.question_area.pack()
        self.spacer2.pack()
        self.answer_area.pack()
        self.spacer3.pack()
        self.submit_btn.pack()
        print("question{}: {}".format(self.count, self.questions[self.count]))
        self.question_area.insert('end', self.questions[self.count])

    def question_changer(self):
        self.count += 1
        self.question_area.delete(0,'end')
        self.answer_area.delete(0,'end')
        self.question_area.insert('end', self.questions[self.count])
        self.answer[self.count] = self.answer_area.get()
        print(self.answer[self.count])

# main window
class Main_Window:
    def __init__(self, main_window):
        # create all window widgets
        self.spacer = Label(main_window, text="     ")
        self.lbl1 = Label(main_window, text="JahMedicare", relief="solid", font="Times 32", width=50)
        self.lbl2 = Label(main_window, text="Digital Doctor", relief="solid", font="Times 20", width=50)
        self.lbl3 = Label(main_window, text="You get here, you get better", width=50)
        self.space = Label(main_window, text="     ")
        self.btn1 = Button(main_window, text="add a patient record", command=self.register)
        self.btn2 = Button(main_window, text="diagnose a patient", command=self.diagnosis)
        self.btn3 = Button(main_window, text="show result", command=self.person_record)
        self.btn4 = Button(main_window, text="admin login", command=self.all_records)

        # add all widgets to window
        self.spacer.pack()
        self.lbl1.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        self.space.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()

        # display registration window on command

    def register(self):
        root_register = Tk()
        reg_win = RegistrationWindow(root_register)
        root_register.title("JahMedicare Registration")
        root_register.geometry("800x500+10+10")
        root_register.mainloop()

    def person_record(self):
        root_record = Tk()
        rec_win = ReportWindow(root_record)
        root_record.title("JahMedicare Report")
        root_record.geometry("800x500+10+10")
        root_record.mainloop()

    def all_records(self):
        root_record = Tk()
        ad_rep_win = AdminReportWindow(root_record)
        root_record.title("JahMedicare Report")
        root_record.geometry("800x500+10+10")
        root_record.mainloop()

    def diagnosis(self):
        root = Tk()
        diagnosis_win = DiagnosisWindow(root)
        root.title('JahMedicare Diagnosis')
        root.geometry("800x400+10+10")
        root.mainloop()
        # display main menu


main_window = Tk()
window = Main_Window(main_window)
main_window.title('JahMedicare System')
main_window.geometry("800x400+10+10")
main_window.mainloop()
