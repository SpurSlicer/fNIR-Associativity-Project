# Import key parts of the PsychoPy library:
from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard
from psychopy.visual import ShapeStim
from pylsl import StreamInfo, StreamOutlet
import os

# Creates base objects:
win = visual.Window(size=(1000,800), monitor='testapp', units="pix")
kb = keyboard.Keyboard()
keys = kb.getKeys()
mouse = event.Mouse()

# Other vars
screen_number = 0
cpt = sum([len(files) for r, d, files in os.walk("data")])
filename = 'person' + str(cpt) +  '.txt'
file = os.path.join('data', filename)
fp = open(file, 'w')
timer = core.CountdownTimer(0)

# FNIRs vars
info = StreamInfo(name="Trigger", type="Markers", channel_count=1, channel_format='int32', source_id="Aurora")
outlet = StreamOutlet(info)

# Shape renders
s1 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, 250), size=(50,50), alignment='center', color='black', fillColor='white')
s2 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, 150), size=(50,50), alignment='center', color='black', fillColor='white')
s3 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, 50), size=(50,50), alignment='center', color='black', fillColor='white')
s4 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, -50), size=(50,50), alignment='center', color='black', fillColor='white')
s5 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, -150), size=(50,50), alignment='center', color='black', fillColor='white')
s6 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(-450, -250), size=(50,50), alignment='center', color='black', fillColor='white')
s7 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, 250), size=(50,50), alignment='center', color='black', fillColor='white')
s8 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, 150), size=(50,50), alignment='center', color='black', fillColor='white')
s9 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, 50), size=(50,50), alignment='center', color='black', fillColor='white')
s10 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, -50), size=(50,50), alignment='center', color='black', fillColor='white')
s11 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, -150), size=(50,50), alignment='center', color='black', fillColor='white')
s12 = visual.TextBox2(win, text="", font="Open Sans", letterHeight=20, pos=(0, -250), size=(50,50), alignment='center', color='black', fillColor='white')
###SEQUENCE 0 OBJS###
msg1 = visual.TextBox2(win,
    text="Hello! Thank you for helping participate in this study! By continuig, you agree to an arbitrary TOS.",
    font="Open Sans", letterHeight=30,
    pos=(0, 100), size=(1000,800), alignment='center')
buttonMsg1 = visual.TextBox2(win,
    text="Continue & Agree",
    font="Open Sans", letterHeight=20,
    pos=(0,0), size=(200,50), lineSpacing=1, fillColor='blue',
    borderColor='darkmagenta', anchor='center', alignment='center')
    
##SEQUENCE 1 OBJS###
msg2 = visual.TextBox2(win,
    text="Please enter your name:",
    font="Open Sans", letterHeight=30,
    pos=(0, 250), size=(1000,800), alignment='center')
inputmsg1 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(0, 150), size=(600,50), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
msg3 = visual.TextBox2(win,
    text="Please enter your age:",
    font="Open Sans", letterHeight=30,
    pos=(0, -50), size=(1000,800), alignment='center')
inputmsg2 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(0, -150), size=(600,50), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
buttonMsg2 = visual.TextBox2(win,
    text="Continue",
    font="Open Sans", letterHeight=20,
    pos=(0,-300), size=(150,50), lineSpacing=1, fillColor='blue',
    borderColor='darkmagenta', anchor='center', alignment='center')
###SEQUENCE 2 OBJS###
msg4 = visual.TextBox2(win,
    text="Now you will be given 12 Chinese characters with no paper and a 1min time limit for memorization. When you click continue, you will be brought to a screen to study and learn the characters and the timer will begin. You will then be brought to a 30-second waiting screen followed by a 1min examanation. Good luck!",
    font="Open Sans", letterHeight=30,
    pos=(0, 200), size=(1000,800), alignment='center')
