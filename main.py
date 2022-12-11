import mido
import time
import threading
from pinpong.board import Board, Pin, NeoPixel

note1 = []
note2 = []
time1 = []
time2 = []
ticks_per_beat = 480


# 导入相关库，并定义需要的变量


def rm_odd(list):#定义一个过滤列表多余信息的函数
    for i in range(len(list) - 2):
        list.pop(i)
        i += 2
        if i > len(list):
            return 0


class myThread(threading.Thread):  # 定义一个新的线程类，用来并行执行两个 track
    def __init__(self, note, times, tempo):
        threading.Thread.__init__(self)
        self.note = note
        self.times = times
        self.tempo = tempo

    def run(self):
        play_single_track(self.note, self.times, self.tempo)


def play_single_track(note, times, tempo):  # 定义一个函数用来播放单个 track
    for i in range(len(times) // 2):
        np[note[i]] = (255, 0, 0)

        time.sleep(mido.tick2second(times[2 * i + 1], 480, tempo))
        np[note[i]] = (0, 0, 0)

        time.sleep(mido.tick2second(times[2 * i + 2], 480, tempo))
        # if 2*i+1>=len(times):
        #     break


Board("uno").begin()

NEOPIXEL_PIN = Pin(Pin.D9)
PIXELS_NUM = 60  # 灯数

np = NeoPixel(NEOPIXEL_PIN, PIXELS_NUM)
# song = input()

mid = mido.MidiFile('test2.mid')

for msg in mid.tracks[0]:#使用 MIDI 库读取 MIDI 文件，并解析音符和时间信息
    if msg.type == 'set_tempo':
        bpm = int(mido.tempo2bpm(msg.tempo))
        tempo = msg.tempo
        # print(msg.tempo)
    if msg.type == 'note_on':
        note1.append(msg.note - 20 - 16)  # note减去20 MIDI note number =>Key number (Piano) 16是低音部
        time1.append(msg.time)
for msg in mid.tracks[1]:

    if msg.type == 'note_on':
        note2.append(msg.note - 20 - 16)  # note减去20 MIDI note number =>Key number (Piano)
        time2.append(msg.time)


rm_odd(note1)
rm_odd(note2)
print(note1, note2, time1, time2)


track1 = myThread(note1, time1, tempo)#创建两个新线程，并将解析到的音符和时间信息传入线程
track2 = myThread(note2, time2, tempo)

track1.start()#启动两个线程，实现两个 track 的同时播放
track2.start()
