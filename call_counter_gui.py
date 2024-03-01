from tkinter import *
from tkinter import messagebox
from datetime import date
import os

# a global variable to store the user's name
username = ""
today = date.today()
# grab the week number from today's date so that we can create/write to a dir for that week
week_number = today.strftime("%U")
# check if the dir exist - make one if not
week_directory = f"Week_{week_number}"
if not os.path.exists(week_directory):
    os.makedirs(week_directory)

# autocomplete call suggestions
with open("common_call_types.txt", "r") as file:
    common_call_types = [line.strip() for line in file.readlines()]

def write_to_file():
    # calculate total calls
    total_calls = sum(var.get() for var in call_counts.values())
    # create a file to write to (i.e Week_8/Alex_DATE_call-logs.csv)
    output_file_name = '{}/{}_{}_call-logs.csv'.format(week_directory,username,today)
    with open(output_file_name, "w") as output_f:
        # write total calls
        output_f.write("Total calls,{}\n".format(total_calls))
        # write all the calls by call type
        for call_type, count_var in call_counts.items():
            output_f.write("{},{}\n".format(call_type, count_var.get()))
    print(f'Writing call counts/records to {output_file_name}...')
    print("Done =)")

def add_call_field():
    new_call_type = call_type_entry.get().strip()
    if new_call_type:
        call_counts[new_call_type] = IntVar()
        Label(root, text=new_call_type).grid(row=len(call_counts) + 1, column=0, sticky=W)
        Entry(root, textvariable=call_counts[new_call_type]).grid(row=len(call_counts) + 1, column=1)
        Button(root, text='+', command=lambda var=call_counts[new_call_type]: var.set(var.get() + 1), bg='green').grid(row=len(call_counts) + 1, column=2)
        Button(root, text='-', command=lambda var=call_counts[new_call_type]: var.set(max(var.get() - 1, 0)), bg='red').grid(row=len(call_counts) + 1, column=3)
        end_shift_button.grid(row=len(call_counts) + 2, column=0, columnspan=2, pady=10)
    else:
        messagebox.showerror("Error", "Please enter a call type.")

def end_shift():
    write_to_file()
    root.destroy()

def login():
    # access the global username variable first
    global username
    username = username_entry.get().strip()
    # check if the user has entered a name before using the program
    if username:
        messagebox.showinfo("Welcome", f"Welcome, {username}!")
        login_window.destroy()
    else:
        messagebox.showerror("Error", "Please enter a username.")

# main func for auto completing - this is kinda buggy atm but it does what i need it to do
def autocomplete(event):
    entered_text = call_type_entry.get()
    if entered_text:
        matches = [call for call in common_call_types if call.startswith(entered_text)]
        # show the first matching call type in autocomplete
        autocomplete_var.set(matches[0])
        # highlight the rest of the text
        call_type_entry.select_range(len(entered_text), END)

# create the initial login window
login_window = Tk()
login_window.title("Login")

Label(login_window, text="Username:").grid(row=0, column=0, sticky=W)
username_entry = Entry(login_window)
username_entry.grid(row=0, column=1)

login_button = Button(login_window, text="Login", command=login)
login_button.grid(row=1, column=0, columnspan=2, pady=10)

login_window.mainloop()

# proceed to the main program if login is successful
root = Tk()
root.title(f'{username} Call Counter')

call_counts = {}

Label(root, text="Add New Call Type:").grid(row=0, column=0, sticky=W)
autocomplete_var = StringVar()
call_type_entry = Entry(root, textvariable=autocomplete_var)
call_type_entry.grid(row=0, column=1)
# binds the autocomplete function to key release event
call_type_entry.bind("<KeyRelease>", autocomplete)
add_button = Button(root, text="Add", bg='blue', command=add_call_field)
add_button.grid(row=0, column=2)

end_shift_button = Button(root, text="End Shift", bg='orange', command=end_shift)

root.mainloop()