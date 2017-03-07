import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG1=26
ECHO1=20
TRIG2=19
ECHO2=16
TRIG3=13
ECHO3=12	
LED1=2
LED2=3
LED3=21
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)

def finddist(TRIG,ECHO):
	pulse_start = 0
	pulse_end = 0
	GPIO.output(TRIG, False)
	time.sleep(0.1)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
 	 pulse_start = time.time()
	while GPIO.input(ECHO)==1:
	 pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance=round(distance,2)
	return distance

while 1:
	dist1=[None]*3
	dist1[0]=finddist(TRIG1,ECHO1)
	time.sleep(0.1)
	dist1[1]=finddist(TRIG1,ECHO1)
	time.sleep(0.1)
	dist1[2]=finddist(TRIG1,ECHO1)
	time.sleep(0.1)
	if dist1[0]<=30:
		sum1=0
		avg1=0	
		sum1=sum1+dist1[0]
		sum1=sum1+dist1[1]
		sum1=sum1+dist1[2]
		print "sum", sum1
		avg1=sum1/3
	else:
		avg1=dist1[0]
	print "avg1",avg1
	print "dist1[0]",dist1[0]
	print "dist1[1]",dist1[1]
	print "dist1[2]",dist1[2]
	dist2=[None]*3
	dist2[0]=finddist(TRIG2,ECHO2)
	time.sleep(0.1)
	dist2[1]=finddist(TRIG2,ECHO2)
	time.sleep(0.1)
	dist2[2]=finddist(TRIG2,ECHO2)
	time.sleep(0.1)
	if dist2[0]<=30:
		sum2=0
		avg2=0
		sum2=sum2+dist2[0]
		sum2=sum2+dist2[1]
		sum2=sum2+dist2[2]
		print "sum", sum2
		avg2=sum2/3
	else:
		avg2=dist2[0]
	print "avg2",avg2
	print "dist2[0]",dist2[0]
	print "dist2[1]",dist2[1]
	print "dist2[2]",dist2[2]
	dist3=[None]*3
	dist3[0]=finddist(TRIG3,ECHO3)
	time.sleep(0.1)
	dist3[1]=finddist(TRIG3,ECHO3)
	time.sleep(0.1)
	dist3[2]=finddist(TRIG3,ECHO3)
	time.sleep(0.1)
	if dist3[0]<=30:
		sum3=0
		avg3=0	
		sum3=sum3+dist3[0]
		sum3=sum3+dist3[1]
		sum3=sum3+dist3[2]
		print "sum3", sum3
		avg3=sum3/3
	else:
		avg3=dist3[0]
	print "avg3",avg3
	print "dist3[0]",dist3[0]
	print "dist3[1]",dist3[1]
	print "dist3[2]",dist3[2]
	if avg1<=30:
		GPIO.output(LED1,1)
	else:
		GPIO.output(LED1,0)
	if avg2<=30:
		GPIO.output(LED2,1)
	else:
		GPIO.output(LED2,0)	
	if avg3<=30:
		GPIO.output(LED3,1)
	else:
		GPIO.output(LED3,0)	
	for i in range (0,3):
		dist1[i]=0
		dist2[i]=0
		dist3[i]=0