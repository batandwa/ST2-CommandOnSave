import sublime
import sublime_plugin
import subprocess
import os
import threading

class CommandThread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        print "Running '%s'" % (self.cmd)

        result = subprocess.call([self.cmd], shell=True)
        if result == 0:
            print "Command '%s' ran successfully" % self.cmd
        else:
            print "Error executing '%s'" % self.cmd

class CommandOnSavePlus(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = sublime.load_settings('CommandOnSavePlus.sublime-settings')
        package_dir = os.path.join(sublime.packages_path(), __name__)
        cos_plus = settings.get("command_on_save_plus")

        file_path = view.file_name()
        file_folder, file_name = os.path.split(file_path)
        window = view.window()
        project_folder = window.folders()[0]
        file_root, file_extension = os.path.splitext(file_name)

        for entry in cos_plus['setting']:

            setting_command = ''
            setting_folder = ''
            setting_file = ''
            setting_extension = ''
            setting_root = ''


            for k,v in entry.iteritems():
                if k == ('folder'):
                    setting_folder = v

                elif k == ('file'):
                    setting_file = v

                elif k == ('extension'):
                    setting_extension = v

                elif k == ('root'):
                    setting_root = v

                elif k == ('command'):
                    setting_command = v
                    setting_command = setting_command.replace('%FILE_NAME%',file_name)
                    setting_command = setting_command.replace('%FILE_PATH%',file_path)
                    setting_command = setting_command.replace('%FILE_FOLDER%',file_folder)
                    setting_command = setting_command.replace('%PROJECT_FOLDER%',project_folder)

            if ( setting_folder == (file_folder) or len(setting_folder) == 0 ) and ( setting_root == (file_root) or len(setting_root) == 0 ) and ( setting_file == (file_name) or len(setting_file) == 0 )  and ( setting_extension == (file_extension) or len(setting_extension) == 0 ):

                if len(setting_command) > 0:
                    CommandThread(setting_command).start()

        return


def debug(message):
    debug = 'echo "' + message + '" >> ~/.sublime/command_on_save_plus_debug.txt'
    subprocess.call([debug], shell=True)
    return
