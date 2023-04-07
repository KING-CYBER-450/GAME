import os, sys

try:

    __import__("tx").Main()

except Exception as e:

    exit(str(e))
