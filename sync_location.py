#!/usr/bin/env python3
import os
import platform
import sys
from xml.dom import minidom

# Read the syncthing config to locate the folders.
# Only folders synced on the current device will be available as globals.
folders = {}
config_file = "~/.config/syncthing/config.xml"
if platform.system().lower() == "darwin":
    config_file = "~/Library/Application Support/Syncthing/config.xml"
if platform.system().lower() == "windows":
    config_file = "~/AppData/Local/Syncthing/config.xml"
config_file = os.path.expanduser(config_file)
if os.path.isfile(config_file):
    config_xml = minidom.parse(config_file)
    for configured_folder in config_xml.getElementsByTagName("folder"):
        folder = configured_folder.attributes["label"].value
        if not folder:
            folder = configured_folder.attributes["id"].value
        folders[folder] = configured_folder.attributes["path"].value
        if not folders[folder].endswith("/"):
            folders[folder] += "/"
        globals()[folder] = folders[folder]

# The download folder is located on the last mounted disk,
# and will be created on that disk if there is no Downloads folder yet.
# For Windows, this will usually just return the user Downloads folder.
disks = [
    "/mnt/HDD2/Downloads/",
    "/mnt/HDD/Downloads/",
    os.path.expanduser("~/Downloads/")
]
for folder in disks:
    if os.path.isdir(folder.replace("Downloads/", "")):
        if not os.path.isdir(folder):
            os.makedirs(folder)
        folders["downloads"] = folder
        break
if "downloads" in folders:
    globals()["downloads"] = folders["downloads"]
globals()["all"] = folders


# This short section provides basic command line usability, for example:
# `sync_location start` will print the location of that folder and exit.
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in folders:
            print(folders[sys.argv[1]])
            sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
