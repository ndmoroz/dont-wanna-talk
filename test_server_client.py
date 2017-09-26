from sys import executable
from os.path import dirname
from subprocess import Popen

# Define a command that starts new terminal
new_window_command = "cmd.exe /c start".split()

# Open new consoles, run server and client
project_path = " " + dirname(__file__)
echos = [executable, project_path, "/server.py"], \
        [executable, project_path, "/client.py 127.0.0.1"]
processes = [Popen(new_window_command + [echo]) for echo in echos]
