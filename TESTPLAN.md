# The Connected Mirror

SYSC 3010 Testing Plan

**Team M5 Members:**

Zein Hajj-Ali

Theo Hronowsky

Connor Mackenzie

## Unit Testing

1.0: Ultrasound Distance Sensor - Hardware Unit

The following code under test is explained through the following test cases. The test cases test the hardware portion of the ultrasound distance sensor. The most complex sensor to test is the ultrasonic sensor and therefore will be the sensor under test. These tests consist of the Arduino retrieving the distance between the sensor and the user of the mirror. In order to obtain a distance, the trig pin on the sensor (Arduino IO port 8) is set to its high state for a few microseconds which will send out a sonic burst which is received through the echo pin (Arduino IO port 9). We will receive a value in microseconds on IO port 9 which indicates the time the sound traveled to its target and back. Multiplying this value by the speed of sound will give us double the distance to the target. Once calculating this distance, it will be relayed to the RPI for further manipulation.

| **Test ID** | **Test Name** | **Test Steps** | **Expected Result** | **Actual Result** | **Steps Taken** |
| --- | --- | --- | --- | --- | --- |
| 0 | test\_initialsensorReading | Connect the sensor to the arduino and used basic code to read time taken for signal to be sent and received from/to the sensor | Consistent time in milliseconds when sensor is put at certain distances | As expected | N/A |
| 1 | test\_timetodistanceReading | Input conversion formula to convert time in milliseconds to distance in centimeters. Run the test code and measure the distances using both the sensor as well as a ruler | Distance readings should match the ruler measurements within 0.5cm when placed at a minimum distance of 5cm | Results were as expected at a minimum distance of 7cm | N/A |
| 3 | test\_arduinocodefromRPI | Connect Arduino to RPI using provided USB cable. Use test python code to receive data sent over serial from Arduino and return results in terminal window. | Same as test 1 but returned on the RPI terminal window instead of the lab computer. | As expected | N/A |

**Table 1** : Hardware Unit Test Cases

The following code stub tests case 3 above. It tests that the connection between the Arduino and RPI receives data sent over serial. The serial data will be accessed by importing and using the serial package. .Serial is used to access this data.  If this data is successfully sent over the connection, the results will be printed in the terminal window.

Test 3 Stub:

