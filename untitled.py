from psychopy import visual, core, event, gui
import glob, random, pandas as pd


#Box for collecting information on the test subjects
box = gui.Dlg(title = "Experiment - assignment 2")
box.addField("Participant ID:")
box.addField("Age:")
box.addField("Gender:", choices=["Other", "Female", "Male"])
box.addField("Native language:", choices=["English", "Non-English"])
box.show()
if box.OK:
    ID = box.data[0]
    AGE=box.data[1]
    GENDER=box.data[2]
    NAT_LANG=box.data[3]
elif box.Cancel:
    core.quit()

#Creating a window
win = visual.Window(fullscr=True)

#Welcome text
txt = ["Welcome to the reading experiment. \n(Press space to continue)", 
"When the experiment starts, a word will be presented on the screen, which you have to read. \n(Press space to continue)",
"When you have read the word, press space and a new word will appear. \n(Press space to continue)",
"You have to do this for the entire text. \n(Press space to continue)", 
"First, a trial of what the test is going to be like \n(Press space to start the trial)",
"This", "is", "an", "example", "of", "what", "the", "test", "will", "be", "like",
"Well done. Now the test will start \n(Press space to start the experiment)"]

for i in txt:
    msg = visual.TextStim(win, text = i)
    msg.draw()
    win.flip()
    event.waitKeys(keyList=["space"])

stopwatch = core.Clock()

stopwatch.reset()


ex_txt = ["The", "experiment", "text"]

for i in ex_txt:
    msg = visual.TextStim(win, text = i)
    msg.draw()
    win.flip()
    stopwatch.reset()
    event.waitKeys(keyList=["space"])
    rt = stopwatch.getTime()
    reaction_time = stopwatch.getTime()





msg = visual.TextStim(win, text = "Well done! The experiment is now done, and you are free to go.")
msg.draw()
win.flip()
event.waitKeys()


#Creating a logfile
logfile = pd.DataFrame(columns = ["ID","Age","Gender", "Native_Language","Stimulus","Reaction_Time"])

logfile = logfile.append({
    "ID": ID,
    "Age": AGE,
    "Gender": GENDER,
    "Native_Language": NAT_LANG,
#    "Stimulus": pic_number,
    "Reaction_Time": reaction_time}, 
    ignore_index = True)



logfile_name = "logfiles/logfile_{}.csv".format(ID)
logfile.to_csv(logfile_name)





