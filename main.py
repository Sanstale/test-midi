import mido
import time
from pinpong.board import Board, Pin, NeoPixel  # 导入neopixel类

note1 = []
note2 = []
time1 = []
time2 = []

def setup():
    Board("uno").begin()  # 初始化，选择板型(uno、leonardo、xugu)和端口号，不输入端口号则进行自动识别

    NEOPIXEL_PIN = Pin(Pin.D9)
    PIXELS_NUM = 60  # 灯数

    np = NeoPixel(NEOPIXEL_PIN, PIXELS_NUM)


def send_msg(song):
    # 返回midi对象
    # 这里调用了mido的库里MidiFile（）方法。
    # 并把文件名＂tset.mid＂传了进去。
    # 这里返回的mid就包含了所读取＂tset.mid”的所有信息，
    # mid这个名字是我们自己起的，然后他就包含了midi文件的信息，以后操作它就行了。
    # 其实实现方法大概是用到了类的思想，以后mid这个变里就是类了，他有很多操作函数.通过点来调用。
    mid = mido.MidiFile(song)
    # out=mid.tracks
    # 下面是一个循环，然后就是操作mid这个变量，调用tracks方法，这里tracks代表了音轨的东西，每条音轨通常情况下就是一个乐器。
    # for i, track in enumerate(mid.tracks):
        # print('Track {}:{}'.format(i, track.name))
    for msg in mid.tracks[0]:
        if msg.type == 'set_tempo':
            bpm = int(mido.tempo2bpm(msg.tempo))
        if msg.type == 'note_on':
            note1.append(msg.note - 20)  # note减去20 MIDI note number =>Key number (Piano)
            time1.append(msg.time)
    for msg in mid.tracks[1]:
        if msg.type == 'set_tempo':
            bpm = int(mido.tempo2bpm(msg.tempo))
        if msg.type == 'note_on':
            note2.append(msg.note - 20)  # note减去20 MIDI note number =>Key number (Piano)
            time2.append(msg.time)
    # print("bpm "+str(bpm))


def rm_odd(list):
    for i in range(len(list) - 2):
        list.pop(i)
        i += 2
        if i > len(list):
            return 0


# 用于遍历，组合成索引序列。
# 输出：Track 0：Piano 1
# 上面一个循环是输出各条音轨，一个midi文件可以是好几条音轨合成的，每条音轨有一个乐器或多个乐器。
# 下面这个循环是循环某一条音轨中的数据，输出音轨中的数据。
# 音轨中记录的一系列钢琴按键按下和弹起的操作。

if __name__ == '__main__':
    # setup()    实际操作时去掉
    # song = input()
    send_msg('test2.mid')
    rm_odd(note1)
    rm_odd(note2)
    print(note1,note2,time1,time2)
    # for i in range(len(note) // 2):
    #     np[note[i]] = (255, 0, 0)
    #     i += 1
    #     time.sleep(1)
