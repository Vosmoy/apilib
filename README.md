# apilib
My library for rdb.altlinux request and CLI-utility which displays:
- all packages that are in the first but not in the second
- all packages that are in the second but not in the first
- all packages, whose version-release is greater in the first than in the second.

## Installation
1. Clone the repository to your local computer using the command: `git clone https://github.com/Vosmoy/apilib.git`
2. Go to the directory with downloaded files `cd apilib`
3. Install the library for CLI utility using the command: `sudo python3 setup.py install`

## Running
1. To start the application, use the command: `python cli-api.py sisyphus p10`. Sisyphus and p10 are two branches for comparison, but you can choose other available branches.
1.1. You can manually choose the architecture, but by default it is x86_64. To select another architecture, add the `--arch` attribute.
1.2 At the end of the command, add `>output.json` if the result is needed for further use.
