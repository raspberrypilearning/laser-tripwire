## Make some noise

There are two ways you can get you program to make some noise rather than just print 'INTRUDER'. 

### Buzzer

The first is to use a piezoelectric buzzer that is switched on when the laser beam is broken. 

--- task ---

Connect the positive leg of the buzzer to any **GPIO** pin on your Raspberry Pi, and the negative leg to a **Ground** pin. The positive leg is normally the longer of the two, and most buzzers are labelled to show which side is positive.

![Buzzer circuit](images/buzzer-circuit.png)

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

Download this sound file: <a href="resources/dog_bark.wav" download>dog_bark.wav</a>

--- /task ---

--- task ---

Move the sound file to your `/home/username/` folder.

**Note**: Change `username` to your own username!

--- /task ---

--- task ---

Alter your `tripwire.py` Python script.

```python
from gpiozero import LightSensor
import pygame

ldr = LightSensor(4))

pygame.init()
my_sound = pygame.mixer.Sound('/home/username/dog_bark.wav')

ldr.when_dark = lambda: my_sound.play()
```

**Note**: Change `username` to your own username!

--- /task ---

[This site](https://freesound.org/){:target="_blank"} has plenty of different sounds to choose from.

--- save ---