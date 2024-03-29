# Main file
import os
import subprocess

# Create paths for files if they do not exist
# Also, if the app path does not exist, it is clear that the app is being run for the first time => install packages
appPath = os.path.join(os.getenv("APPDATA"), "stopr")
if not os.path.exists(appPath):
    subprocess.run("python -m pip install --upgrade pip")
    subprocess.run("pip install -r packages.txt")
    os.mkdir(appPath)
if os.path.exists("config.py"):
    os.remove("config.py")

# Import subprograms
import download
import train
import predict
import plot
