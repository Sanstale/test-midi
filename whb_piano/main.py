import mido


def send_msg():
    # 返回midi对象
    # 这里调用了mido的库里MidiFile（）方法。
    # 并把文件名＂tset.mid＂传了进去。
    # 这里返回的mid就包含了所读取＂tset.mid”的所有信息，
    # mid这个名字是我们自己起的，然后他就包含了midi文件的信息，以后操作它就行了。
    # 其实实现方法大概是用到了类的思想，以后mid这个变里就是类了，他有很多操作函数.通过点来调用。
    mid = mido.MidiFile("test2.mid")
    # out=mid.tracks
    # 下面是一个循环，然后就是操作mid这个变量，调用tracks方法，这里tracks代表了音轨的东西，每条音轨通常情况下就是一个乐器。
    for i, track in enumerate(mid.tracks):
        print('Track {}:{}'.format(i, track.name))
        for msg in track:
            print(msg.time)
    # print(mid.tracks)
    # print(mid.tracks[0][5])
    # print(mid)

# 用于遍历，组合成索引序列。
# 输出：Track 0：Piano 1
# 上面一个循环是输出各条音轨，一个midi文件可以是好几条音轨合成的，每条音轨有一个乐器或多个乐器。
# 下面这个循环是循环某一条音轨中的数据，输出音轨中的数据。
# 音轨中记录的一系列钢琴按键按下和弹起的操作。
# 输出每个动作.
# 代表主函数
if __name__ == '__main__':
    send_msg()
