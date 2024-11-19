## Making some noise

There are two ways you can get you program to make some noise rather than just print 'INTRUDER'. 

### Buzzer

The first is to use a piezoelectric buzzer that is switched on when the laser beam is broken. 

--- task ---

Connect the positive leg of the buzzer to any **GPIO** pin on your Raspberry Pi, and the negative leg to a **Ground** pin. The positive leg is normally the longer of the two, and most buzzers are labelled to show which side is positive.

![circuit](/images/buzzer-circuit.png)

--- /task ---

--- task ---

You can use the `Buzzer` class in `gpiozero` to turn it on and off again. The code below assumes that the buzzer has been wired to **GPIO 17**.

```python
from gpiozero import LightSensor, Buzzer
ldr = LightSensor(4))
buzzer = Buzzer(17)

ldr.when_dark = lambda: buzzer.beep(0.2, 0.2, 20)
```

--- /task ---

### Speakers

If you do not have a buzzer, you could use the PyGame module to play a sound through some speakers.

--- task ---

```python
from gpiozero import LightSensor
import pygame

ldr = LightSensor(4))

pygame.init()
my_sound = pygame.mixer.Sound('path/to/my/soundfile.wav')

ldr.when_dark = lambda: my_sound.play()
```

[This site](http://soundbible.com/royalty-free-sounds-1.html){:target="_blank"} has plenty of different ones to choose from. [This one in particular](http://soundbible.com/71-Dog-Growling-And-Barking.html){:target="_blank"} might be useful.

--- /task ---