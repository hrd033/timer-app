import time
from gtts import gTTS
import IPython.display
import pygame
import os
# from PIL import Image
# import keyboard
import random

# TO TEST: when you open new terminal paste
#  python3 -m venv myvenv -> dont need to run again but that created the venv
#  source myvenv/bin/activate -> will transfer you to the venv
# terminal has to say (myvenv) at the beginning. if it doesn't say that source myvenv/bin/activate
#TO RUN THE CODE: python3.12  TIMERAPP.py 

pygame.mixer.init()

harpup = '/Users/hayleydeberry/Desktop/PROJECT/SOUNDS/HARP UP.mp3'
harpdown='/Users/hayleydeberry/Desktop/PROJECT/SOUNDS/HARP UP.mp3'

def playsound(filepath):
    sound = pygame.mixer.Sound(filepath)
    sound.play()
    pygame.time.delay(int(sound.get_length() * 1000))  # Delay for the length of the sound in milliseconds

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')  # Remove the temporary file after playing

# def show_image(image_path):
#     img = Image.open(image_path)
#     display(img)

# Example usage:
# image_path = '/path/to/your/image.jpg'  # Replace with the actual path to your image file
# show_image(image_path)


class Stretch:
  stretchtotal=0
  def __init__(self, name, tag, lr, defaulttime=60, filepath="", tag2=""):
    self.name=name
    self.tag=tag
    Stretch.stretchtotal+=1
    self.stretchid=self.stretchtotal
    self.lr=lr
    self.filepath=filepath
    self.defaulttime=defaulttime
    self.tag2=tag2
    # stretchdict[self.name]=self.name, self.stretchid, self.tag, self.lr
    if self.tag=="reclining" or self.tag2=="reclining":
      self.defaulttime=90

#hip stretches
hipflexor = Stretch("Hip Flexor Lunge", "hips", 1, 90)
tfl = Stretch("Side TFL Lunge", "hips", 1)
lizard = Stretch("Lizard Pose", "hips", 1)
hamstring = Stretch("Hamstring Forward Fold", "hips", 1)
itband = Stretch("IT Band Forward Fold", "hips", 1)
quads=Stretch("Leaning Quad Stretch", "hips", 1, 90)
middlesplit=Stretch("Center Split", "hips", 0,120)
psoas=Stretch("Psoas Leaning Stretch", "hips", 1)
butterfly=Stretch("Butterfly", "hips", 0, 120)
glutes=Stretch("Fire Logs Pose", "hips", 1, 120)
frontsplit=Stretch("Front Split", "hips", 1, 90)
splitquad=Stretch("Front Split with Quad Stretch", "hips", 1)
frog=Stretch("Frog Pose", "hips", 0, 90)
layingsideex=Stretch("Reclining Side Extension", "hips", 1, 90, "", "reclining")
internal=Stretch("Internal Rotators Stretch", "hips", 0, 90)

#torso/spine stretches
lowerback=Stretch("Figure 4 Fold", "torso", 1)
upwarddog=Stretch("Upward Dog", "torso", 0)
obliques=Stretch("Side Stretch","torso", 1)
neckback=Stretch("Back of Neck Stretch", "torso", 0)
neckfront=Stretch("Front of Neck Stretch", "torso", 0)
necksides=Stretch("Side of Neck Stretch", "torso", 1)
lookside=Stretch("Look to the Side Stretch", "torso", 1, 30)
puppy=Stretch("Puppy Pose on the Wall", "torso", 0)
twist=Stretch("Spinal Twist", "torso", 1)
eagle=Stretch("Eagle Pose", "torso", 1)
childspose=Stretch("Child's Pose", "torso", 0)

#pointe stretches
achilles=Stretch("Achilles Stretch", "pointe", 1, 90)
calves=Stretch("Calf Block Stretch", "pointe", 1, 90)
toesit=Stretch("Toe Sit", "pointe", 0, 120)
topankle=Stretch("Top of Ankle Stretch", "pointe", 1, 120)
arches=Stretch("Arch Stretch", "pointe", 1, 30)
outerankle=Stretch("Outer Ankle Stretch", "pointe", 1)
innerankle=Stretch("Inner Ankle Stretch", "pointe", 1, 90)
midtoes=Stretch("Middle Three Toes Stretch", "pointe", 1)
bigtoe=Stretch("Big Toe Stretch", "pointe", 1)
pinkytoe=Stretch("Pinky Toe Stretch", "pointe", 1)
massage=Stretch("Foot Massage", "pointe", 1)

