#! /usr/bin

# Formatting the files
python3 updateFormat.py hbwall3.txt f1.txt
python3 updateFormat.py vgrall3.txt f2.txt

# Removing the common patterns
python3 removeCommons.py

# f1.txt is the updated hbw file
cp f1.txt updatedHBW.txt


echo "Initial hbwall3 file size: $(wc -l < hbwall3.txt)"
echo "f1.txt file size: $(wc -l < f1.txt)"
echo "updatedHBW-shared.txt file size: $(wc -l < updatedHBW-shared.txt)"
