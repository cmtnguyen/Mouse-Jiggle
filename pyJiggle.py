import time
import threading 
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

# jiggler movement occurance
delay = 0.1
# jiggler occurs with a right-click
button = Button.right
# key to press to start or stop jiggler
start_stop_key = KeyCode(char='s')
# key to quit jiggler
exit_key = KeyCode(char='q')
mouse = Controller()
# units to move mouse
positions = [-1,1,0]

class JiggleMouse(threading.Thread):

    def __init__(self, delay, button):
        super(JiggleMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    
    def start_jiggle(self):
        self.running = True

    def stop_jiggle(self):
        self.running = False

    def exit (self):
        self.stop_jiggle()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # mouse will move selecting random units from positions array
                x = random.choice(positions)
                y = random.choice(positions)
                mouse.move(x, y)
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(.1)

jiggle_thread = JiggleMouse(delay, button)
jiggle_thread.start()

def on_press(key): 
    if key == start_stop_key: 
        if jiggle_thread.running: 
            jiggle_thread.stop_jiggle() 
        else: 
            jiggle_thread.start_jiggle() 
  
  
    elif key == exit_key: 
        jiggle_thread.exit()
        listener.stop() 
  
  
with Listener(on_press=on_press) as listener: 
    listener.join() 