###SEQUENCE 3 OBJS###
NM1 = visual.ImageStim(win, image='assets/NM/NM1.png', pos=(-366,266), anchor='center', size=(200,200))
NM2 = visual.ImageStim(win, image='assets/NM/NM2.png', pos=(-133,266), anchor='center', size=(200,200))
NM3 = visual.ImageStim(win, image='assets/NM/NM3.png', pos=(100,266), anchor='center', size=(200,200))
NM4 = visual.ImageStim(win, image='assets/NM/NM4.png', pos=(333,266), anchor='center', size=(200,200))
NM5 = visual.ImageStim(win, image='assets/NM/NM5.png', pos=(-366,30), anchor='center', size=(200,200))
NM6 = visual.ImageStim(win, image='assets/NM/NM6.png', pos=(-133,30), anchor='center', size=(200,200))
NM7 = visual.ImageStim(win, image='assets/NM/NM7.png', pos=(100,30), anchor='center', size=(200,200))
NM8 = visual.ImageStim(win, image='assets/NM/NM8.png', pos=(333,30), anchor='center', size=(200,200))
NM9 = visual.ImageStim(win, image='assets/NM/NM9.png', pos=(-366,-206), anchor='center', size=(200,200))
NM10 = visual.ImageStim(win, image='assets/NM/NM10.png', pos=(-133,-206), anchor='center', size=(200,200))
NM11 = visual.ImageStim(win, image='assets/NM/NM11.png', pos=(100,-206), anchor='center', size=(200,200))
NM12 = visual.ImageStim(win, image='assets/NM/NM12.png', pos=(333,-206), anchor='center', size=(200,200))
def renderNMImages():
    NM1.draw()
    NM2.draw()
    NM3.draw()
    NM4.draw()
    NM5.draw()
    NM6.draw()
    NM7.draw()
    NM8.draw()
    NM9.draw()
    NM10.draw()
    NM11.draw()
    NM12.draw()
    return

###SEQUENCE 4 OBJS###
msg5 = visual.TextBox2(win,
    text="Please enter the English meaning of each character!",
    font="Open Sans", letterHeight=30,
    pos=(0, 350), size=(1000,200), alignment='center')
ic1 = visual.TextBox2(win,
    text="喝",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 250), size=(110,110), alignment='center', color='black')
ic2 = visual.TextBox2(win,
    text="日",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 150), size=(110,110), alignment='center', color='black')
ic3 = visual.TextBox2(win,
    text="口",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 50), size=(110,110), alignment='center', color='black')
ic4 = visual.TextBox2(win,
    text="坐",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -50), size=(110,110), alignment='center', color='black')
ic5 = visual.TextBox2(win,
    text="山",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -150), size=(110,110), alignment='center', color='black')
ic6 = visual.TextBox2(win,
    text="开",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -250), size=(110,110), alignment='center', color='black')
ic7 = visual.TextBox2(win,
    text="小",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 250), size=(110,110), alignment='center', color='black')
ic8 = visual.TextBox2(win,
    text="飞",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 150), size=(110,110), alignment='center', color='black')
ic9 = visual.TextBox2(win,
    text="人",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 50), size=(110,110), alignment='center', color='black')
ic10 = visual.TextBox2(win,
    text="吃",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -50), size=(110,110), alignment='center', color='black')
ic11 = visual.TextBox2(win,
    text="天",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -150), size=(110,110), alignment='center', color='black')
ic12 = visual.TextBox2(win,
    text="川",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -250), size=(110,110), alignment='center', color='black')
tb1 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb2 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb3 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb4 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb5 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb6 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb7 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb8 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb9 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb10 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb11 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
tb12 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')

def tbtest():
    arr = [0,0,0,0,0,0,0,0,0,0,0,0]
    flag = True
#TB1
    if (len(tb1.text) > 0):
        tb1.borderColor='green'
        arr[0] = 1
    else:
        tb1.borderColor='red'
        arr[0] = 0
#TB2
    if (len(tb2.text) > 0):
        tb2.borderColor='green'
        arr[1] = 1
    else:
        tb2.borderColor='red'
        arr[1] = 0
#TB3
    if (len(tb3.text) > 0):
        tb3.borderColor='green'
        arr[2] = 1
    else:
        tb3.borderColor='red'
        arr[2] = 0