#arm stretches
delt=Stretch("Deltoid Stretch", "arms", 1)
tricep=Stretch("Tricep Stretch", "arms", 1)
shoulder=Stretch("Shoulder Head Lean", "arms", 1)
bicep=Stretch("Bicep Stretch", "arms", 1)
wristtop=Stretch("Top of Wrists Stretch", "arms", 0)
wristbottom=Stretch("Wrists Underneath Stretch", "arms", 0 )
fingers=Stretch("Finger Press", "arms", 0)
thumbs=Stretch("Thumb Stretch", "arms", 0)

#deep stretches
pigeon=Stretch("Pigeon Pose", "deep", 1)
legmount=Stretch("Leg Mount Stretch", "deep", 1)
penche=Stretch("Penche Stretch", "deep", 1)
wheel=Stretch("Wheel Pose", "deep", 0)
bow=Stretch("Bow Pose", "deep", 0)

#reclining stretches
reclininghipflexor=Stretch("Reclining Hip Flexor Stretch", "reclining", 1)
reclininghamstring=Stretch("Reclining Hamstring Stretch", "reclining", 1)
recliningquad=Stretch("Reclining Quad Stretch", "reclining", 1)
recliningglute=Stretch("Reclining Glute Stretch", "reclining", 1)
recliningchest=Stretch("Reclining Chest Stretch", "reclining", 1)
recliningmiddlesplit=Stretch("Reclining Middle Split", "reclining", 0)
layingsideex

savasana=Stretch("Savasana", "rest", 0)

torsoseries=[lowerback, obliques, upwarddog, necksides, neckback, neckfront, lookside,
             puppy, twist, eagle]

hipflow_R=[hipflexor, psoas, tfl, lizard, hamstring, itband, quads]
hipflow_L=hipflow_R
hipscontd=[butterfly, glutes, frog, middlesplit, frontsplit,
            layingsideex, internal]

pointeseries=[calves, achilles, toesit, topankle, arches, outerankle,
        innerankle, bigtoe, midtoes, pinkytoe]

armseries=[delt, tricep, shoulder,  bicep, wristtop, wristbottom,
      fingers, thumbs]

deepstretchseries=[pigeon, penche, legmount, wheel, bow, childspose]

essentials=[lowerback, lowerback, obliques, obliques, upwarddog, hipflexor, hipflexor, tfl, tfl,
              hamstring, hamstring, itband, itband, quads, quads, butterfly, middlesplit,
              calves, calves, achilles, achilles, toesit, topankle, topankle,
              arches, arches, outerankle, outerankle, innerankle, innerankle, frontsplit, frontsplit,
             bicep, bicep]

recliningstretchseries=[reclininghipflexor, reclininghamstring, recliningquad, recliningglute,
                        recliningchest, layingsideex, recliningmiddlesplit]


def buildtorso():
  torsodict={}
  for i in torsoseries:
    if i.lr ==0:
      torsodict.update({str(i.name): i.defaulttime})
    else:
      torsodict.update({str(i.name)+" Right": i.defaulttime})
      torsodict.update({str(i.name)+" Left": i.defaulttime})
  return torsodict

def buildhips():
  hipsdict={}
  for i in hipflow_R:
      hipsdict.update({str(i.name)+" Right": i.defaulttime})
  for i in hipflow_L:
      hipsdict.update({str(i.name)+" Left": i.defaulttime})
  for i in hipscontd:
    if i.lr ==0:
      hipsdict.update({str(i.name): i.defaulttime})
    else:
      hipsdict.update({str(i.name)+" Right": i.defaulttime})
      if i==frontsplit:
        hipsdict.update({str(splitquad.name)+" Right": i.defaulttime})
      hipsdict.update({str(i.name)+" Left": i.defaulttime})
      if i==frontsplit:
        hipsdict.update({str(splitquad.name)+" Left": i.defaulttime})
  return hipsdict

