import sublime
import sublime_plugin
import subprocess
import string
import tempfile

settings = {}

class SendTestCommand(sublime_plugin.TextCommand):
    @staticmethod
    def escapeString(s):
        s = s.replace('\\', '\\\\')
        s = s.replace('"', '\\"')
        return s

    @staticmethod
    def send(selection):
        prog = settings.get('program')

        if prog == "Terminal.app":
            # Remove trailing newline
            selection = selection.rstrip('\n')
            # Split selection into lines
            selection = SendSelectionCommand.escapeString(selection)

            subprocess.call(['osascript', '-e',
                'tell app "Terminal" to do script "' + selection + '" in window 1'])

        elif prog == "iTerm":
            # Remove trailing newline
            selection = selection.rstrip('\n')

            # If it ends with a space, add a newline. iTerm has a quirk where
            # if the scripted command doesn't end with a space, it automatically
            # adds a newline. but if it does end with a space, it doesn't add a newline.
            if (selection[-1] == " "):
                selection = selection + "\n"

            selection = SendSelectionCommand.escapeString(selection)

            subprocess.call(['osascript', '-e', 'tell app "iTerm"',
                '-e', 'set mysession to current session of current terminal',
                '-e', 'tell mysession to write text "' + selection + '"',
                '-e', 'end tell'])

        elif prog == "tmux":
            # Get the full pathname of the tmux, if it's
            progpath = settings.get('paths').get('tmux')
            # If path isn't specified, just call without path
            if not progpath:
                progpath = 'tmux'

            subprocess.call([progpath, 'set-buffer', selection])
            subprocess.call([progpath, 'paste-buffer', '-d'])

        elif prog == "screen":
            # Get the full pathname of the tmux, if it's
            progpath = settings.get('paths').get('screen')
            # If path isn't specified, just call without path
            if not progpath:
                progpath = 'screen'

            if len(selection)<2000:
                subprocess.call([progpath, '-X', 'stuff', selection])
            else:
                with tempfile.NamedTemporaryFile() as tmp:
                    with open(tmp.name, 'w') as file:
                        file.write(selection)
                        subprocess.call([progpath, '-X', 'stuff', ". %s\n" % (file.name)])


    def run(self, edit):
        global settings
        settings = sublime.load_settings('SendTest.sublime-settings')
        test_cmd = settings.get('test_cmd')
        view = sublime.Window.active_view(sublime.active_window())
        # row, col = self.view.rowcol(self.view.sel()[0].begin())

        # join test framework command with current file name
        command = ' '.join([test_cmd, view.file_name()])

        self.send(command)
