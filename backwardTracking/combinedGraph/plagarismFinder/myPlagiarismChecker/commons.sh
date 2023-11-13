#! /usr/bin

# Formatting the files
python3 updateFormat.py hbwall3.txt f1.txt
python3 updateFormat.py vgrall3.txt f2.txt

# Removing the common patterns
python3 removeCommons.py
