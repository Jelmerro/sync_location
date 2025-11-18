sync\_location
==============

Read, parse and expose syncthing folder locations by name

## Features

The sync location tool will read the syncthing configuration for the current machine,
and expose the locations based on the syncthing folder name.

#### Downloads

In addition to the syncthing folders, a folder named "downloads" is always exposed.
This will scan for mounted disks in "/mnt/" to use as the base location of the downloads,
or use the user folder as the main fallback location at `~/Downloads`.
If there is a `downloads` folder in the syncthing config, that will be used instead.

## Install

### Module

You can add it to your setup.py or pyproject.toml file as a dependency using:

`sync_location @ git+https://git@github.com/Jelmerro/sync_location@master`

### Pip

```bash
pip install --user -I git+https://github.com/Jelmerro/sync_location
```

### Python

Download or clone the repo, then run `python sync_location.py` directly.

### [Github](https://github.com/Jelmerro/sync_location/releases)

Download a stable installer or executable for your platform from Github.

### [Fedora](https://jelmerro.nl/fedora)

I host a custom Fedora repository that you can use for automatic updates.

```bash
sudo dnf config-manager addrepo --from-repofile=https://jelmerro.nl/fedora/jelmerro.repo
sudo dnf install sync_location
```

## Contribute

You can support my work on [ko-fi](https://ko-fi.com/Jelmerro) or [Github sponsors](https://github.com/sponsors/Jelmerro).
Another way to help is to report issues or suggest new features.
Please try to follow recommendations by flake8 and pylint when developing.
For an example vimrc that can auto-format based on the included linters,
you can check out my personal [vimrc](https://github.com/Jelmerro/vimrc).

## Building

To create your own builds you can use [jfpm](https://github.com/Jelmerro/jfpm).
Please clone or download both this repo and jfpm, then run `../jfpm/release_py_simple.sh`.
This will build releases for various platforms and output them to `dist`.

## Usage as a module

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

## Usage from the Command-line

To find a location for a folder based on its name from the command line,
it's possible to run the script with a single argument that represents the folder name.
If the folder exists, the location will be returned and the program will exit with status 0.
For missing folders, no output is printed and the program exists with status code 1.
Optionally, a second argument can be presented that is appended to the base path,
this one is not checked for existence though, only the syncthing folder name is.
Without arguments, JSON is used to show all folders, similar to the module's `.all`.
Finally, you can list all configured folder names using the `--folders` argument.

```bash
sync_location default
# /home/user/Sync/

sync_location downloads
# /home/user/Downloads/

sync_location downloads subfolder/fileorfolder
# /home/user/Downloads/subfolder/fileorfolder

sync_location
# {
#     "default": "/home/user/Sync/",
#     "downloads": "/home/user/Downloads/"
# }

sync_location --folders
# default
# downloads
```
