import os
from colorama import init, Fore
init(autoreset=True)
import art
from art import tprint

tprint("File     Manager")
print("™   ╰─ Created by Namesys.\n\n")

print(f'Please, apply {Fore.MAGENTA}settings{Fore.RESET}...\n')
print(f'{Fore.MAGENTA}    (1){Fore.RESET} > Disable "tree".')
print(f'{Fore.MAGENTA}    (2){Fore.RESET} > Turn off farewell message upon exit.\n')
print(f'Type {Fore.MAGENTA}1{Fore.RESET} or {Fore.MAGENTA}2{Fore.RESET} to apply one of the settings.')
print(f'Type {Fore.MAGENTA}all{Fore.RESET} to apply all settings.')
print(f'Type {Fore.YELLOW}Enter{Fore.RESET} or anything else to skip and don\'t applying settings.\n')
print()
settings = input(">>> ")


# optione
print(f'Please, select an {Fore.YELLOW}option{Fore.RESET}...\n')
print(f'{Fore.RED}    [{Fore.YELLOW}i{Fore.RED}]{Fore.RESET} — About program.')
print(f'{Fore.RED}    [{Fore.YELLOW}c{Fore.RED}]{Fore.RESET} — Contact developer.')
print(f'{Fore.RED}    [{Fore.YELLOW}q{Fore.RED}]{Fore.RESET} — Quit.\n')
print(f'{Fore.RED}    [{Fore.YELLOW}1{Fore.RED}]{Fore.RESET} — ls.')
print(f'{Fore.RED}    [{Fore.YELLOW}2{Fore.RED}]{Fore.RESET} — Navigating through directories.')
print(f'{Fore.RED}    [{Fore.YELLOW}3{Fore.RED}]{Fore.RESET} — Print the contents of the file.')
print(f'{Fore.RED}    [{Fore.YELLOW}4{Fore.RED}]{Fore.RESET} — Print the contents of the directory.')
print(f'{Fore.RED}    [{Fore.YELLOW}5{Fore.RED}]{Fore.RESET} — Delete file or directory.')
print(f'{Fore.RED}    [{Fore.YELLOW}6{Fore.RED}]{Fore.RESET} — Create new file.')
print(f'{Fore.RED}    [{Fore.YELLOW}7{Fore.RED}]{Fore.RESET} — Create a new directory.')
print(f'{Fore.RED}    [{Fore.YELLOW}8{Fore.RED}]{Fore.RESET} — Rename file or directory.')
print(f'{Fore.RED}    [{Fore.YELLOW}9{Fore.RED}]{Fore.RESET} — Move file or directory.')
print(f'{Fore.RED}   [{Fore.YELLOW}10{Fore.RED}]{Fore.RESET} — Display information about the file.')
print(f'{Fore.RED}   [{Fore.YELLOW}11{Fore.RED}]{Fore.RESET} — Edit a file.')
print(f'{Fore.RED}   [{Fore.YELLOW}12{Fore.RED}]{Fore.RESET} — Copy file.')
print(f'\n{Fore.YELLOW}Note:{Fore.RESET} you can cancel an operation by pressing Enter or typing "q".')
print()
while True:
    option = input("OPTION: ")

    if option == 'i' or option == 'I':
        print("\nFile Manager this is my personal little project.\nI created it to make it easier to work with files, directories and other data.\nIf you have any ideas or encounter a problem, please contact me.\n")

    elif option == '1':
        print()
        os.system('ls -A')
        if settings == '2' or settings == 'all':
            os.system('tree')
            print()
        else:
            print()
    elif option == '2':
        print("\nChoose the "+Fore.YELLOW+"action"+Fore.RESET+"...")
        print(f'\n{Fore.MAGENTA}      [1]{Fore.RESET} — Move to directory.')
        print(f'{Fore.MAGENTA}      [2]{Fore.RESET} — Move back directory.')
        print(f'{Fore.MAGENTA}      [3]{Fore.RESET} — Move to root directory.')
        print(f'{Fore.MAGENTA}      [4]{Fore.RESET} — Back.\n')

        extraoption = input("EXTRA OPTION: ")
        if extraoption == '2':
            current_dir = os.getcwd()
            os.chdir(os.path.abspath(os.path.join(current_dir, os.pardir)))
        elif extraoption == '3':
            os.chdir('/data/data/com.termux/files/home')
        elif extraoption == '1':
            print()
            os.system('ls -A')
            print()
            dirname = input("ENTER DIRECTORY NAME: ")
            os.chdir(dirname)
        elif extraoption == '4':
            print("OPERATION CANCELED")
        else:
            print(f'{Fore.RED}ERR: {Fore.RESET}invalid option!')

    elif option == '3':
        print()
        os.system('ls -A')
        print("\nChoose a file...    (Press Enter or \"q\" to cancel operation.)")
        filename = input("FILE NAME: ")
        if filename == '' or filename == 'q':
            print("OPERATION CANCELED")
        else:
            os.system('cat '+filename)

    elif option == '4':
        print()
        os.system('ls -A')
        print("\nChoose a directory...    (Press Enter or \"q\" to cancel operation")
        dirname = input("DIRECTORY NAME: ")
        if dirname == 'q' or dirname == '':
            print("OPERATION CANCELED")
        else:
            path = os.path.abspath(dirname)
            print()

            if os.path.exists(path):
                print("\nDirectory information")
                print("╰─>Path:", path)
                print("╰─>Files and subdirectories:")
                for item in os.listdir(path):
                    print(item)
                print()

                if os.path.isfile(path):
                    print(f'{Fore.RED}ERR: {Fore.RESET}This is a file.')
            else:
                print(f'{Fore.RED}ERR: {Fore.RESET}Directory does not exist.')

    elif option == '5':
        print()
        os.system('ls -A')
        print()
        name = input("DELETE ")
        if name == 'q' or name == '':
            print("OPERATION CANCELED")
        else:
            os.system('rm -rf '+name)
            print(f'{name} HAS BEEN DELETED')

    elif option == '6':
        mkfilename = input("ENTER NAME: ")
        if mkfilename == '' or mkfilename == 'q':
            print("OPERATION CANCELED")
        else:
            os.system('touch '+mkfilename)
            print(f'{mkfilename} HAS BEEN CREATED')

    elif option == '7':
        mkdirname = input("ENTER NAME: ")
        if mkdirname == '' or mkdirname == 'q':
            print("OPERATION CANCELED")
        else:
            os.system('mkdir '+mkdirname)
            print(f'{mkdirname} HAS BEEN CREATED')

    elif option == 'q':
        if settings == '2' or settings == 'all':
           break
        else:
           print("Thank you for using!\n")
           break

    elif option == '8':
        oldname = input("OLD NAME: ")
        newname = input("NEW: ")
        if oldname == 'q' or oldname == '':
            print("OPERATION CANCELED")
        elif newname == 'q' or newname == '':
            print("OPERATION CANCELED")
        else:
            try:
                os.rename(oldname, newname)
            except FileNotFoundError:
                print(f'{Fore.RED}ERR: {Fore.ERROR}{oldname} not found.')

    elif option == 'c':
        print("\nTelegram: @drttm\n\nOther:\nGitHub: NamesysF\n\n\nI can speak on Russian and English.\n")

    elif option == '9':
        print()
        os.system('ls -A')
        print('\nSelect object...')
        source = input("PRESS ENTER TO CONTINUE... ")
        if source == '' or source == 'q':
            print("OPERATION CANCELED")
        else:
            dest = input("PATH: ")
            if not os.path.exists(dest):
                print(f'{Fore.RED}ERR: {Fore.RESET}path {dest} is not valid.')
            else:
                try:
                    new_path = os.path.join(dest, os.path.basename(source))
                    os.replace(source, new_path)
                    print(f'{source} MOVED TO {new_path}')
                except Exception as MoveErr:
                    print(f'{Fore.RED}MOVE ERR: {Fore.RESET}unknown error has occurred.\n{Fore.RED}{MoveErr}')

    elif option == '10':
        def file_information():
            file_path = input("WAY TO FILE: ")
            if file_path == '' or file_path == 'q':
                print("OPERATION CANCELED")
            else:
                file_name = os.path.basename(file_path)
                print("\nName:", file_name)
                file_dir = os.path.dirname(file_path)
                print("Path:", file_dir)
                file_size = os.path.getsize(file_path)
                print("Size:", file_size, "bytes")
                file_extension = os.path.splitext(file_path)[1]
                print("Extension:", file_extension+"\n")

        file_information()

    elif option == '11':
        print()
        os.system('ls -A')
        filename = input("FILE NAME: ")
        if filename == '' or filename == 'q':
            print("OPERATION CANCELED")
        else:
            os.system('nano '+filename)

    elif option == '12':
        print()
        os.system('ls -A')
        filepath = input("PATH TO FILE: ")
        if filepath == '' or filepath == 'q':
            print("OPERATION CANCELED")
        else:
            dirpath = input("PATH TO DIRECTORY: ")
            if dirpath == '' or dirpath == 'q':
                print("OPERATION CANCELED")
            else:
                os.system('cp '+filepath+' '+dirpath)
                
    else:
        print(f'{Fore.RED}ERR: {Fore.RESET}invalid option!')
