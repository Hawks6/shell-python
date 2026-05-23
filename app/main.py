import subprocess
import sys
import os
import subprocess


def main():
    
    while True:
        sys.stdout.write("$ ")

    # pass
        commands = ['echo','type','exit']
        command = input()
        found = False
        command_parts = command.split(' ')
        command_name = command_parts[0]
        
        path = os.environ.get("PATH","")
        directories = path.split(os.pathsep)
        if(command == 'exit'):
            break
        elif(command.startswith("echo")):
            print(command[5:])
        elif(command.startswith("type")):
            if(command[5:] in commands):
                print(f"{command[5:]} is a shell builtin")
            else:
                for directory in directories:
                    command_exe = command[5:].strip()
                    full_path = os.path.join(directory, command_exe)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{command[5:]} is {full_path}")
                        found = True
                        break
                if not found:
                    print(f"{command[5:]}: not found")
        else:
            for directory in directories:
                full_path = os.path.join(directory, command_name)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    subprocess.run([command_name]+ command_parts[1:], executable=full_path)
                    found =True

            

                    



            if not found:
                print(f"{command}: command not found")
        

if __name__ == "__main__":

    main()
