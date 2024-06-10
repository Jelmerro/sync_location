sync\_location
==============

#### Read, parse and expose syncthing folder locations by name

The sync location tool will read the syncthing configuration for the current machine,
and expose the locations based on the syncthing folder name.

#### Downloads

In addition to the syncthing folders, a folder named "downloads" is always exposed.
This will scan for mounted disks in "/mnt/" to use as the base location of the downloads,
or use the user folder as the main fallback location at `~/Downloads`.
If there is a `downloads` folder in the syncthing config, that will be used instead.

## Installation

```bash
git clone https://github.com/Jelmerro/sync_location.git
pip3 install --user --upgrade ./sync_location
```

## Import as a module

The package exposes the syncthing folders as a single dictionary named "all".
Its keys are based on the folder names, and the values are set to the folder locations.
Additionally, all folders are also exposed by their label/name as globals.

```python
import sync_location

print(sync_location.all)
# {"downloads": "/home/user/Downloads", "default": "/home/user/Sync"}

print(sync_location.all["downloads"])
print(sync_location.downloads)
# /home/user/Downloads/

if "default" in sync_location.all:
    print(sync_location.all["default"])
    print(sync_location.default)
    # /home/user/Sync/
```

## Command-line

To find a location for a folder based on its name from the command line,
it's possible to run the script with a single argument that represents the folder name.
If the folder exists, the location will be returned and the program will exit with status 0.
For missing folders, no output is printed and the program exists with status code 1.
Optionally, a second argument can be presented that is appended to the base path,
this one is not checked for existence though, only the syncthing folder name is.

```bash
sync_location default
# /home/user/Sync/

sync_location downloads
# /home/user/Downloads/

sync_location downloads subfolder/fileorfolder
# /home/user/Downloads/subfolder/fileorfolder
```

## License

The sync location tool is created by [Jelmer van Arnhem](https://github.com/Jelmerro)
and may be copied and modified under the terms of the [MIT license](./LICENSE).
