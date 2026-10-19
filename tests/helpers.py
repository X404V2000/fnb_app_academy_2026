"""Shared helpers for the test suite: import a script from a unit_X/ folder by path."""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_module(relative_path):
	"""Import a module from a path relative to the repo root.

	The folder is temporarily on sys.path so sibling imports keep working.
	"""
	path = os.path.join(ROOT, relative_path)
	folder = os.path.dirname(path)
	sys.path.insert(0, folder)
	try:
		name = os.path.splitext(os.path.basename(path))[0]
		spec = importlib.util.spec_from_file_location(name, path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		return module
	finally:
		sys.path.remove(folder)
