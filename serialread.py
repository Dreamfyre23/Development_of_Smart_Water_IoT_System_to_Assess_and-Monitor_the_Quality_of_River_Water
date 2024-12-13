import time
from Adafruit_IO import Client
import requests
#import serial

# Configuration --/
# USB port - Adruino USB connection to PC --/
#usb_serial_port = "COM3"

ADAF_Username = 'dineshram'
ADAF_Key = 'aio_GSvf4292LhXOCUmMvSpGuP9PGpdF'

aio = Client(ADAF_Username, ADAF_Key)

# Website host address
host= "http://localhost/Water-Quality-Monitoring-System-Website/" # End url with a slash '/'

#ser = serial.Serial(usb_serial_port,9600) --/
while True:
	#getVal = ser.readline() --/
	#val = str(getVal).replace("b'","").replace("\\r\\n'","") --/
	#arr = val.split(",") --/

	#tds = (aio.receive('ch3').value)
	#turb = (aio.receive('ch4').value)
	#temp = (aio.receive('ch1').value)
	#ph = (aio.receive('ch2').value)

	#TDS = (tds.split('$'))
	#TURB = (turb.split('$'))
	#TEMP = (temp.split('$'))
	#PH = (ph.split('$'))

	arr = [0]*4
	#arr[0] = int(TEMP[0])
	#arr[1] = int(TURB[0])
	#arr[2] = int(PH[0])
	#arr[3] = float(TDS[0])
	#print(arr)

	arr[0] = 27 #temp
	arr[1] = 10 #turb
	arr[2] = 8 #pH
	arr[3] = 510.0 #tds

	print(arr)

	Wtemp = 1
	Wturb = 1
	Wph = 1
	Wtds = 1

	#Q Value for pH
	if(arr[2]<=2 or arr[2]>=12):
		Qph = 0
	elif(arr[2]==3 or arr[2]==11):
		Qph = 5
	elif(arr[2]==4):
		Qph = 10
	elif(arr[2]==10):
		Qph = 20
	elif(arr[2]==5):
		Qph = 25
	elif(arr[2]==9):
		Qph = 50
	elif(arr[2]==6):
		Qph = 75
	elif(arr[2]==8):
		Qph = 80
	elif(arr[2]==7):
		Qph = 100

	#Q Value for Temperature
	Qtemp = 100

	#Q Value for Turbidity
	if(arr[1]>=0 and arr[1]<=10):
		Qturb = 95
	elif(arr[1]<20 and arr[1]>10):
		Qturb = 70
	elif(arr[1]<30 and arr[1]>=20):
		Qturb = 55
	elif(arr[1]<40 and arr[1]>=30):
		Qturb = 49
	elif(arr[1]<50 and arr[1]>=40):
		Qturb = 42
	elif(arr[1]<60 and arr[1]>=50):
		Qturb = 35
	elif(arr[1]<70 and arr[1]>=60):
		Qturb = 32
	elif(arr[1]<80 and arr[1]>=70):
		Qturb = 27
	elif(arr[1]<90 and arr[1]>=80):
		Qturb = 22
	elif(arr[1]<=100 and arr[1]>=90):
		Qturb = 18
	else:
		Qturb = 5

	#Q Value for TDS
	if(arr[3]>=0 and arr[3]<=50):
		Qtds = 85
	elif(arr[3]<100 and arr[3]>50):
		Qtds = 95
	elif(arr[3]<150 and arr[3]>=100):
		Qtds = 80
	elif(arr[3]<200 and arr[3]>=150):
		Qtds = 75
	elif(arr[3]<250 and arr[3]>=200):
		Qtds = 68
	elif(arr[3]<300 and arr[3]>=250):
		Qtds = 63
	elif(arr[3]<350 and arr[3]>=300):
		Qtds = 55
	elif(arr[3]<400 and arr[3]>=350):
		Qtds = 50
	elif(arr[3]<450 and arr[3]>=400):
		Qtds = 42
	elif(arr[3]<=500 and arr[3]>=450):
		Qtds = 35
	elif(arr[3]>500):
		Qtds = 20

	arr[0] = Qtemp #temp
	arr[1] = Qturb #turb
	arr[2] = Qph #pH
	arr[3] = Qtds #tds
	print(arr)

	WQI = ((Qtemp*Wtemp)+(Qturb*Wturb)+(Qph*Wph)+(Qtds*Wtds))/(Wtemp+Wturb+Wph+Wtds)
	print(WQI)

	# send to web server (php) --/
	#userdata = {"temperature": arr[0], "turbidity": arr[1], "ph": arr[2], "solids": arr[3]} 
	#resp = requests.post(host + "insert_data.php", params=userdata)

	time.sleep(5)