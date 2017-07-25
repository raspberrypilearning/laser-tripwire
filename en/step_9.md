## Testing the buzzer

Next you can test that the buzzer is working.

-  Alter the `import` line so it looks like this, so you can access the `Buzzer` class from `gpiozero`:

```python
from gpiozero import LightSensor, Buzzer
```

-  Next, you need to tell the program which pin the buzzer is connected to:

```python
buzzer = Buzzer(17)
```

-  Your script should now look like this:

```python
  from gpiozero import LightSensor, Buzzer

  ldr = LightSensor(4)  # alter if using a different pin
  buzzer = Buzzer(17)  # alter if using a different pin

```

-  Run your code and then in the interpreter type the following:

```python
buzzer.on()
# and
buzzer.off()
```

This will switch the buzzer on and off. If it's not working, check your wiring and pin numbers.

