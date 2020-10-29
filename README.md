sync\_location
==============

#### Read, parse and expose syncthing folder locations by name

The sync location tool will read the syncthing configuration for the current machine,
and expose the locations based on the syncthing folder name.
In addition to the syncthing folders, a folder named "downloads" is also exposed.
This will scan for mounted disks in "/mnt/" to use as the base location of the downloads.
For most operating systems and configurations this will simply be `~/Downloads`.

## Installation

```bash
git clone https://github.com/Jelmerro/sync_location.git
pip3 install --user --upgrade ./sync_location
```

## Import as a module

The package exposes the syncthing folders as a single dictionary named "all".
It's keys are based on the folder names, and the values are set to the folder locations.
Additionally, all folders are also exposed by their label/name as globals.

```python
import sync_location

print(sync_location.all)
# {"downloads": "/home/user/Downloads", "default": "/home/user/Sync"}

print(sync_location.all["downloads"])
print(sync_location.downloads)
# /home/user/Downloads/

print(sync_location.all["default"])
print(sync_location.default)
# /home/user/Sync/
```

## Command-line

To find a location for a folder based on it's name from the command line,
it's possible to run the script with a single argument that represents the folder name.
If the folder exists, the location will be returned and the program will exit with status 0.
For missing folders, no output is printed and the program exists with status code 1.

```bash
sync_location default
# /home/user/Sync/

sync_location downloads
# /home/user/Downloads/
```

## License

The sync location tool is created by [Jelmer van Arnhem](https://github.com/Jelmerro)
and may be copied and modified under the terms of the [MIT license](./LICENSE).
