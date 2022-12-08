import mido
import time
import threading
from pinpong.board import Board, Pin, NeoPixel  # 导入neopixel类

note1 = []
note2 = []
time1 = []
time2 = []

ticks_per_beat = 480


# tempo=0

# def send_msg(song,length):
#     # 返回midi对象
#     # 这里调用了mido的库里MidiFile（）方法。
#     # 并把文件名＂tset.mid＂传了进去。
#     # 这里返回的mid就包含了所读取＂tset.mid ”的所有信息，
#     # mid这个名字是我们自己起的，然后他就包含了midi文件的信息，以后操作它就行了。
#     # 其实实现方法大概是用到了类的思想，以后mid这个变里就是类了，他有很多操作函数.通过点来调用。
#     mid = mido.MidiFile(song)
#     # out=mid.tracks
#     # 下面是一个循环，然后就是操作mid这个变量，调用tracks方法，这里tracks代表了音轨的东西，每条音轨通常情况下就是一个乐器。
#     # for i, track in enumerate(mid.tracks):
#     # print('Track {}:{}'.format(i, track.name))
#     for msg in mid.tracks[0]:
#         if msg.type == 'set_tempo':
#             bpm = int(mido.tempo2bpm(msg.tempo))
#         if msg.type == 'note_on':
#             note1.append(msg.note - 20 - 16)  # note减去20 MIDI note number =>Key number (Piano) 16是低音部
#             time1.append(msg.time)
#     for msg in mid.tracks[1]:
#         if msg.type == 'set_tempo':
#             bpm = int(mido.tempo2bpm(msg.tempo))
#         if msg.type == 'note_on':
#             note2.append(msg.note - 20 - 16)  # note减去20 MIDI note number =>Key number (Piano)
#             time2.append(msg.time)
#     for i in mid.tracks:
#         if msg.type == 'note_on':
#             length+=1
#     # print("bpm "+str(bpm))


def rm_odd(list):
    for i in range(len(list) - 2):
        list.pop(i)
        i += 2
        if i > len(list):
            return 0

class myThread (threading.Thread):
    def __init__(self, note,times,tempo):
        threading.Thread.__init__(self)
        self.note = note
        self.times = times
        self.tempo = tempo
    def run(self):
        play_single_track(self.note,self.times,self.tempo)
def play_single_track(note,times,tempo):
    for i in range(len(times) // 2):
        np[note[i]] = (255, 0, 0)
        time.sleep(mido.tick2second(times[2 * i + 1], 480, tempo))
        np[note[i]] = (0, 0, 0)
        time.sleep(mido.tick2second(times[2 * i + 2], 480, tempo))


# 用于遍历，组合成索引序列。
# 输出：Track 0：Piano 1
# 上面一个循环是输出各条音轨，一个midi文件可以是好几条音轨合成的，每条音轨有一个乐器或多个乐器。
# 下面这个循环是循环某一条音轨中的数据，输出音轨中的数据。
# 音轨中记录的一系列钢琴按键按下和弹起的操作。


Board("uno").begin()

NEOPIXEL_PIN = Pin(Pin.D9)
PIXELS_NUM = 60  # 灯数

np = NeoPixel(NEOPIXEL_PIN, PIXELS_NUM)
# song = input()

mid = mido.MidiFile('test2.mid')

for msg in mid.tracks[0]:
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

# print("bpm "+str(bpm))
rm_odd(note1)
rm_odd(note2)
print(note1, note2, time1, time2)
# for i in range(len(time1) // 2):
#     np[note1[i]] = (255, 0, 0)
#     time.sleep(mido.tick2second(time1[2 * i + 1], ticks_per_beat, tempo))
#     np[note1[i]] = (0, 0, 0)
#     time.sleep(mido.tick2second(time1[2 * i + 2], ticks_per_beat, tempo))

track1=myThread(note1,time1,tempo)
track2=myThread(note2,time2,tempo)

track1.start()
track2.start()