import subprocess
import threading
import queue

queue = queue.Queue()


class ffmpeg:
    def __init__(self, num):
        self.num = num
        self.thread_call = threading.Thread(target=self.work)
        self.thread_convert = threading.Thread(target=self.convert)

    def work(self):
        i = 0
        while(i < 10):
            name = ['480p_'+str(self.num)+'.mp4', '720p_'+str(self.num)+'.mp4']
            task = [
                'ffmpeg', '-i', 'video.mp4',
                '-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', name[0],
                            '-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', name[1]
            ]
            queue.put(task)
            print(threading.currentThread().getName() + "is working!")
            i = i + 1

    def convert(self):
        # if not queue.empty():
        #     subprocess.call(queue.get())
        queue.task_done
        print(threading.currentThread().getName() + "is working!")


def main():
    for i in range(3):
        ffm = ffmpeg(i)
        ffm.thread_call.start()
        ffm.thread_convert.start()
        print("procaess %d started" % i)
        ffm.thread_call.join()
        ffm.thread_convert.join()
        print("videos %d are done!" % i)
        print(threading.active_count())


if __name__ == "__main__":
    main()
