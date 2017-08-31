## Coding a light sensor

Luckily, most of the complicated code you would have to write to detect the light levels received by the LDR has been abstracted away by the `gpiozero` library. This library will handle the timing of the capacitor's charging and discharging for you.

Use the following code to set up the light sensor:

```python
  from gpiozero import LightSensor

  ldr = LightSensor(4)  # alter if using a different pin
```

Now run the code and switch over to the interpreter. Type `ldr.value` into the interpreter to see the light level currently recorded. Next, shine the laser pointer onto the LDR and type `ldr.value` into the interpreter again, to see the light level when the LDR is illuminated.

