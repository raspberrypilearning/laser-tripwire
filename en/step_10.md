## The tripwire code

You need a loop to constantly check the light level hitting the LDR. As long as the light level is high, you can assume the laser beam has not been broken. When the light level drops, the beam has been broken and the buzzer should sound.

To do this you can use an infinite loop. This is a loop that will keep going until you quit the program:

```python
  from gpiozero import LightSensor, Buzzer

  ldr = LightSensor(4)  # alter if using a different pin
  buzzer = Buzzer(17)  # alter if using a different pin

  while True:
```

Within the loop, you can use conditional selection to see if the light level falls below some threshold value. Start with `0.5`, but adjust it if you need to increase or decrease the sensitivity of the system:

```python
  from gpiozero import LightSensor, Buzzer

  ldr = LightSensor(4)  # alter if using a different pin
  buzzer = Buzzer(17)  # alter if using a different pin

  while True:
      if ldr.value < 0.5:  # adjust this to make the circuit more or less sensitive
          buzzer.on()
      else:
          buzzer.off()
```

If you were to run this now, it would fail. This is because the `while` loop runs so many times a second, it checks the light level faster than the capacitor charges and discharges. To slow the script down, you'll need to use the `time` library and add a `sleep` into the loop:

```python
  from gpiozero import LightSensor, Buzzer
  from time import sleep

  ldr = LightSensor(4)  # alter if using a different pin
  buzzer = Buzzer(17)  # alter if using a different pin

  while True:
      sleep(0.1)
      if ldr.value < 0.5:  # adjust this to make the circuit more or less sensitive
          buzzer.on()
          # uncomment the next line to have the alarm trigger for 30 seconds.
          # sleep(30) 
      else:
          buzzer.off()
```

Run the code and shine the laser onto the LDR. When you break the beam, the buzzer should sound.