def buildpointe():
  pointedict={}
  for i in pointeseries:
    if i.lr ==0:
      pointedict.update({str(i.name): i.defaulttime})
    else:
      pointedict.update({str(i.name)+" Right": i.defaulttime})
      pointedict.update({str(i.name)+" Left": i.defaulttime})
  return pointedict

def buildarms():
  armsdict={}
  for i in armseries:
    if i.lr ==0:
      armsdict.update({str(i.name): i.defaulttime})
    else:
      armsdict.update({str(i.name)+" Right": i.defaulttime})
      armsdict.update({str(i.name)+" Left": i.defaulttime})
  return armsdict

def builddeepstretches():
  deepstretchdict={}
  for i in deepstretchseries:
      if i.lr==1:
        deepstretchdict.update({str(i.name)+" Right": i.defaulttime})
        deepstretchdict.update({str(i.name)+" Left": i.defaulttime})
      else: 
        deepstretchdict.update({str(i.name): i.defaulttime})
  return deepstretchdict

def buildessentials():
  inp=input("Is there anything you want to focus on for this series? Y/N: ").upper()
  print(inp)
  focusoptions={"torso": buildtorso(), "hips": buildhips(),
                "arms": buildarms(), "pointe": buildpointe()}
  focus=""
  restofessentials=[]
  essentialsdict={}
  if inp=="Y":

    print(list(focusoptions))
    focus=(input("What focus area would you like to add? "))
    focusedessentials=[]
    
    if focus in focusoptions.keys():
      focusedessentials.append(focusoptions[focus])
      for i in essentials:
        if i.tag!=focus:
          restofessentials.append(i)
      print(f'{focus.title()} added to Essentials.')
      essentialsdict=focusedessentials[0]
  elif inp=="N":
    focus==""
    pass
  else: print("Please enter a valid input. Y/N")
  for i in restofessentials:
    if i.lr==1:
      essentialsdict.update({str(i.name)+" Right": i.defaulttime})
      essentialsdict.update({str(i.name)+" Left": i.defaulttime})
    else:
      essentialsdict.update({str(i.name): i.defaulttime})
  return essentialsdict

def buildreclining():
  recliningdict={}
  for i in recliningstretchseries:
    if i.lr==1:
      recliningdict.update({str(i.name)+" Right": i.defaulttime})
      recliningdict.update({str(i.name)+" Left": i.defaulttime})
    else:
      recliningdict.update({str(i.name): i.defaulttime})
  return recliningdict

def buildfullbody():
  ss=[]
  torso=buildtorso()
  hips=buildhips()
  pointe=buildpointe()
  arms= buildarms()
  deepstretches=builddeepstretches()
  ss = torso|hips|pointe|arms|deepstretches
  ss.update({childspose.name: childspose.defaulttime})
  ss.update({savasana.name: savasana.defaulttime})
  return ss

def buildsequence(): #WORKING OK
  sequencedict={}
  essentialsdict={}
  optionslist={"torso": buildtorso(), "hips": buildhips(),
                "arms": buildarms(), "pointe": buildpointe(),
                "full body": buildfullbody(), "reclining": buildreclining(),
                "essentials": buildessentials, "deep stretches": builddeepstretches()}
  print(list(optionslist))
  def askonce():
    inp = input("What would you like to stretch? (0=finished) ")
    if inp in optionslist:
      if inp=="essentials":
        essentialssequence=buildessentials()
        print(essentialssequence)
        return essentialssequence
      else:
        print(f"\n {inp.title()} added to sequence.\n")
        sequencedict.update(optionslist[inp])
        print(list(sequencedict), "\n")
        return sequencedict
    elif inp=="0":
      print("Your sequence is empty.")
      return {}
    else:
      print("\nPlease enter a valid input. 0=finished ")
      print(list(optionslist.keys()))
      inp = input("What would you like to stretch? (0=finished) ")
      return {}
  def anythingelse():
    sequencedict={}
    askoncedict=askonce()
    sequencedict.update(askoncedict)
    for i in range(0, 3):
      print(list(optionslist))
      whatelse=input("Anything else? Press 0 to save and move on. ")
      if whatelse in optionslist:
        print(f"\n {whatelse.title()} added to sequence.\n")
        sequencedict.update(optionslist[whatelse])
        print(list(sequencedict), "\n")
        return sequencedict
      elif whatelse=="0":
        print("Sequence saved.")
        return sequencedict
        continue
      else: 
         print("\nPlease enter a valid input. 0=finished ")
         print(list(optionslist))
         print (whatelse)
         return sequencedict
  done=anythingelse()
  return done