| import serialimport osser = serial.Serial(&#39;/dev/ttyACM0&#39;, 9600)while1:
        print(ser.readline());        |
| --- |

2.0: Raspberry PI Screen Trigger - General Utility Unit

The general utility Unit tests the Raspberry PI Screen Trigger process. Through the test cases presented in table 2, the code will detect the user at a certain distance and decide whether to turn the screen on or off depending on the user&#39;s distance. This general utility unit will take advantage of the code developed for the hardware unit testing portion by accessing the calculated distance measurements. The distance is then compared to a minimum distance of 75 centimeters. If it is within this range the LCD will receive a connection and will display a ripple input to visually demonstrate that a connection has been established. If the distance is out of range, that is greater than 75 centimeters, the connection to the LCD will be cut.

| **Test ID** | **Test Name** | **Test Steps** | **Expected Result** | **Actual Result** | **Steps Taken** |
| --- | --- | --- | --- | --- | --- |
| 0 | test\_rpiretrievesDistance | Raspberry Pi accesses Arduino through USB cable to receive the calculated distance | Distance in centimeters is retrieved from RPI to be used for further examination | As expected | N/A |
| 1 | test\_comparisonofDistance | Raspberry Pi compares the retrieved distance to a set minimum distance of 75 centimetres. | The distance value is compared to the minimum value. The distance is then determine to be in range or out of range by the next two test cases (3&amp;4) | As expected | N/A |
| 3 | test\_comparewithinRange | Raspberry Pi reads a distance within the range of 75 centimetres. The console prints out a message such as close or within range to confirm the user is within working range. Connection to the LCD display is turned on and the program can continue to display. The LCD is sent a signal to flicker on the display to visually ensure the device can display further information. | Raspberry Pi compares the distance to the minimum distance and determines that the user is in the working range of of the display booting up. The within range message is displayed and the connection to the LCD display is made and the display flickers as expected. | As expected, Raspberry pi determines the distance is in range | N/A |
| 4 | test\_compareoutsideRange | Raspberry Pi reads a distance out of range of the minimum working range of 75 centimetres. The console prints out a message such as far or out of range to confirm that the user is not within the working range of the mirror. Connection to the LCD is shut off. | Raspberry Pi compares the distance to the minimum distance and determines that the user is not within the working range of of the display booting up. The out of range message is displayed and the connection to the LCD is shut off. | As expected, Raspberry pi determines the distance is out of range | N/A |

**Table 2** : General Utility Unit Test Cases

The following stub code tests whether the screen will be triggered on or off.  The code stub makes the necessary comparisons to determine if the LCD will be turned on or off. The serial distance input will be compared to a set minimum distance and from there, the distance will be determined to be in or out of range.

Test Stub for Raspberry PI Screen Trigger:

| import serialimport osser = serial.Serial(&#39;/dev/ttyACM0&#39;, 9600)onOff = 1;while1:
        if int( ser.readline())&lt;75:                print(&quot;Close&quot;);                print(ser.readline());                if onOff == 1:                        os.system(&quot;tvservice -p&quot;);                        os.system(&quot;xset -display :0 dpms force on&quot;);                        onOff = 0;        else:                print(&quot;Far&quot;);                print(ser.readline());                if onOff == 0:                        os.system(&quot;tvservice -o&quot;);                        onOff = 1; |
| --- |
|   |
|   |
|   |

3.0 Distributed Systems Unit - Database

The following test case revolves around the Connected Mirrors database where many values are updated and retrieved for information purposes. The Connected MIrror will use a SQL database called MySQL which will send and receive data. The database will be accessed through java code connecting the RPI. The following table, Table 3, shows different test cases and the response to each trigger. It shows the messages that will either be received or sent out by the server. The database stores the user&#39;s preferred settings through unique keys and an enumeration corresponding to a combination of modules.

| **No.** | **Title** | **Description** | **Context** | **Trigger** | **Response** |
| --- | --- | --- | --- | --- | --- |
| 1 | test\_setuserSettings | Set the values in the table userSettings | Mirror is connected to MySQL database on rpi 1. Java code makes connection to database. | When mirror is turned on for the first time it will prompt user for information and send to database. | When table is queried using &quot;Select \* from userSettings&quot; it should return the values set. |
| 2 | test\_update userSettings | update the values in the table userSettings | Mirror is connected to MySQL database on rpi 1. Java code makes connection to database. | When the user chooses to update their user settings they are prompted for new settings and the table is updated. | When table is queried using &quot;Select \* from userSettings where Setting = 1&quot; it should return the updated values. |
| 3 | test\_setLEDSettings | Set the values in the table LEDSettings | Mirror is connected to MySQL database on rpi 1. Java code makes connection to database. | When mirror is turned on for the first time it will prompt user for information and send to database. | When table is queried using &quot;Select \* from LEDSettings where Setting = 1&quot; it should return the set values. |
| 4 | test\_updateLEDSettings | Update the values in the table LEDSettings | Mirror is connected to MySQL database on rpi 1. Java code makes connection to database. | When the user chooses to update their LED settings they are prompted for new settings and the table is updated. | When table is queried using &quot;Select \* from LEDSettings where Setting = Row just updated&quot; it should return the updated values. |
| 5 | test\_addLEDSettings | Insert a new row into the LEDSettings table | Mirror is connected to MySQL database on rpi 1. Java code makes connection to database. | When the user chooses to add an LED profile they are prompted for new settings and the table is updated. | When table is queried using &quot;Select \* from userSettings where Setting = Row just inserted&quot; it should return the inserted values. |

**Table 3** : Database Test Cases

4.0 Acceptance Testing

The following acceptance testing table, table 4, represents a list of scenarios both successful and erroneous and the corresponding results. The purpose of this acceptance testing is to show how the complete Connected Mirror works together as a whole.

| Scenario | Result |
| --- | --- |
| 1 |
- Ultrasonic sensor polls for a person to walk within 75 cm
- Screen turns on
  |
| 2 |
- User commands with voice to check weather
- Weather is displayed on screen
  |
| 3 |
- User walks away
- Screen turns off
 |
| 4 |
- Microphone doesn&#39;t understand or receive a voice input
- Microphone keeps pooling/asks for voice command again
 |
| 5 |
- Color choice on android app is chosen
- LED lighting surrounding the mirror is changed to the new color
- Brightness adjustment is made on android app
- Brightness of LEDs on mirror is adjusted as well
 |

**Table 4:** Acceptance testing scenarios
