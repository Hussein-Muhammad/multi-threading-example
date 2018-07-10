####################################
# Task   : Multi-Threading example # 
# Author : Hussein Muhammad        #
# Date   : 10 / 3 / 2018           #
####################################


import threading
import time


clean_data = []  #Global_variable

class myThread (threading.Thread):  #inherit from Thread class in threading module
  thread_counter = 0   #static variable to count objects from the class (every object is of for this class is a thread )
  def __init__(self, task, threadID=thread_counter):
      threading.Thread.__init__(self)  	#call the super class(parent class) constructor
      self.threadID = threadID
      self.task = task
      thread_counter+=1    
      
  def run(self):
    if self.task is "average":
        avg = 0
        for num in clean_data:
            avg += float(num)
        while True:
            print("the average is : " ,avg/len(clean_data))
            time.sleep(2)  #delay to let user show all output

    elif self.task is "minimum":
        while True:
            print("the minimum is : " ,min(clean_data))
            time.sleep(2)  #delay to let user show all output
    elif self.task is "maximum":
        while True:
            print("the maximum is : " ,max(clean_data))
            time.sleep(2)  #delay to let user show all output
    else:
        print("Sorry undifiend task")
###***              END OF CLASS              ***###

data = input("please enter numbers in a line separated by space  ")
data = list(data.split(" "))  #split string at each space then put them in the list called data
clean_data = [float(i) for i in data]  # for every string item in the list return a converted copy to float from it
print("your data",clean_data)  # show the data after cleaning(convert it to suitable format i can process on it)
thread1 = myThread("average")  # creat object from myThread class and set its "task" attribute value with "average"
thread2 = myThread("minimum")  # creat object from myThread class and set its "task" attribute value with "minimum" 
thread3 = myThread("maximum")  # creat object from myThread class and set its "task" attribute value with "maximum"
thread1.start()  #start the thread (start is inherited from super class we now know that because we didn't implement it)
thread2.start()
thread3.start()
