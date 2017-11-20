# The ​ ​ Connected ​ ​ Mirror

![CU Logo](https://image.ibb.co/fPWTHm/image7.png)

SYSC​ ​ 3010

2017-10-23

Connor​ ​MacKenzie

Theo​ ​Hronowsky

Zein​ ​Hajj-Ali


## 1.0 ​ ​ Team ​ ​ Project

What​ ​if​ ​your​ ​bathroom​ ​mirror​ ​was​ ​more​ ​than​ ​just​ ​a​ ​mirror?​ ​Tired​ ​of​ ​wasting​ ​precious​ ​time
catching​ ​up​ ​on​ ​social​ ​media​ ​and​ ​world​ ​updates​ ​while​ ​getting​ ​ready​ ​for​ ​your​ ​busy​ ​day?​ ​The
Connected​ ​Mirror​ ​is​ ​a​ ​media​ ​platform​ ​loaded​ ​with​ ​features​ ​making​ ​those​ ​early​ ​morning​ ​wake
ups​ ​a​ ​bit​ ​more​ ​fun.​ ​The​ ​Connected​ ​Mirror​ ​is​ ​an​ ​optimistic​ ​vision​ ​of​ ​the​ ​future​ ​which​ ​involves​ ​the
use​ ​of​ ​screens​ ​and​ ​data​ ​everywhere,​ ​ready​ ​to​ ​push​ ​information​ ​to​ ​the​ ​user​ ​at​ ​a​ ​moment's​ ​notice
while​ ​acting​ ​as​ ​a​ ​traditional​ ​mirror​ ​simultaneously.
The​ ​Connected​ ​Mirror​ ​allows​ ​users​ ​to​ ​organize​ ​themselves​ ​and​ ​access​ ​any​ ​information​ ​they
need​ ​all​ ​in​ ​one​ ​space​ ​for​ ​an​ ​easier​ ​and​ ​more​ ​efficient​ ​start​ ​to​ ​one's​ ​day.​ ​With​ ​access​ ​to
calendar,​ ​reminders,​ ​news,​ ​weather,​ ​traffic​ ​and​ ​much​ ​more,​ ​the​ ​Connected​ ​Mirror​ ​will​ ​improve
your​ ​day​ ​by​ ​giving​ ​you​ ​a​ ​heads-up​ ​of​ ​what’s​ ​planned​ ​ahead.​ ​Connected​ ​Mirror​ ​is​ ​your​ ​very​ ​own
personalized​ ​smart​ ​mirror​ ​focused​ ​entirely​ ​on​ ​increasing​ ​your​ ​productivity.
With​ ​the​ ​Connected​ ​Mirror​ ​you’ll​ ​manage​ ​access​ ​to​ ​the​ ​following​ ​without​ ​having​ ​to​ ​find​ ​your
smartphone​ ​in​ ​the​ ​morning:

● Calendar

● Clock

● Reminders​ ​for​ ​events

● Newsfeed

● Complements​ ​and​ ​inspiring​ ​quotes

● Voice​ ​control

● Stock​ ​report

● Weather

● Traffic

Connected​ ​Mirror​ ​helps​ ​keeps​ ​you​ ​connected,​ ​in​ ​control,​ ​and​ ​confident​ ​every​ ​morning.​ ​Plus,​ ​it
makes​ ​you​ ​ridiculously​ ​good​ ​looking.

## 2.0 ​ ​ Design

**2.1** ​ ​ **Design** ​ ​ **Architecture**
To create a testable and functionable Connected Mirror, the following items will be used to
fabricate​ ​the​ ​product:

● Arduino​ ​Uno

● 2 ​ ​Raspberry​ ​Pi

● Prototyping​ ​Board

● Microphone

● Ultrasonic​ ​Sensor

● LCD​ ​display
● 2 ​ ​Way​ ​Mirror

● Led​ ​Lights

● Wood​ ​Frame

The layout of the test unit is represented by Figure 1, below, and the implementation of the
hardware​ ​will​ ​look​ ​similar​ ​to​ ​that​ ​of​ ​Figure​ ​2.

![Figure 1](https://image.ibb.co/itfNcm/image9.png)

### Figure ​ ​ 1 ​:​ ​General​ ​layout​ ​of​ ​the​ ​Connected​ ​Mirror​ ​[​Michael​ ​Teeuw​,​​ ​ MirrorMirror ​^2 ​,​ ​2016]


![Figure 2](https://preview.ibb.co/js5AV6/image3.png)


### Figure ​ ​ 2 ​:​ ​Hardware​ ​installed​ ​into​ ​frame​ ​[​Dylan​ ​Pierce,​ ​​ Building ​ ​ MirrorMirror ​,​ ​2015]

Figure 1 shows how the frame of the Connected Mirror will house the two way mirror and the
LCD display behind it. Figure 2 shows a similar project(not ours) that is also an interpretation of
a smart mirror. It shows how the Raspberry Pi and Arduino will be connected to the Mirror.
Behind the mirror, the frame will contain the LCD display, the two Raspberry Pi, the arduino, as
well as the sensors and any necessary wiring used to connect the system. The two sensors, the
ultrasonic sensor and the microphone will be positioned on the outside of the mirror in order for
the devices to work properly. Led lights will surround the perimeter of the frame and be
controlled​ ​by​ ​an​ ​android​ ​app.
**2.2** ​ ​ **Systems** ​ ​ **Architecture** ​ ​ **Deployment** ​ ​ **Diagram**
Provide below, Figure 3, is the systems architecture deployment diagram for the Connected
Mirror. It shows the relationships between the devices used and how they work and
communicate​ ​together​ ​in​ ​the​ ​system.

![Figure 3](https://image.ibb.co/cpFoHm/image8.png)

**Figure** ​ ​ **3:** ​ ​​System​ ​Deployment​ ​Diagram​ ​for​ ​the​ ​Connected​ ​Mirror

_The first Raspberry Pi_ will be used to control the LCD display. It will display information gathered
from the second Raspberry Pi. It will update the graphical user interface on the LCD to display useful
information to the user. It will also listen to the user via a microphone to receive then execute
commands​ ​based​ ​on​ ​the​ ​input​ ​by​ ​the​ ​user.
_The second Raspberry Pi_ ​will access the Web and provide the required information to the rest of the
system. It will store an SQL database of information that can be accessed at any time. Additionally, it
will communicate with the android app and sent commands to the Arduino to control the LED
lighting.


_The Arduino_ will control the hardware side of the system. It will control the LED lighting used for the
mirror as well as use ultrasonic sensors to track movement in front of the mirror. The ultrasonic
sensor​ ​will​ ​be​ ​in​ ​charge​ ​of​ ​turning​ ​on​ ​the​ ​mirror.
The android application is in charge of controlling the LED lights mounted to the front of the frame. It
will​ ​be​ ​able​ ​to​ ​manually​ ​change​ ​the​ ​color​ ​of​ ​the​ ​LEDS​ ​at​ ​any​ ​point.
The three devices will be connected to each other making up the system that is the Connected
Mirror.
**2.3** ​ ​ **Systems** ​ ​ **Sequence** ​ ​ **Diagrams**
In order to explain the systems design and functionality further, two general sequence diagrams
are included on the following page. Figure 4 represents the sequence in which the system
follows in order to wake up the mirror. Figure 5 represents the sequence of how the system
handles​ ​a​ ​voice​ ​input​ ​via​ ​the​ ​user.

![Figure 4](https://image.ibb.co/dyqYiR/image4.png)

**Figure** ​ ​ **4** ​:​ ​Sequence​ ​Diagram​ ​for​ ​System​ ​Wake​ ​Up

The Connected Mirror system wakes up and begins once the ultrasonic sensor detects
movement in front of it. The ultrasonic sensor is connected to the Arduino which is constantly
polling for a motion. Once the Arduino detects a movement, it sends a signal to the Raspberry
Pi 1 which then gathers all data needed for start up. This data is then pushed to the LCD for the
user​ ​to​ ​view.

![Figure 5](https://image.ibb.co/bMOVV6/image5.png)

**Figure** ​ ​ **5** ​:​ ​Sequence​ ​Diagram​ ​for​ ​Handling​ ​a​ ​Voice​ ​Command

The​ ​sequence​ ​in​ ​which​ ​the​ ​Connected​ ​Mirror​ ​handles​ ​a​ ​voice​ ​command​ ​begins​ ​with​ ​the
Raspberry​ ​Pi​ ​ 2 ​ ​polling​ ​the​ ​microphone​ ​which​ ​is​ ​connected​ ​to​ ​the​ ​2nd​ ​Raspberry​ ​Pi.​ ​The​ ​2nd
Raspberry​ ​Pi​ ​determines​ ​the​ ​suitable​ ​action​ ​that​ ​matches​ ​the​ ​voice​ ​command​ ​and​ ​sends​ ​it​ ​to
the​ ​1st​ ​Raspberry​ ​Pi.​ ​Then,​ ​an​ ​actionHandler​ ​is​ ​used​ ​to​ ​determine​ ​what​ ​the​ ​action​ ​will​ ​do.
Finally,​ ​the​ ​determined​ ​action​ ​is​ ​sent​ ​to​ ​the​ ​LCD​ ​to​ ​be​ ​displayed​ ​to​ ​the​ ​User.​ ​For​ ​example,​ ​a
user​ ​might​ ​say​ ​something​ ​along​ ​the​ ​lines​ ​of​ ​“what​ ​is​ ​the​ ​weather”.​ ​The​ ​process​ ​will​ ​realize​ ​that
the​ ​command​ ​concerns​ ​displaying​ ​the​ ​weather​ ​and​ ​then​ ​will​ ​access​ ​the​ ​database​ ​which
contains​ ​the​ ​data​ ​for​ ​the​ ​weather.​ ​This​ ​will​ ​then​ ​be​ ​pushed​ ​to​ ​the​ ​display​ ​for​ ​viewing.
**2.4** ​ ​ **Software**
The​ ​system​ ​will​ ​be​ ​woken​ ​up​ ​by​ ​the​ ​Arduino​ ​constantly​ ​polling​ ​for​ ​a​ ​person​ ​to​ ​come​ ​within​ ​a
specified​ ​distance​ ​of​ ​it.​ ​This​ ​will​ ​be​ ​written​ ​in​ ​C​ ​and​ ​follow​ ​the​ ​following​ ​flow​ ​in​ ​Figure​ ​6.

![Figure 6](https://image.ibb.co/d2Phcm/image2.jpg)

**Figure** ​ ​ **6:** ​ ​​Flow​ ​of​ ​Motion​ ​Detection

Once​ ​the​ ​system​ ​has​ ​woken​ ​up​ ​a​ ​portion​ ​of​ ​java​ ​code​ ​is​ ​used​ ​control​ ​and​ ​organize​ ​the​ ​display
using​ ​setting​ ​stored​ ​in​ ​a​ ​MySQL​ ​database.

![Figure 7](https://image.ibb.co/d9iKOR/image11.png)

**Figure** ​ ​ **7:** ​ ​​Class​ ​Diagram​ ​for​ ​Screen​ ​Initialization


The​ ​first​ ​table​ ​in​ ​the​ ​database​ ​will​ ​store​ ​the​ ​user’s​ ​preferred​ ​settings​ ​through​ ​a​ ​unique​ ​primary
key​ ​SettingID,​ ​their​ ​location​ ​and​ ​an​ ​enumeration​ ​corresponding​ ​to​ ​a​ ​preferred​ ​combination​ ​of
modules.​ ​The​ ​second​ ​table​ ​contains​ ​information​ ​for​ ​preset​ ​LED​ ​lighting​ ​combinations.​ ​The​ ​last
table​ ​contains​ ​keywords​ ​for​ ​the​ ​voice​ ​command​ ​to​ ​recognize​ ​and​ ​the​ ​corresponding​ ​command.

![Figure 8](https://image.ibb.co/euFoHm/image10.png)

**Figure** ​ ​ **8:** ​ ​​Tables​ ​to​ ​be​ ​Stored​ ​in​ ​Database

Rounding​ ​out​ ​our​ ​software​ ​is​ ​a​ ​portion​ ​of​ ​java​ ​code​ ​to​ ​handle​ ​voice​ ​commands.​ ​It​ ​will​ ​poll​ ​for​ ​a
command​ ​then​ ​using​ ​keywords​ ​it​ ​will​ ​identify​ ​the​ ​command​ ​and​ ​execute.

![Figure 9](https://image.ibb.co/kO3VV6/image1.jpg)

**Figure** ​ ​ **9:** ​​ ​Class​ ​Diagram​ ​of​ ​Voice​ ​Control

**2.5:** ​ ​ **Hardware/Testing**
As​ ​seen​ ​below,​ ​the​ ​ultrasonic​ ​sensor​ ​is​ ​connected​ ​to​ ​the​ ​Arduino​ ​first​ ​using​ ​the​ ​breadboard​ ​in​ ​a
manner​ ​that​ ​will​ ​allow​ ​us​ ​to​ ​test​ ​the​ ​distances​ ​it​ ​can​ ​detect.​ ​The​ ​trig​ ​pin​ ​on​ ​the​ ​sensor​ ​(Arduino
IO​ ​port​ ​8)​ ​is​ ​set​ ​to​ ​its​ ​high​ ​state​ ​for​ ​a​ ​few​ ​microseconds​ ​which​ ​will​ ​send​ ​out​ ​a​ ​sonic​ ​burst​ ​which
is​ ​received​ ​through​ ​the​ ​echo​ ​pin​ ​(Arduino​ ​IO​ ​port​ ​9).​ ​We​ ​will​ ​receive​ ​a​ ​value​ ​in​ ​microseconds​ ​on
IO​ ​port​ ​ 9 ​ ​which​ ​indicates​ ​the​ ​time​ ​the​ ​sound​ ​traveled​ ​to​ ​its​ ​target​ ​and​ ​back.​ ​Multiplying​ ​this
value​ ​by​ ​the​ ​speed​ ​of​ ​sound​ ​will​ ​give​ ​us​ ​double​ ​the​ ​distance​ ​to​ ​the​ ​target.

![Connections](https://image.ibb.co/hYOxA6/image6.jpg)

**2.6:** ​ ​ **Communication** ​ ​ **Protocols**
Communication​ ​between​ ​the​ ​Arduino​ ​and​ ​one​ ​of​ ​the​ ​Raspberry​ ​PIs​ ​will​ ​happen​ ​using​ ​serial
through​ ​the​ ​USB​ ​cable​ ​at​ ​ 9600 ​ ​bps.​ ​The​ ​Raspberry​ ​Pi​ ​will​ ​use​ ​the​ ​Serial​ ​Python​ ​library​ ​to
receive​ ​and​ ​decode​ ​the​ ​data.​ ​For​ ​instance,​ ​sending​ ​the​ ​detected​ ​distance​ ​using​ ​the​ ​ultrasound
sensor​ ​from​ ​the​ ​Arduino​ ​to​ ​the​ ​Raspberry​ ​Pi​ ​will​ ​send​ ​the​ ​number​ ​as​ ​an​ ​integer​ ​in​ ​binary​ ​bit​ ​by
bit​ ​at​ ​ 9600 ​ ​bps​ ​over​ ​the​ ​USB​ ​cable.
Communication​ ​between​ ​both​ ​Raspberry​ ​Pis​ ​will​ ​use​ ​the​ ​UDP​ ​protocol.​ ​One​ ​Raspberry​ ​Pi​ ​will
encode​ ​the​ ​data​ ​in​ ​JSON​ ​and​ ​send​ ​it​ ​in​ ​UDP​ ​packets​ ​to​ ​the​ ​other​ ​Pi​ ​to​ ​be​ ​decoded​ ​and​ ​used.​ ​If
we​ ​are​ ​sending​ ​an​ ​object​ ​created​ ​from​ ​a​ ​complex​ ​class,​ ​we​ ​have​ ​to​ ​first​ ​define​ ​a​ ​default​ ​method
for​ ​encoding,​ ​we​ ​will​ ​encode​ ​it​ ​as​ ​a​ ​dictionary​ ​for​ ​our​ ​purposes.​ ​We​ ​then​ ​receive​ ​it​ ​on​ ​the​ ​other
Raspberry​ ​Pi​ ​using​ ​the​ ​UDP​ ​protocols​ ​and​ ​decode​ ​it​ ​back​ ​into​ ​the​ ​object​ ​it​ ​was​ ​sent​ ​as.
For​ ​example:
If​ ​we​ ​have​ ​a​ ​Weather​ ​class
class​​ ​​Weather​:
'Simple​ ​weather​ ​class​ ​to​ ​send​ ​and​ ​display​ ​weather​ ​data'
def ​​​​_init_​(self,​ ​temperature,​ ​forecast):


self.temperature​ ​=​ ​temperature
Self.forecast​ ​=​ ​forecast
We​ ​then​ ​have​ ​to​ ​define​ ​a​ ​default​ ​JSON​ ​encoding​ ​method:
​ ​​ ​​ ​​ ​​ ​​ ​def​​ ​​defaultJSON​(object):
return​​ ​object._dict_
This​ ​converts​ ​the​ ​object​ ​to​ ​a​ ​dictionary​ ​which​ ​can​ ​easily​ ​be​ ​sent​ ​and​ ​decoded​ ​by​ ​the​ ​other
Raspberry​ ​PI.
**Testing** ​ ​ **Processes:**
1-​ ​Test​ ​ultrasonic​ ​distances​ ​and​ ​required​ ​detection​ ​distance
2-​ ​Test​ ​LCD​ ​display​ ​using​ ​Arduino,​ ​making​ ​sure​ ​to​ ​place​ ​LCD​ ​behind​ ​mirror​ ​and​ ​re-test
3-​ ​Review​ ​JSON​ ​protocols​ ​for​ ​data​ ​transfer​ ​between​ ​RPI1,​ ​RPI2,​ ​and​ ​Arduino
4-​ ​Install​ ​and​ ​implement​ ​voice​ ​control​ ​interface
5-​ ​Review​ ​JSON​ ​protocols​ ​for​ ​data​ ​retrieval​ ​on​ ​RPI1​ ​from​ ​Android​ ​phone​ ​using​ ​Pushbullet​ ​API
6-​ ​Review​ ​JSON​ ​protocols​ ​for​ ​data​ ​retrieval​ ​on​ ​RPI1​ ​from​ ​online​ ​weather​ ​database


