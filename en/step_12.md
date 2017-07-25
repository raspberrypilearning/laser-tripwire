## Using a sound file and a speaker

- If you have a speaker that you can plug into your Raspberry Pi, you can get your program to play a scary sound instead of sounding a buzzer.

- First you'll need to choose an appropriate sound file. [This site](http://soundbible.com/royalty-free-sounds-1.html) has lots of sounds that you can use, and [this one](http://soundbible.com/71-Dog-Growling-And-Barking.html) is particularly appropriate. Once you have your sound you can use it in your program.

- To play the sound with Python, you'll need to use the `pygame` library. Add this line below your `gpiozero` import.

    ``` python
    import pygame
    ```
- Next you need to initialise Pygame and its sound mixer.

    ``` python
    pygame.init()
    pygame.mixer.init()
    ```
- The sound file you used needs to be loaded up by your script. You can give it any name you like, just make sure you get the filename correct. You'll also need the length of the sound clip.

    ``` python
    growl = pygame.mixer.Sound('growl.mp3')
    length = growl.get_length()
    ```
- Now, within the `while True:` loop, you can play the sound file instead of making the buzzer sound, and have it stop once the sound has finished playing.

    ``` python
    while True:
        sleep(0.1)
        if ldr.value < 0.5:  # adjust this to make the circuit more or less sensitive
            growl.play()
            sleep(length)
            growl.stop()

    ```
- Have a play with different sounds to get the one that is most appropriate for your environment. Maybe you could use this on Halloween with a [witch's cackle](http://soundbible.com/33-Evil-Laugh-Cackle.html), to catch the kids trick or treating.

