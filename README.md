# call_counter
You can run the pre-compiled version of this by just opening the executable file located under '/dist/call_counter_gui.exe'

Source code is the main directory.

## demo
https://i.imgur.com/RYhdRk8.gif

## features

### logins
We needed a way to organise whos daily logs are whos - so I made a small window at the start of the program that ask for a name.

No password required, in my use case, I'm just getting names of people on my team so that each person has a different log file for that day.

### file saving / organisation
When the user hits the end shift button, the program looks for a directory titled 'Week_XX' - these are weeks of the year.

If the directory doesn't already exist (i.e. start of a new week), it will create one and write the user's call log file for that shift.

An example would be: 'Week_08/Alex_2024-03-01_call-logs.csv'.

### call auto suggestions
I wanted my team to be able to quickly add common call types that we usually get.

So I wrote this auto suggestion feature that goes off the frist couple of characters/letters they enter into the 'Add Call' textbox.

Commom calls/auto suggested calls can be added to the common_call_types.txt file.

Users can also enter in new types of calls that aren't already in the common call txt file, these are still saved and will appear in the daily/weekly roundups.

### weekly roundup
Drag and drop 'weekly-roundup.py' into one of the weekly folders (i.e. Week_08) and run it in python.

This grabs all the data from every CSV file stored in that week's folder and creates a total of all the calls we got that week.

Then we can use this weekly roundup to graph pretty charts in Excel.

I may or may not turn this into a GUI.

<br>

<b>Thanks so much! =)</b>

<i>(a good friend once told me "this could've been written down in a note book instead")</i>
