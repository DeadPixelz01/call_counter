from tkinter import *
from tkinter import messagebox
from datetime import date

# function to write/save to the output file
def write_to_file():
    # calculate total number of calls
    total_calls = sum(var.get() for var in call_counts.values())
    # open/create the output file (i.e. *todays date*_call-logs.txt)
    output_file_name = '{}_call-logs.txt'.format(today)
    with open(output_file_name, "w") as output_f:
        # write the total number of calls and the 'titles/names' of the calls
        output_f.write("Total calls: {}\n".format(total_calls))
        for call_type, count_var in call_counts.items():
            output_f.write("{}: {}\n".format(call_type, count_var.get()))
    # inform the user in the terminal that the files was written successfully
    print("Writing call counts/records to the output file...")
    print("Done =)")

# set the date to today's date
today = date.today()

# create the main gui window
root = Tk()
root.title("Alex's Call Counter")

# dictionary to store all our call counts
call_counts = {}

# function to add a new call field
def add_call_field():
    # create a new call type
    # strip func is used here to remove leading/trailing whitespaces
    new_call_type = call_type_entry.get().strip()
    if new_call_type:
        # check if the call type is not empty
        call_counts[new_call_type] = IntVar()
        # draw the label for the call
        Label(root, text=new_call_type).grid(row=len(call_counts) + 1, column=0, sticky=W)
        # draw the text box field for counting the calls
        Entry(root, textvariable=call_counts[new_call_type]).grid(row=len(call_counts) + 1, column=1)
        # draw the plus/minus buttons for changing the values
        Button(root, text='+', command=lambda var=call_counts[new_call_type]: var.set(var.get() + 1)).grid(row=len(call_counts) + 1, column=2)
        Button(root, text='-', command=lambda var=call_counts[new_call_type]: var.set(max(var.get() - 1, 0))).grid(row=len(call_counts) + 1, column=3)

        # reposition the "End Shift" button below the last call field
        end_shift_button.grid(row=len(call_counts) + 2, column=0, columnspan=2, pady=10)
    else:
        # notify the user if the call type is empty
        messagebox.showerror("Error", "Please enter a call type.")

# function to handle end of shift
def end_shift():
    write_to_file()
    root.destroy()

# label and entry widgets for adding new call types
Label(root, text="Add New Call Type:").grid(row=0, column=0, sticky=W)
call_type_entry = Entry(root)
call_type_entry.grid(row=0, column=1)
add_button = Button(root, text="Add", command=add_call_field)
add_button.grid(row=0, column=2)

# button to end shift
end_shift_button = Button(root, text="End Shift", command=end_shift)

# run the main program's loop
root.mainloop()