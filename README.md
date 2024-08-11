# Python-Scripting-Project

This script prompts the user for a directory path that contains game directories and other files. The script performs the following tasks:

Directory Identification and Renaming:

It identifies directories within the specified path that contain the word "game" in their names.
It extracts a new name for each identified directory by removing the "game" element.
Target Directory Creation:

If the target directory does not exist, the script creates it. If it already exists, it will be overwritten.
For each game directory, a new directory is created inside the target directory, using the name derived in the previous step (without the "game" in the directory's name).
All contents of the original game directories are copied to the corresponding new directories in the target location.
JSON Metadata Creation:

The script generates a JSON file that contains metadata about the game directories, including the names of the game directories and the total number of them.
Code Compilation and Execution:

The script compiles the code inside a specified directory and executes it using a subprocess.