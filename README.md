![Holberton school logo](https://github.com/campopinillos/AirBnB_clone/blob/master/hbnb.png)
# AirBnB clone Project

## Table of Contents
* [Description](#description)
* [File Structure](#file-structure)
* [Requirements](#requirements)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)

## Description
This is collaborative project made by Luz Adriana Ariza and Campo Elias Pinillos, students of Software Engineering at Holberton School. This repository contains the files for Holberton's **AirBnB clone project**. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

**The Console**

Will help us to:

1. Create your data model
2. Manage (create, update, destroy, etc) objects via a console / command interpreter
3. Store and persist objects to a file (JSON file)

In this case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## File Structure

These are the files with the custom funtions and system calls, each one contains a brief description:



|   ***File***    |  ***Description***                   |
|---------------|---------------------------------------|
|  [`console.py`](./console.py)	|  Console file	|
|  [`models`](./models) |  Contains all the classes |
|  [`models/__init__`](./models/__init__.py) |  Connects with filestorage |
|  [`models/base_model`](./models/base_model.py) |  Base Model class |
|  [`models/user`](./models/user.py) |  User class |
|  [`models/state`](./models/state.py) |  State class |
|  [`models/city`](./models/city.py) |  City class |
|  [`models/place`](./models/place.py) |  Place class |
|  [`models/amenity`](./models/amenity.py) |  Amenity class |
|  [`models/review`](./models/review.py) |  Review class |
|  [`models/engine`](./models/engine) |  Contains File Storage engine |
|  [`models/engine/file_storage`](./models/engine/file_storage.py) |  File Storage module |
|  [`tests`](./tests) |  Prompt and getline file	|
|  [`AUTHORS`](./AUTHORS)	|  AUTHORS file|
|  [`README.md`](./README.md) | README.md file |


## Requirements
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3
* Code should use the PEP 8 style (version 1.7 or more)
* Your code should use the PEP 8 style (version 1.7 or more)


## Quick Start
1. Clone repo
```
git clone https://github.com/campopinillos/AirBnB_clone.git
```
2. Change directory to simple_shell
```
cd AirBnB_clone/
```
3. Execute ./console.py
```
> ./console.py
      WELCOME!
        .--. 
       |o_o |
       |!_/ |
      //   \ \ 
     (|     | ) 
    / \_   _/ \ 
    \___)=(___/ 
```

## Usage

In interactive mode input is accepted from character input, as follow:

**create**:
```
(hbnb) create BaseModel
f2f11b8d-f082-494d-8703-d198deb61e3c
(hbnb)
```
**show**:
```
(hbnb) show BaseModel f2f11b8d-f082-494d-8703-d198deb61e3c
[BaseModel] (f2f11b8d-f082-494d-8703-d198deb61e3c) {'id': 'f2f11b8d-f082-494d-8703-d198deb61e3c', 'updated_at': datetime.datetime(2020, 2, 17, 0, 26, 36, 658033), 'created_at': datetime.datetime(2020, 2, 17, 0, 26, 36, 658019)}
(hbnb) 
```
**all**:
```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
**destroy**:
```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```
**to_exit**:
```
(hbnb) quit
> 
```

## Bugs
No known bugs. Please contact any of the authors if a bug appears.


## Authors
* **Luz Adriana Ariza** - [AdrianaAriza](https://github.com/AdrianaAriza) - [@Adriana92060737](https://twitter.com/Adriana92060737)

* **Campo Elias Pinillos** - [campopinillos](https://github.com/campopinillos) - [@campopinillos](https://twitter.com/CampoPinillos)
