#!/usr/bin/python3
"""
FileStorage Class

"""

class FileStorage:
	__file_path="file.json"
	__objects={}

	def all(self):
		return FileStorage.__objects

	def new(self, obj):
		FileStorage.__objects['key'] = obj.__class__.__name__.id

	def save(self):
		pass

	def reload(self):
		pass