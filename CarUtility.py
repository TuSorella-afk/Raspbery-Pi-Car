import RPi.GPIO as GPIO
import time
import smbus

class ADCDevice(object):
    def __init__(self):
        self.cmd = 0
        self.address = 0
        self.bus=smbus.SMBus(1)
        # print("ADCDevice init")

    def detectI2C(self,addr):
        try:
            self.bus.write_byte(addr,0)
            print("Found device in address 0x%x"%(addr))
            return True
        except:
            print("Not found device in address 0x%x"%(addr))
            return False

    def close(self):
        self.bus.close()

class PCF8591(ADCDevice):
    def __init__(self):
        super(PCF8591, self).__init__()
        self.cmd = 0x40     # The default command for PCF8591 is 0x40.
        self.address = 0x48 # 0x48 is the default i2c address for PCF8591 Module.

    def analogRead(self, chn): # PCF8591 has 4 ADC input pins, chn:0,1,2,3
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        return value

    def analogWrite(self,value): # write DAC value
        self.bus.write_byte_data(address,cmd,value)	

class ADS7830(ADCDevice):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.cmd = 0x84
        self.address = 0x4b # 0x4b is the default i2c address for ADS7830 Module.

    def analogRead(self, chn): # ADS7830 has 8 ADC input pins, chn:0,1,2,3,4,5,6,7
        value = self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
        return value

#____________________________________________________________________________________
class Sonar():
    def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        pulseTime = (time.time() - t0)*1000000
        return pulseTime

    def getSonar(trigPin, echoPin, timeOut):     # get the measurement results of ultrasonic module,with unit: cm
        GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level
        time.sleep(0.00001)     # 10us
        GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level
        pingTime = Sonar.pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s
        return distance

    def getDistance(trigPin, echoPin, MAX_DISTANCE):
        timeOut = MAX_DISTANCE * 60
        GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
        GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
        GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode
        while(True):
            distance = Sonar.getSonar(trigPin, echoPin, timeOut) # get distance
            return distance
class Fari():
    def setup(ledPin):
        global adc
        adc = ADCDevice()
        if(adc.detectI2C(0x48)): # Detect the pcf8591.
            adc = PCF8591()
        elif(adc.detectI2C(0x4b)): # Detect the ads7830
            adc = ADS7830()
        else:
            print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n");
            exit(-1)
        global p
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ledPin,GPIO.OUT)   # set ledPin to OUTPUT mode
        GPIO.output(ledPin,GPIO.LOW)

        p = GPIO.PWM(ledPin,1000) # set PWM Frequence to 1kHz
        p.start(0)

    def getFari():
        value = adc.analogRead(0)    # read the ADC value of channel 0
        time.sleep(1)
        if value < 120:
            p.ChangeDutyCycle(0)
        elif value > 120:
            p.ChangeDutyCycle(100)
        voltage = value / 255.0 * 3.3

    def stopFari():
        adc.close()
        p.stop()  # stop PWM
        GPIO.cleanup()



