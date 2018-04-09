from cs1graphics import *
import time
from time import sleep
import imageio
import os
import sys
_GIF_LENGTH_LIMIT = 10 # Result GIF file's length limit in seconds
_filename_base = sys.argv[0].replace('converted/', '')
_timer = 0
_count = 0
def canvas_save():
    global _filename_base
    global _timer
    global _count
    getLatestCanvas().saveToFile('./frames/%s_%d.png' % (_filename_base, _count))
    _count += 1
def sleep_and_save(t):
    global _filename_base
    global _timer
    global _count
    ct = int(t * 1000)
    for i in range(ct):
        _timer += 1
        if _timer % 100 == 0:
            canvas_save()
        if _timer >= (_GIF_LENGTH_LIMIT * 1000):
            save_and_exit()
def save_gif():
    global _filename_base
    global _count
    with imageio.get_writer('./gifs/%s.gif' % (_filename_base), mode='I', duration=0.1) as writer:
        for i in range(_count):
            image = imageio.imread('./frames/%s_%d.png' % (_filename_base, i))
            writer.append_data(image)
    for i in range(_count):
        os.remove('./frames/%s_%d.png' % (_filename_base, i))
def save_and_exit():
    canvas_save()
    save_gif()
    sys.exit(0)
time.sleep = sleep_and_save
sleep = sleep_and_save