#TB4
    if (len(tb4.text) > 0):
        tb4.borderColor='green'
        arr[3] = 1
    else:
        tb4.borderColor='red'
        arr[3] = 0
#TB5
    if (len(tb5.text) > 0):
        tb5.borderColor='green'
        arr[4] = 1
    else:
        tb5.borderColor='red'
        arr[4] = 0
#TB6
    if (len(tb6.text) > 0):
        tb6.borderColor='green'
        arr[5] = 1
    else:
        tb6.borderColor='red'
        arr[5] = 0
#TB7
    if (len(tb7.text) > 0):
        tb7.borderColor='green'
        arr[6] = 1
    else:
        tb7.borderColor='red'
        arr[6] = 0
#TB8
    if (len(tb8.text) > 0):
        tb8.borderColor='green'
        arr[7] = 1
    else:
        tb8.borderColor='red'
        arr[7] = 0
#TB9
    if (len(tb9.text) > 0):
        tb9.borderColor='green'
        arr[8] = 1
    else:
        tb9.borderColor='red'
        arr[8] = 0
#TB10
    if (len(tb10.text) > 0):
        tb10.borderColor='green'
        arr[9] = 1
    else:
        tb10.borderColor='red'
        arr[9] = 0
#TB11
    if (len(tb11.text) > 0):
        tb11.borderColor='green'
        arr[10] = 1
    else:
        tb11.borderColor='red'
        arr[10] = 0
#TB12
    if (len(tb12.text) > 0):
        tb12.borderColor='green'
        arr[11] = 1
    else:
        tb12.borderColor='red'
        arr[11] = 0
#Continue
    for i in arr:
        if not i:
            flag = False
            break
    if flag:
        buttonMsg5.draw()
        #return True
    #return False
    return

def renderics():
    s1.draw()
    s2.draw()
    s3.draw()
    s4.draw()
    s5.draw()
    s6.draw()
    s7.draw()
    s8.draw()
    s9.draw()
    s10.draw()
    s11.draw()
    s12.draw()
    ic1.draw()
    ic2.draw()
    ic3.draw()
    ic4.draw()
    ic5.draw()
    ic6.draw()
    ic7.draw()
    ic8.draw()
    ic9.draw()
    ic10.draw()
    ic11.draw()
    ic12.draw()
    tb1.draw()
    tb2.draw()
    tb3.draw()
    tb4.draw()
    tb5.draw()
    tb6.draw()
    tb7.draw()
    tb8.draw()
    tb9.draw()
    tb10.draw()
    tb11.draw()
    tb12.draw()
def grade():
    fp.write("\n---Non Mnemonic Answers---\n")
    fp.write(tb1.text + "\n")
    fp.write(tb2.text + "\n")
    fp.write(tb3.text + "\n")
    fp.write(tb4.text + "\n")
    fp.write(tb5.text + "\n")
    fp.write(tb6.text + "\n")
    fp.write(tb7.text + "\n")
    fp.write(tb8.text + "\n")
    fp.write(tb9.text + "\n")
    fp.write(tb10.text + "\n")
    fp.write(tb11.text + "\n")
    fp.write(tb12.text + "\n")
    fp.write("--------------------------\n")
    score = 0
    if (tb1.text.lower().__contains__("drink")):
        score += 1
    if (tb2.text.lower().__contains__("sun") or tb2.text.lower().__contains__("day")):
        score += 1
    if (tb3.text.lower().__contains__("mouth")):
        score += 1
    if (tb4.text.lower().__contains__("sit")):
        score += 1
    if (tb5.text.lower().__contains__("mountain")):
        score += 1
    if (tb6.text.lower().__contains__("open")):
        score += 1
    if (tb7.text.lower().__contains__("small")):
        score += 1
    if (tb8.text.lower().__contains__("fly")):
        score += 1
    if (tb9.text.lower().__contains__("person")):
        score += 1
    if (tb10.text.lower().__contains__("eat")):
        score += 1
    if (tb11.text.lower().__contains__("sky")):
        score += 1
    if (tb12.text.lower().__contains__("river")):
        score += 1
    fp.write("Score: " + str((score/12)*100) + "\n")
