import subprocess
import time

def begin_APRS_recieve():
    print("Running")
    with open("data", "w") as file:
        process = subprocess.Popen(["rtl_fm", "-f", "144.900M", "-s", "22050"], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        subprocess.Popen(["multimon-ng", "-t", "raw", "-a", "AFSK1200", "-f", "alpha", "/dev/stdin"], 
                         stdin=process.stdout, 
                         stdout=file, 
                         stderr=subprocess.PIPE)
    return process

if __name__ == '__main__':
    begin_APRS_recieve()
