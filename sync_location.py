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
        if not folder:
            continue
        folders[folder] = configured_folder.attributes["path"].value
        if not folders[folder].endswith("/"):
            folders[folder] += "/"
        globals()[folder] = folders[folder]

# The download folder is created for the first location found:
# - Mounted disk in reverse-alphabetical order (so HDD2 before HDD etc.)
# - Main user folder
# For most setups, this will usually just return the user Downloads folder.
disks = []
if os.path.isdir("/mnt/"):
    disks = [f"/mnt/{f}" for f in os.listdir("/mnt/")]
    disks = sorted([d for d in disks if os.path.isdir(d)], reverse=True)
disks.append("~")
for disk in disks:
    if os.path.isdir(disk):
        folders["downloads"] = os.path.join(disk, "Downloads/")
        break
if "downloads" in folders:
    os.makedirs(folders["downloads"], exist_ok=True)
    globals()["downloads"] = folders["downloads"]
globals()["all"] = folders


# This short section provides basic command line usability, for example:
# `sync_location default` will print the location of the default sync folder.
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in folders:
            print(folders[sys.argv[1]])
            sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
