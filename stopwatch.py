# simple console command stopwatch application

import time

def getTimeStamp(): 
    # prints the local time of when the stopwatch started
    print("Local Time: ", time.asctime(time.localtime(time.time())))
    return time.time() # returns timestamp

def getTime(start, stop): # return the time difference
    # get difference in seconds between start time and stop time rounded to 2nd decimal
    return round(stop - start, 2)

def main():
    # get start time timestamp
    input("Press ENTER to Start Stopwatch")
    startTime = getTimeStamp()

    # get stop time timestamp
    input("Press ENTER to Stop...")
    stopTime = getTimeStamp()

    # get the time difference between the two timestamps and print to console
    print("Time Elapsed:", getTime(startTime, stopTime), "Seconds")

if __name__ == "__main__":
    main()