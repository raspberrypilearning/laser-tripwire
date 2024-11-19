## Building your laser tripwire

Once the circuit has been tested, you can wire up the components directly to the Raspberry Pi.

--- task ---

Place one leg of the LDR and the long leg of the capacitor into a female-to-female jumper lead. Then tape it up to secure the legs.

--- /task ---

--- task ---

Place the remaining legs into jumper leads, then plug it all back into the Raspberry Pi.

![](images/assembly1.jpg)

--- /task ---

--- task ---

You can place the Raspberry Pi and components in a housing to conceal them if you wish. Here we have used a plastic box with a hole made in it for the straw:

![](images/assembly2.jpg)

--- /task ---

--- task ---

Place your container near a doorway. Then affix the laser pointer to the wall so the beam is focused down the straw.

--- /task ---

--- task ---

**Test**: Run the code and test your laser tripwire.

--- /task ---

### Run on boot

Your code needs to run as soon as the Raspberry Pi starts up. 

You can automate tasks with **Cron**.

--- task ---

Open Terminal and type:

```bash
sudo nano /lib/systemd/system/tripwire.service
```

--- /task ---

--- task ---

Add this text:

```bash
[Unit]
Description=Laser Tripwire
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/username/tripwire.py

[Install]
WantedBy=multi-user.target
```
--- /task ---

--- task ---

Save and exit nano by pressing `Ctrl + x` and then typing in `y` when you are prompted to save.

--- /task ---