def storeduration():
  userduration=int(input("For how long would you like to hold each stretch? Enter your choice in seconds. 0 to use system defaults. "))
  return userduration


def startmidway():
  sequencedict=buildsequence()
  print("Here is your sequence: ")
  print(sequencedict)
  inp=input("Would you like to start from the beginning of this sequence, or midway through? B/M ").upper()
  if inp=="B":
    print("Got it. Your sequence will begin from the first stretch.")
    # return sequencedict
  elif inp=="M":
    updatedsequence={}
    for index, (key, value) in enumerate(sequencedict.items(), start=1):
      print(f"{index}. {key}: {value}")
    newstart=int(input("Please select the number corresponding to the stretch where you would like to start: "))
    for index, (key, value) in enumerate(sequencedict.items(), start=1):
      if index >= newstart:
          updatedsequence[key] = value
          sequencedict=updatedsequence
    print("Got it. Here is your updated sequence: ")
    sequencedict=updatedsequence
    # return updatedsequence
  return sequencedict

##IF STRETCH HAS L AND R, MODIFY BOTH. ASK., BC SOMETIMES L
#ALSO MODIFY TO ADJUST DEFAULT STRETCH DURATION
def setdurations(): #not gonna lie chatgpt did this whole thing, enumerate fucked me upppp
  sequencedict=startmidway()
  userduration=storeduration()
  print("Here is your sequence:")
  if userduration==0:
    for index, (key, value) in enumerate(sequencedict.items()):
      print(f"{index + 1}. {key}: {value}")
  elif isinstance(userduration, int) and userduration != 0:
    for key in sequencedict.keys():
      sequencedict[key] = userduration
    print(sequencedict)
  return sequencedict
    # for index, (key, value) in enumerate(sequencedict.items()):
    #   print(f'{index + 1}. {key}: {userduration}')

def modifydurations():
 sequencedict=setdurations()
 wanttomodify=input("Would you like to modify any stretch durations? Y/N: ").upper()
 if wanttomodify=="Y":
  while True:
    try:
      index_to_change = int(input("Enter the index of the value to change (0 to finish): ")) - 1
      if index_to_change == -1:
        print("Modification finished.")
        break
      if 0 <= index_to_change < len(sequencedict):
          stretchtochange = list(sequencedict)[index_to_change]
          newduration = input(f"Enter the new duration for {stretchtochange}: ")
          sequencedict[stretchtochange] = newduration
          print(f"Duration of {stretchtochange} updated successfully to {newduration}.\n")
          return sequencedict
      else:
        print("Invalid index. Please enter a valid index or 0 to finish.\n")
        return sequencedict
    except ValueError:
      print("Invalid input. Please enter a valid index or 0 to finish.\n")
      # return sequencedict
 return sequencedict  

