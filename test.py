import mido
import time

note = []
time = []


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
    for i, track in enumerate(mid.tracks):
        # print('Track {}:{}'.format(i, track.name))
        for msg in track:
            if msg.type == 'set_tempo':
                bpm = int(mido.tempo2bpm(msg.tempo))
            if msg.type == 'note_on':
                note.append(msg.note - 20)  # note减去20 MIDI note number =>Key number (Piano)
                time.append(msg.time)
    print(note)
    print(time)
    # print("bpm "+str(bpm))

def send_msg2(song):
    # 返回midi对象
    # 这里调用了mido的库里MidiFile（）方法。
    # 并把文件名＂tset.mid＂传了进去。
    # 这里返回的mid就包含了所读取＂tset.mid”的所有信息，
    # mid这个名字是我们自己起的，然后他就包含了midi文件的信息，以后操作它就行了。
    # 其实实现方法大概是用到了类的思想，以后mid这个变里就是类了，他有很多操作函数.通过点来调用。
    mid = mido.MidiFile(song)
    # out=mid.tracks
    # 下面是一个循环，然后就是操作mid这个变量，调用tracks方法，这里tracks代表了音轨的东西，每条音轨通常情况下就是一个乐器。
    for i, track in enumerate(mid.tracks):
        print('Track {}:{}'.format(i, track.name))
        for msg in track:
            print(msg)

    # print("bpm "+str(bpm))

def rm_odd(list):
    for i in range(len(list) - 2):
        list.pop(i)
        i += 2
        if i > len(list):
            return 0


if __name__ == '__main__':
    # setup()    实际操作时去掉
    song = input('song?') + '.mid'
    method=input('method')
    if method=='1':
        send_msg(song)
    else:
        send_msg2(song)
    rm_odd(note)
