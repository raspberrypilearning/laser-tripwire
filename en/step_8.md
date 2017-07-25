## Reducing light to the LDR

You probably noticed that unless you are in a dark room, there is little difference in the measured light levels when the LDR is illuminated by the laser, and when it's not. This can be fixed by reducing the amount of light that the LDR receives from other light sources in the room.

-  Take an opaque drinking straw and cut a length from it between 2 and 5 cm long.
2.  Insert the head of the LDR into the straw.
3.  Type `ldr.value` into the interpreter again, then once more with the LDR illuminated by the laser.

You should now see a larger difference in the recorded light levels.

Wiring up the buzzer
--------------------

-  The piezo buzzer is a polar component, like the capacitor. Place it into the breadboard, then connect the longer leg to GPIO 17 and the shorter leg into one of the ground pins.

![](images/Laser-tripwire_4-01.png)

