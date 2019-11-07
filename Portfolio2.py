#Title: Portfolio 2
#Date: 07.10.2019
#Author: Lærke Kyed Reese Andersen 
 
#Reading library
from psychopy import visual, core, event, gui
import glob
import random
import pandas as pd

#Pop up window
box = gui.Dlg(title = "Title")
box.addField("ID:")
box.addField("Age:")
box.addField("Gender:", choices = ["Female", "Male", "Other"])
box.addField("Native Language:", choices = ["English", "Non-English"])
box.show()
if box.OK:
    ID = box.data[0]
    AGE = box.data[1]
    GENDER = box.data[2]
    NAT_LANG = box.data[3]
elif box.Cancel:
    core.quit()

logfile = pd.DataFrame(columns = ["ID", "Age", "Gender", "Native_Language", "Stimulus", "Word", "Reaction.time"])

#Defining window
win = visual.Window(fullscr = True)

#Introduction
msg = visual.TextStim(win, text = "Welcome to the experiment! \n\nYou will be presented with a short text. \nYou will only be able to read one word at a time. \nWhen you have read the word, press 'space' to get the next word. \n\nWe will start out with a brief example:")
msg.draw()
win.flip()
event.waitKeys(keyList = ["space"])

Trial = "This is just an example."
Trial = Trial.split(sep = " ")

for testword in Trial:
    msg = visual.TextStim(win, text = testword)
    msg.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

msg = visual.TextStim(win, text = "Great! You are now ready to begin the experiment. \n(Press 'space' to continue)")
msg.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#Experiment:

#Adding stopwatch
stopwatch = core.Clock()

#Securing randomization
if random.randrange(0, 2) == 0:
    Stimulus = "Once upon a time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by himself under the name of Sanders. One day when he was out walking, he came to an open place in the middle of the forest, and in the middle of this place was a large oak-tree, and, from the top of the tree, there came a loud buzzing-noise. Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws, and began to think. First of all he said to himself: That buzzing-noise means something. You don’t get a buzzing-noise like that, just buzzing and buzzing, without its meaning something. If there’s a buzzing-noise, somebody’s making a buzzing-noise, and the only reason for making a buzzing-noise that I know of is because you’re a bee. Then he thought another long time, and said: ‘And the only reason for being a bee that I know of is making honey.’ And then he got up, and said: ‘And the only reason for making honey is so as I can eat it.’ So he began to climb the tree."
    Stimulus_num = 1
else:
    Stimulus = "Once upon a time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by himself under the name of Sanders. One day when he was out walking, he came to an open place in the middle of the forest, and in the middle of this place was a large oak-tree, and, from the top of the tree, there came a loud buzzing-noise. Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws, and began to think. First of all he said to himself: That buzzing-noise means something. You don’t get a buzzing-noise like that, just buzzing and buzzing, without its meaning something. If there’s a buzzing-noise, somebody’s making a buzzing-noise, and the only reason for making a buzzing-noise that I know of is because you’re a bee. Then he thought another long time, and said: ‘And the only reason for being a bee that I know of is making juice.’ And then he got up, and said: ‘And the only reason for making honey is so as I can eat it.’ So he began to climb the tree."
    Stimulus_num = 2

#Splitting the list into seperate words:
Stimulus = Stimulus.split(sep = " ")

#Creating loop for every word in the text:
for word in Stimulus:
    msg = visual.TextStim(win, text = word)
    msg.draw()
    win.flip()
    stopwatch.reset()
    event.waitKeys(keyList = ["space"])
    reaction_time = stopwatch.getTime()
    Word = word
    logfile = logfile.append({
        "ID": ID,
        "Age": AGE,
        "Gender": GENDER,
        "Native_Language": NAT_LANG,
        "Stimulus": Stimulus_num,
        "Word": Word,
        "Reaction.time": reaction_time}, ignore_index = True)

#Saving the data
logfile_id = "logfiles/readingP2_{0}.csv".format(ID)
logfile.to_csv(logfile_id)