###SEQUENCE 5 OBJS###
msg6 = visual.TextBox2(win,
    text="Now you will be given 12 Chinese characters with mnemonic devices, no paper, and no time limit--though you will be timed. When you click continue, you will be brought to a screen to study and learn the characters. When you click next, you will be examined on them. Good luck!",
    font="Open Sans", letterHeight=30,
    pos=(0, 200), size=(1000,800), alignment='center')
###SEQUENCE 6 OBJS###
#'''
M1 = visual.ImageStim(win, image='assets/CM/CM1.png', pos=(325,325), anchor='center', size=(300,120))
M2 = visual.ImageStim(win, image='assets/CM/CM2.png', pos=(0,325), anchor='center', size=(300,120))
M3 = visual.ImageStim(win, image='assets/CM/CM3.png', pos=(-325,325), anchor='center', size=(300,120))
M4 = visual.ImageStim(win, image='assets/CM/CM4.png', pos=(325,175), anchor='center', size=(300,120))
M5 = visual.ImageStim(win, image='assets/CM/CM5.png', pos=(0,175), anchor='center', size=(300,120))
M6 = visual.ImageStim(win, image='assets/CM/CM6.png', pos=(-325,175), anchor='center', size=(300,120))
M7 = visual.ImageStim(win, image='assets/CM/CM7.png', pos=(325,25), anchor='center', size=(300,120))
M8 = visual.ImageStim(win, image='assets/CM/CM8.png', pos=(0,25), anchor='center', size=(300,120))
M9 = visual.ImageStim(win, image='assets/CM/CM9.png', pos=(-325,25), anchor='center', size=(300,120))
M10 = visual.ImageStim(win, image='assets/CM/CM10.png', pos=(325,-125), anchor='center', size=(300,120))
M11 = visual.ImageStim(win, image='assets/CM/CM11.png', pos=(0,-125), anchor='center', size=(300,120))
M12 = visual.ImageStim(win, image='assets/CM/CM12.png', pos=(-325,-125), anchor='center', size=(300,120))
'''
M1 = visual.ImageStim(win, image='assets/M/M1.png', pos=(325,325), anchor='center', size=(300,120))
M2 = visual.ImageStim(win, image='assets/M/M2.png', pos=(0,325), anchor='center', size=(300,120))
M3 = visual.ImageStim(win, image='assets/M/M3.png', pos=(-325,325), anchor='center', size=(300,120))
M4 = visual.ImageStim(win, image='assets/M/M4.png', pos=(325,175), anchor='center', size=(300,120))
M5 = visual.ImageStim(win, image='assets/M/M5.png', pos=(0,175), anchor='center', size=(300,120))
M6 = visual.ImageStim(win, image='assets/M/M6.png', pos=(-325,175), anchor='center', size=(300,120))
M7 = visual.ImageStim(win, image='assets/M/M7.png', pos=(325,25), anchor='center', size=(300,120))
M8 = visual.ImageStim(win, image='assets/M/M8.png', pos=(0,25), anchor='center', size=(300,120))
M9 = visual.ImageStim(win, image='assets/M/M9.png', pos=(-325,25), anchor='center', size=(300,120))
M10 = visual.ImageStim(win, image='assets/M/M10.png', pos=(325,-125), anchor='center', size=(300,120))
M11 = visual.ImageStim(win, image='assets/M/M11.png', pos=(0,-125), anchor='center', size=(300,120))
M12 = visual.ImageStim(win, image='assets/M/M12.png', pos=(-325,-125), anchor='center', size=(300,120))
'''
def renderMImages():
    M1.draw()
    M2.draw()
    M3.draw()
    M4.draw()
    M5.draw()
    M6.draw()
    M7.draw()
    M8.draw()
    M9.draw()
    M10.draw()
    M11.draw()
    M12.draw()
    return
###SEQUENCE 7 OBJS###
msg7 = visual.TextBox2(win,
    text="Please enter the English meaning of each character!",
    font="Open Sans", letterHeight=30,
    pos=(0, 350), size=(1000,200), alignment='center')
