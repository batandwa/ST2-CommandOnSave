import sublime
import sublime_plugin
import subprocess
import os
import re


class CommandOnSavePlus(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = view.settings()
        cos_plus = settings.get("command_on_save_plus")
        file_path = view.file_name()
        file_folder, file_name = os.path.split(file_path)
        project_folder = view.folders()[0]
        file_root, file_extension = os.path.splitext(file_name)


        for entry in cos_plus:

            setting_command = ''
            setting_folder = ''
            setting_file = ''
            setting_extension = ''
            setting_root = ''


            for k,v in enumerate entry
                if k.match('folder')
                    setting_folder = v
                elif k.match('file')
                    setting_file = v
                elif k.match('extension')
                    setting_extension = v
                elif k.match('root')
                    setting_root = v
                elif k.match('command')
                    setting_command = v
                    setting_command = setting_command.replace('%FILE_NAME%',file_name)
                    setting_command = setting_command.replace('%FILE_PATH%',file_path)
                    setting_command = setting_command.replace('%FILE_FOLDER%',file_folder)
                    setting_command = setting_command.replace('%PROJECT_FOLDER%',project_folder)



            if ( setting_folder.match(file_folder) or len(setting_folder) == 0 ) and ( setting_root.match(file_root) or len(setting_root) == 0 ) and ( setting_file.match(file_name) or len(setting_file) == 0 )  and ( setting_extension.match(file_extension) or len(setting_extension) == 0 )

                if len(setting_command) > 0:
                    subprocess.call([setting_command], shell=True)

        return


def debug(message):
    debug = 'echo "' + message + '" >> ~/.sublime/command_on_save_plus_debug.txt'
    subprocess.call([debug], shell=True)
    return
