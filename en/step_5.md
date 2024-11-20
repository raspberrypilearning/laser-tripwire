## Run on boot

You can use `systemd` to run your code when Raspberry Pi starts up.

**Note** `systemd` is only available from Jessie versions of the Raspbian OS.

--- task ---

Open Terminal and type:

```bash
sudo nano /etc/systemd/system/tripwire.service
```

--- /task ---

--- task ---

Create your service.

```bash
[Unit]
Description=Laser Tripwire
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/username/tripwire.py
Environment="PULSE_RUNTIME_PATH=/run/user/1000/pulse/"

[Install]
WantedBy=multi-user.target
```
**Note**: Change `username` to your username.
--- /task ---

--- task ---

Save and exit nano by pressing `Ctrl + x` and then press `y` when you are prompted to save.

--- /task ---

--- task ---

Tell systemd to enable your new service.

```bash
sudo systemctl daemon-reload
sudo systemctl enable tripwire.service
```

--- /task ---

--- task ---

Make sure your headphones or speakers are connected to your Raspberry Pi.

--- /task ---

--- task ---

**Test**: your service runs when you reboot your Raspberry Pi.

```bash
sudo reboot
```

--- /task ---