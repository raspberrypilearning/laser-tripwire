## Run on boot

Your code needs to run as soon as the Raspberry Pi starts up. 

You can control what programs run when the system boots with `systemd`.

**Note** `systemd` is only available from Jessie versions of the Raspbian OS.

--- task ---

Open Terminal and type:

```bash
sudo nano /lib/systemd/system/tripwire.service
```

--- /task ---

The “ExecStart” parameter is used to specify the command we want to run. The “Type” is set to “idle” to ensure that the ExecStart command is run only when everything else has loaded. Note that the paths are absolute and define the complete location of Python as well as the location of our Python script.

--- task ---

Define a new unit called 'Laser Tripwire' and set it to run after the multi-user environment is available. 

```bash
[Unit]
Description=Laser Tripwire
After=multi-user.target
```

--- /task ---

--- task ---

Configure the service.

Set the `Type` to 'idle' so the 'ExecStart' command runs only when everything else has loaded.

Set the `ExecStart` parameter to the command to run.

```bash
[Unit]
Description=Laser Tripwire
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/username/tripwire.py
```

**Note** Replace `username` with your username!

--- /task ---

--- task ---

Add a `WantedBy` directive to 'multi-user.target', so a directory called multi-user.target.wants is created within /etc/systemd/system (if not already available) and a symbolic link to the your unit is placed within. Disabling your unit removes the link and the dependency relationship.

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

Set the permission on the unit file to 644 (read/write).

--- task ---

```bash
sudo chmod 644 /lib/systemd/system/tripwire.service
```

--- /task ---

--- task ---

Tell systemd to start your unit file during the boot sequence.

```bash
sudo systemctl daemon-reload
sudo systemctl enable tripwire.service
```

--- /task ---

--- task ---

**Test**: Reboot your Raspberry Pi to check your service runs.

```bash
sudo reboot
```

--- /task ---