mic1 = visual.TextBox2(win,
    text="鱼",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 250), size=(110,110), alignment='center', color='black')
mic2 = visual.TextBox2(win,
    text="看",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 150), size=(110,110), alignment='center', color='black')
mic3 = visual.TextBox2(win,
    text="瓜",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, 50), size=(110,110), alignment='center', color='black')
mic4 = visual.TextBox2(win,
    text="田",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -50), size=(110,110), alignment='center', color='black')
mic5 = visual.TextBox2(win,
    text="马",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -150), size=(110,110), alignment='center', color='black')
mic6 = visual.TextBox2(win,
    text="雨",
    font="DFKai-SB", letterHeight=50,
    pos=(-450, -250), size=(110,110), alignment='center', color='black')
mic7 = visual.TextBox2(win,
    text="学",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 250), size=(110,110), alignment='center', color='black')
mic8 = visual.TextBox2(win,
    text="说",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 150), size=(110,110), alignment='center', color='black')
mic9 = visual.TextBox2(win,
    text="填",
    font="DFKai-SB", letterHeight=50,
    pos=(0, 50), size=(110,110), alignment='center', color='black')
mic10 = visual.TextBox2(win,
    text="牛",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -50), size=(110,110), alignment='center', color='black')
mic11 = visual.TextBox2(win,
    text="想",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -150), size=(110,110), alignment='center', color='black')
mic12 = visual.TextBox2(win,
    text="唱",
    font="DFKai-SB", letterHeight=50,
    pos=(0, -250), size=(110,110), alignment='center', color='black')
mtb1 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb2 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb3 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, 50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb4 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb5 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb6 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(-235, -250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb7 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb8 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb9 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, 50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb10 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -50), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb11 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -150), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')
mtb12 = visual.TextBox2(win,
    text="",
    font="Open Sans", letterHeight=20,
    pos=(215, -250), size=(375,48), lineSpacing=1, fillColor='white',
    borderColor='red', anchor='center', alignment='left', editable=True, color='black')

def mtbtest():
    arr = [0,0,0,0,0,0,0,0,0,0,0,0]
#MTB1
    if (len(mtb1.text) > 0):
        mtb1.borderColor='green'
        arr[0] = 1
    else:
        mtb1.borderColor='red'
        arr[0] = 0
#MTB2
    if (len(mtb2.text) > 0):
        mtb2.borderColor='green'
        arr[1] = 1
    else:
        mtb2.borderColor='red'
        arr[1] = 0
#MTB3
    if (len(mtb3.text) > 0):
        mtb3.borderColor='green'
        arr[2] = 1
    else:
        mtb3.borderColor='red'
        arr[2] = 0
#MTB4
    if (len(mtb4.text) > 0):
        mtb4.borderColor='green'
        arr[3] = 1
    else:
        mtb4.borderColor='red'
        arr[3] = 0
#MTB5
    if (len(mtb5.text) > 0):
        mtb5.borderColor='green'
        arr[4] = 1
    else:
        mtb5.borderColor='red'
        arr[4] = 0
#MTB6
    if (len(mtb6.text) > 0):
        mtb6.borderColor='green'
        arr[5] = 1
    else:
        mtb6.borderColor='red'
        arr[5] = 0
#MTB7
    if (len(mtb7.text) > 0):
        mtb7.borderColor='green'
        arr[6] = 1
    else:
        mtb7.borderColor='red'
        arr[6] = 0
#MTB8
    if (len(mtb8.text) > 0):
        mtb8.borderColor='green'
        arr[7] = 1
    else:
        mtb8.borderColor='red'
        arr[7] = 0
#MTB9
    if (len(mtb9.text) > 0):
        mtb9.borderColor='green'
        arr[8] = 1
    else:
        mtb9.borderColor='red'
        arr[8] = 0
#MTB10
    if (len(mtb10.text) > 0):
        mtb10.borderColor='green'
        arr[9] = 1
    else:
        mtb10.borderColor='red'
        arr[9] = 0
#MTB11
    if (len(mtb11.text) > 0):
        mtb11.borderColor='green'
        arr[10] = 1
    else:
        mtb11.borderColor='red'
        arr[10] = 0
