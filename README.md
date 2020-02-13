![Holberton school logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200212T214854Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7382345320fac4fbe79b2f9f210346e173da2846547dc5ec08dd1b475e9c4c40)
# AirBnB clone Project

## Table of Contents
* [Description](#description)
* [File Structure](#file-structure)
* [Requirements](#requirements)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Man page](#man-page)
* [Example of Use](#example-of-use)
* [Bugs](#bugs)
* [Authors](#authors)

## Description
This is collaborative project made by Luz Adriana Ariza and Campo Elias Pinillos, students of Software Engineering at Holberton School. This repository contains the files for Holberton's **AirBnB clone project**. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

**The Console**

1. Create your data model
2. Manage (create, update, destroy, etc) objects via a console / command interpreter
3. Store and persist objects to a file (JSON file)


## File Structure

These are the files with the custom funtions and system calls, each one contains a brief description:

|   ***File***    |  ***Description***                   |
|---------------|---------------------------------------|
|  [`holberton.h`](./holberton.h)	|  Header file with the prototypes	|
|  [`lsh.c`](./lsh.c) |  Main File functions to execute |
|  [`_prompt.c`](./_prompt.c) |  Prompt and getline file	|
|  [`_execve.c`](./_execve.c)	|  Execute function |
|  [`_strtok.c`](./_strtok.c) | Custom strtok function  |
|  [`_signal.c`](./_signal.c)  | Ctrl + C deal function	|
|  [`_ifdir.c`](./_ifdir.c)  | Checks if the command is only a directory	|


## Requirements
This simple_shell project is designed to run in the Ubuntu 14.04 LTS linux environment and to be compiled using the GNU compiler collection v. gcc 4.8.4 with flags-Wall, -Werror, -Wextra, and -pedantic.

### List of used and allowed system calls and functions:

This files only contains the following allowed funtion and system calls that where used in our .c files:

| ***System call*** | ***Man page*** | ***System call*** | ***Man page*** |
| ------------- | ------------- | ------------- | ------------- |
| access  | man 2 access  | open |  man 2 open |
| write  | man 2 write | opendir |  man 3 opendir |
| perror |  man 3 perror | closedir  | man 3 closedir  |
| execve  | man 2 execve | exit  | man 3 exit  |
| signal |  man 2 signal | fork  | man 2 fork  |
| free  | man 3 free  | wait |  man 2 wait |
| getline  | man 3 getline | isatty  | man 3 isatty  |
| malloc | man 3 malloc |  |   |


## Quick Start
1. Clone repo
```
git clone https://github.com/campopinillos/simple_shell.git
```
2. Change directory to simple_shell
```
cd simple_shell/
```
3. Compile all the `.c` files in /simple_shell
```
gcc -Wall -Werror -Wextra -pedantic *.c -o lsh
```

## Usage

### Interactive Mode:
In interactive mode input is accepted from character input, as follow:
```
> ./lsh
$ /bin/ls -l
total 52
-rw-r--r-- 1 vagrant vagrant   168 Nov 20 01:50 AUTHORS
-rw-r--r-- 1 vagrant vagrant  2789 Nov 20 03:47 README.md
-rw-r--r-- 1 vagrant vagrant   486 Nov 20 00:50 _execve.c
-rw-r--r-- 1 vagrant vagrant   763 Nov 20 01:45 _prompt.c
-rw-r--r-- 1 vagrant vagrant   239 Nov 19 14:35 _signal.c
-rw-r--r-- 1 vagrant vagrant  1039 Nov 19 14:38 _strtok.c
-rwxr-xr-x 1 vagrant vagrant 18278 Nov 20 01:46 a.out
-rw-r--r-- 1 vagrant vagrant   394 Nov 19 21:37 holberton.h
-rw-r--r-- 1 vagrant vagrant   443 Nov 20 00:55 lsh.c
-rw-r--r-- 1 vagrant vagrant     0 Nov 20 01:31 man_1_simple_shell
```

### Non-Interactive Mode:
In non-interactive mode, the shell is run from commands being piped in. The subshell
is only opened as the command is carried out and closes at the completion of the command.

```
> echo "/bin/ls -l"  | ./lsh
total 52
-rw-r--r-- 1 vagrant vagrant   168 Nov 20 01:50 AUTHORS
-rw-r--r-- 1 vagrant vagrant  2789 Nov 20 03:47 README.md
-rw-r--r-- 1 vagrant vagrant   486 Nov 20 00:50 _execve.c
-rw-r--r-- 1 vagrant vagrant   763 Nov 20 01:45 _prompt.c
-rw-r--r-- 1 vagrant vagrant   239 Nov 19 14:35 _signal.c
-rw-r--r-- 1 vagrant vagrant  1039 Nov 19 14:38 _strtok.c
-rwxr-xr-x 1 vagrant vagrant 18278 Nov 20 01:46 a.out
-rw-r--r-- 1 vagrant vagrant   394 Nov 19 21:37 holberton.h
-rw-r--r-- 1 vagrant vagrant   443 Nov 20 00:55 lsh.c
-rw-r--r-- 1 vagrant vagrant     0 Nov 20 01:31 man_1_simple_shell
```

## Man page
For further information please refer to the man page - accessed in terminal with:
```
> man ./man_1_simple_shell
```

## Example of Use

Some other examples to execute commands in the ./lsh interactive mode:
```
~/simple_shel > ./lsh
```
**ls**:
```
$ ls
AUTHORS    _prompt.c  a.out	   man_1_simple_shell README.md  _signal.c  holberton.h _execve.c  _strtok.c  lsh.c
```
**pwd**:
```
$ pwd
/home/vagrant/simple_shell
```

## Bugs
No known bugs. Please contact any of the authors if a bug appears.


## Authors
* **Luz Adriana Ariza** - [AdrianaAriza](https://github.com/AdrianaAriza) - [@Adriana92060737](https://twitter.com/Adriana92060737)

* **Campo Elias Pinillos** - [campopinillos](https://github.com/campopinillos) - [@campopinillos](https://twitter.com/CampoPinillos)
