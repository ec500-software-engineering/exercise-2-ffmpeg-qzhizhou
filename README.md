# FFMPEG Exercise by Zhizhou Qiu    

## To run the conversion:
```
python3 main.py
```
## To run the test:
```
python3 test.py
```
## Explaination:    
def ffprobe() is used to check whether the conversion is succeeded or not.        
def create_task() is used to get files name in current dictionary and creat related tasks into queue.     
def work() is used to create threads according input number.     
def convert() is used to convert the videos       

## Estimation:
When I used 10 threads to convert 10 videos at the same time, it comsumed almost 400% CPU resource. So I guessed if I doubled the number task, this may crash my computer.