#MTB12
    if (len(mtb12.text) > 0):
        mtb12.borderColor='green'
        arr[11] = 1
    else:
        mtb12.borderColor='red'
        arr[11] = 0
    return 

def mrenderics():
    s1.draw()
    s2.draw()
    s3.draw()
    s4.draw()
    s5.draw()
    s6.draw()
    s7.draw()
    s8.draw()
    s9.draw()
    s10.draw()
    s11.draw()
    s12.draw()
    mic1.draw()
    mic2.draw()
    mic3.draw()
    mic4.draw()
    mic5.draw()
    mic6.draw()
    mic7.draw()
    mic8.draw()
    mic9.draw()
    mic10.draw()
    mic11.draw()
    mic12.draw()
    mtb1.draw()
    mtb2.draw()
    mtb3.draw()
    mtb4.draw()
    mtb5.draw()
    mtb6.draw()
    mtb7.draw()
    mtb8.draw()
    mtb9.draw()
    mtb10.draw()
    mtb11.draw()
    mtb12.draw()
def mgrade():
    fp.write("\n---Mnemonic Answers---\n")
    fp.write(mtb1.text + "\n")
    fp.write(mtb2.text + "\n")
    fp.write(mtb3.text + "\n")
    fp.write(mtb4.text + "\n")
    fp.write(mtb5.text + "\n")
    fp.write(mtb6.text + "\n")
    fp.write(mtb7.text + "\n")
    fp.write(mtb8.text + "\n")
    fp.write(mtb9.text + "\n")
    fp.write(mtb10.text + "\n")
    fp.write(mtb11.text + "\n")
    fp.write(mtb12.text + "\n")
    fp.write("--------------------------\n")
    score = 0
    if (mtb1.text.lower().__contains__("fish")):
        score += 1
    if (mtb2.text.lower().__contains__("look") or mtb2.text.lower().__contains__("see")):
        score += 1
    if (mtb3.text.lower().__contains__("melon")):
        score += 1
    if (mtb4.text.lower().__contains__("field")):
        score += 1
    if (mtb5.text.lower().__contains__("horse")):
        score += 1
    if (mtb6.text.lower().__contains__("rain")):
        score += 1
    if (mtb7.text.lower().__contains__("learn")):
        score += 1
    if (mtb8.text.lower().__contains__("speak") or mtb8.text.lower().__contains__("say")):
        score += 1
    if (mtb9.text.lower().__contains__("fill")):
        score += 1
    if (mtb10.text.lower().__contains__("cow")):
        score += 1
    if (mtb11.text.lower().__contains__("think")):
        score += 1
    if (mtb12.text.lower().__contains__("sing")):
        score += 1
    fp.write("Score: " + str((score/12)*100) + "\n")
###SEQUENCE 0 OBJS###
msg8 = visual.TextBox2(win,
    text="And that's it! Thank you so much for participating!",
    font="Open Sans", letterHeight=30,
    pos=(0, 200), size=(1000,800), alignment='center')
buttonMsg9 = visual.TextBox2(win,
    text="Exit the Study",
    font="Open Sans", letterHeight=20,
    pos=(0,0), size=(200,50), lineSpacing=1, fillColor='blue',
    borderColor='darkmagenta', anchor='center', alignment='center')
    
###OTHER OBJS###
msg9 = visual.TextBox2(win,
    text="Cool! Now wait for 30 seconds :)",
    font="Open Sans", letterHeight=30,
    pos=(0, 200), size=(1000,800), alignment='center')
#while 'escape' not in keys:
while True:
#General objects
    win.clearBuffer()
    keys = kb.getKeys()
    if (screen_number > 0):
        if 'left' in keys:
            screen_number -= 1
    if 'right' in keys:
        screen_number += 1
    if 'escape' in keys:
        break
    keys.clear()
