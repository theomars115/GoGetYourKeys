from cx_Freeze import setup, Executable

# Created by J Maria Irudaya Regilan
# website located here: https://regilanj.wordpress.com/

base = None

executables = [Executable("log.py", base=base)]

packages = ["idna", "smtplib", "email", "pynput", "logging", "time"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "Log",
    options = options,
    version = "1",
    description = "",
    executables = executables
)