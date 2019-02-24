import subprocess
import threading
import queue
import os
import time
import json


class ffmpegs:
    def __init__(self, nworrkers):
        self.num = nworrkers
        self.q = queue.Queue()

    def ffprobe(self, file):
        meta_data = subprocess.check_output(['ffprobe', '-v', 'warning',
                                             '-print_format', 'json',
                                             '-show_streams',
                                             '-show_format',
                                             file])
        return json.loads(meta_data)

    def work(self):
        start = time.time()
        ths = []
        for i in range(self.num):
            thread_convert = threading.Thread(target=self.convert)
            ths.append(thread_convert)
            thread_convert.start()
            print("there are %d threads are running." %
                  threading.active_count())
        for th in ths:
            th.join()
        print('finished in total', time.time() - start, 'seconds')

    def create_tasks(self):
        files = os.listdir()
        for file in files:
            name = file.split('.')
            if name[-1] == 'mp4' or name[-1] == 'mov':
                task = [
                    'ffmpeg', '-i', file,
                    '-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', '480p_'+file,
                    '-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', '720p_'+file
                ]
                self.q.put(task)

    def convert(self):
        print(threading.currentThread().getName() + "is created!")
        if not self.q.empty():
            subprocess.call(self.q.get())
        self.q.task_done


def main():
    ff = ffmpegs(4)
    ff.create_tasks()
    ff.work()


if __name__ == "__main__":
    main()
