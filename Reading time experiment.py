#Reading time experiment by Søren Orm Hansen - 28/10-2019

#Importing the packages
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

#Welcoming text + accustoming the participants to experimental setup
txt = ["Welcome to the reading experiment. \n(Press space to continue)", 
"When the experiment starts, a word will be presented on the screen, which you have to read. \n(Press space to continue)",
"When you have read the word, press space and a new word will appear. \n(Press space to continue)",
"You have to do this for the entire text. \n(Press space to continue)", 
"First, a trial of what the test is going to be like \n(Press space to start the trial)",
"This", "is", "an", "example", "of", "what", "the", "test", "will", "be", "like",
"Well done. Now the test will start \n(Press space to start the experiment)"]

#Showing the welcoming text to the participants
for i in txt:
    msg = visual.TextStim(win, text = i)
    msg.draw()
    win.flip()
    event.waitKeys(keyList=["space"])

#Creating a stopwatch
stopwatch = core.Clock()

#Reseting the stopwatch
stopwatch.reset()

#Creating the logfile
logfile = pd.DataFrame(columns = ["ID","Age","Gender", "Native_Language","Stimulus", "Word", "Reaction_Time"])

#Randomly assigning experimental setting 1 (the first part of Winnie the Pooh with bees making honey) 
#or 2 (the first part of Winnie the Pooh with bees making juice) to the participants 
if random.randrange(0, 2) == 0:
    ex_txt = """Once upon a time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by himself under the name of Sanders. 
One day when he was out walking, he came to an open place in the middle of the forest, and in the middle of this place was a large oak-tree, and, from the top of the tree, 
there came a loud buzzing-noise. Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws, and began to think. First of all he said to himself: 
That buzzing-noise means something. You don’t get a buzzing-noise like that, just buzzing and buzzing, without its meaning something. 
If there’s a buzzing-noise, somebody’s making a buzzing-noise, and the only reason for making a buzzing-noise that I know of is because you’re a bee. 
Then he thought another long time, and said: ‘And the only reason for being a bee that I know of is making honey.’ 
And then he got up, and said: ‘And the only reason for making honey is so as I can eat it.’ So he began to climb the tree."""
    txt_num = 1
else:
    ex_txt = """Once upon a time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by himself under the name of Sanders. 
One day when he was out walking, he came to an open place in the middle of the forest, and in the middle of this place was a large oak-tree, and, from the top of the tree, 
there came a loud buzzing-noise. Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws, and began to think. First of all he said to himself: 
That buzzing-noise means something. You don’t get a buzzing-noise like that, just buzzing and buzzing, without its meaning something. 
If there’s a buzzing-noise, somebody’s making a buzzing-noise, and the only reason for making a buzzing-noise that I know of is because you’re a bee. 
Then he thought another long time, and said: ‘And the only reason for being a bee that I know of is making juice.’ 
And then he got up, and said: ‘And the only reason for making honey is so as I can eat it.’ So he began to climb the tree."""
    txt_num = 2

#Splitting the text by the spaces in the text
ex_txt = ex_txt.split(sep = " ")

#Showing the participants the words in the text assigned to them while recording the participant's ID, age,
#native language, stimulus, word they read, and reading time
for i in ex_txt:
    msg = visual.TextStim(win, text = i)
    msg.draw()
    win.flip()
    stopwatch.reset()
    event.waitKeys(keyList=["space"])
    rt = stopwatch.getTime()
    word = i
    logfile = logfile.append({
        "ID": ID,
        "Age": AGE,
        "Gender": GENDER,
        "Native_Language": NAT_LANG,
        "Stimulus": txt_num,
        "Word":   word,
        "Reaction_Time": rt}, 
        ignore_index = True)

#Showing the participants the end of experiment text
msg = visual.TextStim(win, text = "Well done! The experiment is now done, and you are free to go.")
msg.draw()
win.flip()
event.waitKeys()

#naming the logfile 
logfile_name = "logfiles/readingP2_{}.csv".format(ID) #don't have two people with the same id

#exporting the logfile to a .csv file
logfile.to_csv(logfile_name)
