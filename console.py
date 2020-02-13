#!/usr/bin/python3
"""
HBNB Console

"""
import cmd


class HBNBCommand(cmd.Cmd):
	""" Console """
	prompt = '> '
	intro = "Welcome!"

if __name__ == '__main__':
    HBNBCommand().cmdloop()
