import platform
from platform import python_version

print(platform.system(), platform.platform(), platform.machine())

print(f"The version of python on my laptop is: {platform.python_version()}")

python_version = platform.python_version()
version = int(python_version[0])
print(version)
if version != 3:
    print("You are not using the appropriate version of python on your device.")
else:
    print("You are using the appropriate version of pythion on your device.")