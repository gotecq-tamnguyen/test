# 2023 - Week 01 - Operating System and Git
## 1. [Hello World exercise](src/hello.py)
- Make a `hello_world` file what print `Hello World!` in terminal an run it.
## 2. OS Practice
Disclaimer: the `homework` folder in the exercise is `os_practice` folder in this repo
- install `neofetch` .
- install `neovim` .
- create new directory name: `os_practice` . Check [here](src/os_practice)
- create new file name `system_information` in `os_practice` directory.
- write down the `neofetch` information into `system_information`. Check [here](src/os_practice/archived/system_information)
- create directory name `system` in `os_practice` directory.
- move file `system_information` into system folder.
- duplicate `system` folder.
- set new folder name `archived` .
- create new directory name: `script` into `system` .
- create new file name `echo`
- write some `echo` command into `echo` file with `neovim` . Check [here](src/os_practice/system/script/echo)
- set permission `execute` for `echo` file: ``` chmod +x echo ```
- run `echo` file
- create new folder name `command_meaning` in system folder. Check the folder [here](src/os_practice/archived/command_meaning)
- writedown the user manual of any command ( `man` command) you learn into file. (Ex: The `ls` manual command will be written to the filename `ls`). Automatic this step will get big bonus point. Check [here](src/os_practice/archived/command_meaning/write_man.sh)
- Move the `command_meaning` folder to archived folder.
### Directory structure 
```
└── os_practice
    ├── archived
    │   ├── command_meaning
    │   │   ├── cp
    │   │   ├── ls
    │   │   ├── mkdir
    │   │   ├── touch
    │   │   ├── vi
    │   │   └── write_man.sh
    │   └── system_information
    └── system
        ├── script
        │   ├── advance.sh
        │   └── echo
        └── system_information
```
### Advance exercise
- Write a bash file to install all necessary tools, includes:
- Update latest package via "Package manager"(apt)
- Terminal (yakuake/tmux)
- Shell (Zsh/Fish)
- Git
- Text editor
- Browser
- Zulip
- Ibus-bamboo
* Check the file [here](src/os_practice/system/script/advance.sh)