def runtimer():
  sequencedict=modifydurations()
  totallength=[]
  readytostart=input("Ready to begin? Press any key: ")
  paused=False
  for value in sequencedict.values():
    totallength.append(value)
  seqmin=(sum(totallength)//60)
  seqsec=sum(totallength)%60
  displaylength=f'{seqmin} minutes, {seqsec} seconds'
  dispayseq=("\n".join(list(sequencedict.keys())))
  print(dispayseq+"\n")
  completed=0
  remaining=len(totallength)
  starting=f'This series contains {len(totallength)} total intervals and will last {displaylength}.'
  speak(starting)
  currentsound = harpup  # Start with the first sound
  for key, value in sequencedict.items():
    if remaining!=len(totallength):
      print(f'{completed} intervals completed; {remaining} intervals remaining.\n')
    # keyboard._listener("space")
    instruction= f"Do {key}."
    print(instruction)
    speak(instruction)
    playsound(currentsound)
    currentsound=harpdown if currentsound==harpup else harpup #chatgpt did this one lol
    completed=completed+1
    remaining=remaining-1
    time.sleep(value)
    if completed==len(totallength)/2:
      halfway="You're halfway done. Congratulations—keep going!"
      speak(halfway)
    if completed==len(totallength):
      finished="Sequence completed. Congratulations!"
      print(finished)
      speak(finished)
      break

class WorkoutVideo:
  def __init__(self, title, filepath, length, bodypart, lr):
    self.title=title
    self.filepath=filepath
    self.length=length
    self.bodypart=bodypart
    self.lr=lr
    if self.bodypart=="hips":
      hipworkouts.append(self.title)
    elif self.bodypart=="abs":
      abworkouts.append(self.title)
    elif self.bodypart=="arabesque":
      arabesqueworkouts.append(self.title)
    elif self.bodypart=="butt":
      buttworkouts.append(self.title)
    elif self.bodypart=="inner thighs":
      innerthighworkouts.append(self.title)

hipworkouts=[]
abworkouts=[]
arabesqueworkouts=[]
buttworkouts=[]
innerthighworkouts=[]

#Hip workouts
hips1=WorkoutVideo("Hips 1", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Hips 1.mp4", "4:03", "hips", 1)
hips2=WorkoutVideo("Hips 2", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Hips 2.mp4", "5;15", "hips", 1)
hips3=WorkoutVideo("Hips 3", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Hips 3.mp4", "4:10", "hips", 1)

#butt workouts
butt1=WorkoutVideo("Butt 1", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Booty 1.mp4", "3:36", "butt", 1)
butt2=WorkoutVideo("Butt 2", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Booty 2.mp4", "8:08", "butt", 0)

#ab workouts
abs1=WorkoutVideo("Abs 1", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Abs 1.mp4", "5:15", "abs", 0)
abs2=WorkoutVideo("Abs 2", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Abs 2.mp4", "5:08", "abs", 0)
abs3=WorkoutVideo("Abs 3", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Abs 3.mp4", "5:07", "abs", 0)
abs4=WorkoutVideo("Abs 4", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Abs 4.mp4", "5:08", "abs", 0)
abs2=WorkoutVideo("Abs 5", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Abs 5.mp4", "5:08", "abs", 0)

#arabesque workouts
arabesque1=WorkoutVideo("Arabesque 1", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Arabesque 1.mp4", "5:03", "arabesque", 0)

# inner thigh workouts
innerhtighs1=WorkoutVideo("Inner Thighs 1", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Inner Thighs 1.mp4", "6:37", "inner thighs", 0)
innerhtighs2=WorkoutVideo("Inner Thighs 2", "/Users/hayleydeberry/Desktop/PROJECT/WORKOUT VIDEOS/Inner Thighs 2.mp4", "4:26", "inner thighs", 0)


def hipschoice():
  hipselection=random.choices(hipworkouts)
  return hipselection

def abschoice():
  abselection=random.choices(abworkouts)
  return abselection

def arabesquechoice():
  arabesqueselection=random.choices(arabesqueworkouts)
  return arabesqueselection

def buttchoice():
  buttselection=random.choices(buttworkouts)
  return buttselection

def innerthighchoice():
  innerthighselection=random.choices(innerthighworkouts)
  return innerthighselection

def buildworkout(*args):
  workoutlist=[]
  if "abs" in args:
    abselection=abschoice()
    workoutlist.append(abselection)
  if "hips" in args:
    hipselection=hipschoice()
    workoutlist.append(hipselection)
    workoutlist.append(hipselection)
  if "butt" in args:
    buttselection=buttchoice()
    workoutlist.append(buttselection)
    workoutlist.append(buttselection)
  return workoutlist
  

# print(buildworkout("hips", "abs"))



runtimer()