# gshell
# This is a custom shell
import os

print("Welcome to G Shell")

while True:
    cmd = input("[gshell]$ ")
    if cmd == "exit":
        print("Goodbye")
        exit()
    elif cmd == "quit":
        print("Goodbye")
        quit()
    elif cmd == "ls":
        print("Listing files inside this directory...")
        print(os.listdir())
    elif cmd == "lsr":
        print("Listing files inside this directory...")
        print(os.popen("ls").read())
    elif cmd == "mkdir":
        folder_name = input("Folder name: ")
        os.popen("mkdir " + str(folder_name)).read()
    else:
        print("Unknown Command")
