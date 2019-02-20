import subprocess
import threading
import queue


class ffmpegs:
    def __init__(self, nworrkers):
        self.num = nworrkers
        self.q = queue.Queue()

    def work(self):
        for i in range(self.num):
            thread_convert = threading.Thread(target=self.convert)
            # thread_convert.daemon = True
            thread_convert.start()
            print("there are %d threads are running." %
                  threading.active_count())

    def create_tasks(self):
        i = 0
        while(i < 10):
            name = ['480p_'+str(i)+'.mp4', '720p_'+str(i)+'.mp4']
            task = [
                'ffmpeg', '-i', 'video.mp4',
                '-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', name[0],
                            '-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', name[1]
            ]
            self.q.put(task)
            i = i + 1

    def convert(self):
        print(threading.currentThread().getName() + "is working!")
        if not self.q.empty():
            subprocess.call(self.q.get())
        self.q.task_done


def main():
    ff = ffmpegs(2)
    for i in range(10):
        ff.create_tasks()
    ff.work()


if __name__ == "__main__":
    main()
