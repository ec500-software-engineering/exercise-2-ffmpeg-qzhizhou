import subprocess
import threading
import queue
from multiprocessing import Pool
import os
from concurrent.futures import ThreadPoolExecutor
import time


class ffmpegs:
    def __init__(self):
        self.q = queue.Queue()

    def getInput(self):
        # _q = queue.Queue()
        files = os.listdir()
        for file in files:
            name = file.split('.')
            if name[-1] == 'mp4' or name[-1] == 'mov':
                task = [
                    'ffmpeg', '-i', file,
                    '-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', '480p_'+file,
                    '-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', '720p_'+file
                ]
                # _q.put(task)
                self.q.put(task)
        # return _q

    def work(self):
        # task_list = list(self.q)
        # pool = threadpool.Threadpool(4)
        # requests = threadpool.makeRequests(self.convert, task_list)
        # [pool.putRequest(req) for req in requests]
        # start = time.time()
        # ths = []
        # for i in range(3):
        #     th = threading.Thread(target=self.convert)
        #     th.daemon = True
        #     th.start()
        #     ths.append(th)
        # print('task done')
        # for th in ths:
        #     th.join()
        # print('thread total', time.time() - start, 'seconds')
        start = time.time()
        ths = []
        for i in range(3):
            th = threading.Thread(target=self.convert)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()
        print('thread total', time.time() - start, 'seconds')

    def convert(self):
        print(threading.currentThread().getName() + "is working!")
        task = self.q.get()
        subprocess.call(task)
        self.q.task_done()


def main():
    ff = ffmpegs()
    ff.getInput()
    ff.work()
    print('main done')


if __name__ == "__main__":
    main()
