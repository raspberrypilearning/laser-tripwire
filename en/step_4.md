## Making some noise

There are two ways you can get you program to make some noise rather than just print 'INTRUDER'. The first is to use a buzzer that is switched on when the laser beam is broken. The second is to use the PyGame module to play a sound through some speakers.

Have a look at the sections below that detail how to use buzzers and play sounds with PyGame. Choose the method your prefer, and then have a go at making some noise when the laser beam is broken. If you want to have a go at playing sounds through the speakers, then [this site](http://soundbible.com/royalty-free-sounds-1.html){:target="_blank"} has plenty of different ones to choose from. [This one in particular](http://soundbible.com/71-Dog-Growling-And-Barking.html){:target="_blank"} might be useful.

[[[rpi-python-piezoelectric-buzzer]]]
[[[generic-python-playing-sound-files]]]

--- hints --- --- hint ---
Again, you can use the `when_dark` method to trigger the sound. The `when_dark` method can be tied to `buzz.beep` or `sound.play`, for instance.
--- /hint --- --- hint ---
- If you're playing sounds with PyGame, then a sound lasts for a specific amount of time.
- If you're using a buzzer, its `.beep` or `.on` methods will run forever unless you tell them how many times to play.
- As you can't provide arguments to functions called by `when_dark`, you could use a lambda function instead. For instance:

```python
ldr.when_dark = lambda: buzz.beep(0.2, 0.2, 20)
```
--- /hint --- --- hint ---

Here's a couple of videos showing you how to use either method:
<iframe width="560" height="315" src="https://www.youtube.com/embed/CI3Msjrx0V4" frameborder="0" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/xfLAa01vqnc" frameborder="0" allowfullscreen></iframe>

--- /hint --- --- /hints ---
