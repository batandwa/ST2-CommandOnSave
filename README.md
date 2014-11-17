ABOUT
=====
This plugin is based on Klaas Cuvelier's original Command-On-Save plugin.

This plugin executes a certain command after saving a file.
Commands can be specific to folder, filename, extension, or root name. Additionally, certain variables may be used.

INSTALLATION
============
Clone the git repository into your packages folder:

    git clone git://github.com/stuckpixel-ryan/ST2-CommandOnSave.git CommandOnSavePlus

SETTINGS
========
There a Base File for settings, in there you specify which command needs to be executed.
You can see some examples in the file.

You can use these placeholders in your command to do substitution, based on the saved file's path:
- **%PROJECT_FOLDER%** - The project folder. If there are multiple directories, the first one will be used.
- **%FILE_FOLDER%** - The full path directory to the directory where the edited file is contained.
- **%FILE_NAME%** - The name of the file, including the extension, excluding the directory path. Aka basename.
- **%FILE_PATH%** - The full path to the file.

**Note:** If more than one set of rules matches your file, the commands for each will be executed in the order they're listed in the settings.