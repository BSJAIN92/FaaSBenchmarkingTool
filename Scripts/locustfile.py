from locust import HttpLocust, TaskSet, task, between, TaskSequence, seq_task
import datetime, time
import os

class UserBehavior(TaskSequence):


	global requestTrigger
	global requestResponse
	global executionStartTime
	global executionEndTime
	global last_wait_time
	global counter
	global sleepDuration
	global sleepCounter

	def on_start(self):
		global last_wait_time
		global sleepCounter
		global counter
		global sleepDuration
		sleepCounter = 1
		counter = 1
		sleepDuration = 2
		last_wait_time = 0
		filepath = '../Results/' + (os.environ.get("file_name"))
		with open(filepath, 'a+') as f:
			f.write("requestTrigger" + "," + "executionStartTime" + "," + "executionEndTime" + ", "+ "requestResponse" + "," + "executionTime" + "," +"requestResponseTime" + "\n")


	@seq_task(1)
	def start(self):
		global requestTrigger
		requestTrigger = int(round(time.time() * 1000))



	@seq_task(2)
	def get_something(self):
#		global sleepDuration
#		t = datetime.datetime.now()

#		print (os.environ.get("url")+"?d="+str(sleepDuration))
#		r= self.client.get(os.environ.get("url")+"?d="+str(sleepDuration)) #Used for Sleep experiment
		r= self.client.get(os.environ.get("url"))
		#r = r.json()
		#r = r.replace("\'", "\"")
		#print(r)

		global executionStartTime
		executionStartTime = (r.json()["executionStart"])
		global executionEndTime
		executionEndTime = (r.json()["executionEnd"])


	@seq_task(3)
	def stop(self):
		global requestResponse
		global requestTrigger
		global executionStartTime
		global executionEndTime
		global last_wait_time
		global sleepDuration
		global sleepCounter
		global counter
		requestResponse = int(round(time.time() * 1000))

		filepath = '../Results/' + (os.environ.get("file_name"))

		executionTime = executionEndTime - executionStartTime
		requestResponseTime = requestResponse - requestTrigger

		with open(filepath, 'a+') as f:
			f.write(str(requestTrigger) + "," + str(executionStartTime) + "," + str(executionEndTime) + "," + str(requestResponse) + "," + str(executionTime) + "," + str(requestResponseTime) + "\n")
		
#		if (counter == 3 and sleepCounter <= 13): #Used for Sleep experiment
#			sleepCounter = sleepCounter + 1
#			counter = 1
#		else:
#			counter = counter + 1
#		sleepDuration = 2**sleepCounter
		
		last_wait_time += 60 # += 60 for Backoff Test
		time.sleep(last_wait_time)


		

class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	
	wait_time = between(0, 0)

