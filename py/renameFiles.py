#! python3

import shutil, os, re

# Create a regex that matches files with the American date format.
myPattern = re.compile(r"""^(.*?)					# all text before the num
    (\d{3}) 										# num part
    (.*?)$ 											# all text after the num
    """, re.VERBOSE)

filePath = 'F:\\ghost_dsb\\euler\\Euler solutions'
	
# Loop over the files in the working directory.
for oldName in os.listdir(filePath):
    mo = myPattern.search(oldName)

    # Skip files without desired pattern
    if mo == None:
        continue

    # Get the different parts of the filename.
    prePart   = mo.group(1)
    numPart   = mo.group(2)
    namePart  = mo.group(3)
	extension = '.txt'
    

    # Form the new filename.
    newName = prePart + numPart + extension

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(filePath)
    oldName = os.path.join(absWorkingDir, oldName)
    newName = os.path.join(absWorkingDir, newName)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (oldName, newName))
    #shutil.move(oldName, newName) # uncomment after testing
