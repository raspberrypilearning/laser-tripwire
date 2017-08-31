## Detecting a broken beam

Your first step will be to create a simple prototype on a breadboard to detect whether or not a beam of light is hitting the **l**ight-**d**ependent **r**esistor (LDR).

### Shielding the LDR

It's a good idea to shield your LDR to make sure that only light from the laser pointer will trigger your program. You can do this with a small roll of paper, or even more easily with a section of a drinking straw.

![ldr and straw](images/ldr-straw1.png)
![ldr in straw](images/ldr-straw2.png)

### Building and coding your light sensor

Now you're going to need to do a couple of things:

- Set up your circuit using a capacitor and an LDR wired to your Raspberry Pi. There's an optional section below which explains how RC timing circuits work. The other section details how to use Python to detect light levels.

[[[generic-theory-rc-timing-circuit]]]
[[[rpi-python-ldr]]]

- Now you're ready to write a script to detect when the laser beam is broken. You can use methods from the `gpiozero` module to do this. One of your options is to use a `while True` loop containing the `wait_for_dark` method. However, a better way might be to use the `when_dark` method. If you choose this method, you need to either create a function to print `'INTRUDER'`, or you could use a lambda function.

[[[generic-python-lambda-functions]]]

If you need a little help, then have a look at the hints below.

--- hints --- --- hint ---
- Import the `LightSensor` class from `gpiozero`.
- Create an 'ldr' object for the GPIO pin to which you have connected the LDR.
- Use the `when_dark` method to trigger your `print`. The print command could either be inside another function, or called using a lambda function.
--- /hint --- --- hint ---
Assuming you've imported your `LightSensor` class and set up an object on a GPIO pin, this single line will print 'INTRUDER' whenever the laser beam is broken:
```python
ldr.when_dark = lambda: print("INTRUDER")
```
--- /hint --- --- hint ---
Here's an animation showing how to set up the circuit and write your Python program.
![ldr to print](images/print_with_ldr.gif)
--- /hint --- --- /hints ---