#Screens
    if (screen_number == 0):
        buttonMsg1.draw()
        msg1.draw()
        if mouse.isPressedIn(buttonMsg1):
            screen_number += 1
    elif (screen_number == 1):
        if (len(inputmsg1.text) > 0):
            inputmsg1.borderColor='green'
        else:
            inputmsg1.borderColor='red'
        msg2.draw()
        inputmsg1.draw()
        if (len(inputmsg2.text) > 0):
            inputmsg2.borderColor='green'
        else:
            inputmsg2.borderColor='red'
        msg3.draw()
        inputmsg2.draw()
        if (len(inputmsg2.text) > 0 and len(inputmsg1.text) > 0):
            buttonMsg2.draw()
            if mouse.isPressedIn(buttonMsg2):
                screen_number += 1
                fp.write(inputmsg1.text + "\n")
                fp.write(inputmsg2.text + "\n")
                timer.reset()
                timer.addTime(30)
    elif (screen_number == 2): #explanation screen
        msg4.draw()
        if (timer.getTime() > 0):
            buttonMsg3 = visual.TextBox2(win,
                text="Continue in: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,0), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg3.draw()
        else:
            screen_number += 1 #PUSH 1
            outlet.push_sample(x=[1])
            timer.reset()
            timer.addTime(60)
    elif (screen_number == 3): #NM Char review screen
        renderNMImages()
        if (timer.getTime() > 0):
            buttonMsg4 = visual.TextBox2(win,
                text="Time Remaining: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-350), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg4.draw()
        else:
            screen_number += 1
            timer.reset()
            timer.addTime(30)
    elif (screen_number == 4): #NM Char wait screen
        msg9.draw()
        if (timer.getTime() > 0):
            buttonMsg4 = visual.TextBox2(win,
                text="Continue in: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-350), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg4.draw()
        else:
            screen_number += 1
            outlet.push_sample(x=[2]) #PUSH 2
            timer.reset()
            timer.addTime(60)
    elif (screen_number == 5): #NM Char exam screen
        msg5.draw()
        renderics()
        tbtest()
        if (timer.getTime() > 0):
            buttonMsg5 = visual.TextBox2(win,
                text="Time Remaining: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-350), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg5.draw()
        else:
            screen_number += 1
            grade()
            timer.reset()
            timer.addTime(30)
    elif (screen_number == 6): #Intermediary wait screen
        msg6.draw()
        if (timer.getTime() > 0):
            buttonMsg6 = visual.TextBox2(win,
                text="Continue in: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,0), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg6.draw()
        else:
            screen_number += 1
            outlet.push_sample(x=[3]) #PUSH 3
            timer.reset()
            timer.addTime(60)
    elif (screen_number == 7): #M Char review screen
        renderMImages()
        if (timer.getTime() > 0):
            buttonMsg7 = visual.TextBox2(win,
                text="Time Remaining: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-290), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg7.draw()
        else:
            screen_number += 1
            timer.reset()
            timer.addTime(30)
    elif (screen_number == 8): #M Char wait screen
        msg9.draw()
        if (timer.getTime() > 0):
            buttonMsg4 = visual.TextBox2(win,
                text="Continue in: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-350), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg4.draw()
        else:
            screen_number += 1
            outlet.push_sample(x=[4]) #PUSH 4
            timer.reset()
            timer.addTime(60)
    elif (screen_number == 9): #M Char exam screen
        msg7.draw()
        mrenderics()
        mtbtest()
        if (timer.getTime() > 0):
            buttonMsg8 = visual.TextBox2(win,
                text="Time Remaining: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,-350), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg8.draw()
        else:
            screen_number += 1
            mgrade()
            timer.reset()
            timer.addTime(30)
    elif (screen_number == 10): #Exit wait screen
        msg8.draw()
        if (timer.getTime() > 0):
            buttonMsg6 = visual.TextBox2(win,
                text="Exiting in: {}".format(int(timer.getTime())),
                font="Open Sans", letterHeight=20,
                pos=(0,0), size=(250,50), lineSpacing=1, fillColor='blue',
                borderColor='darkmagenta', anchor='center', alignment='center')
            buttonMsg6.draw()
        else:
            timer.reset()
            break

    else:
        screen_number = 0
    win.flip()
    
win.close()
core.quit()