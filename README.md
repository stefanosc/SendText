# SendTest for Sublime Text 2 and 3

This is a modified version of the SendText plugin for Sublime Text.
It's a quick dirty hack to be able to send Rspec tests to terminal.
I might further develop this if I find it useful :)

Below is the original readme from the SendText plugin.

# SendText for Sublime Text 2 and 3

This package sends text to a terminal (or other program). If text is selected, it will send the selection to the terminal when you press cmd-Enter (Mac) or ctrl-Enter (Linux/Windows); if no text is selected, it will send the current line to the terminal and move the cursor to the next line.
This is very useful for coding in interpreted languages.

SendText presently works with:

* Terminal.app on Mac OS X. SendText will send the text to the most recently active Terminal window.
* iTerm on Mac OS X. SendText will send the text to the most recently iTerm window.
* GNU screen on any platform (Linux and Mac OS X). Screen is a terminal multiplexer which you can start in any terminal emulator. SendText will send the text to the most recently active screen session.
* tmux on any platform (Linux and Mac OS X). tmux is a terminal multiplexer (like GNU screen) which you can start in any terminal emulator. SendText will send the text to the most recently active tmux session.


Hopefully in the future it will also be possible to do the following:

* Attach a Sublime Text view to a particular terminal window.

This plugin was originally based on Rtools by Karthik Ram: https://github.com/karthik/Rtools

## Installation

The easy way is to first install the [Package Control](http://wbond.net/sublime_packages/package_control/installation) plugin.
Once it's installed, press Ctrl-Shift-P (or Cmd-Shift-P), type `install`, and select "Package Control: Install Packages".
Then type "sendtext", and choose to install the SendText plugin.

The other way is to clone this git repository into your `Sublime Text 2/Packages` or `Sublime Text 3/Packages` directory. This will be in different places depending on the OS (for ST3, replace the 2 with 3):

* Windows: `%APPDATA%\Sublime Text 2\Packages`
* OS X: `~/Library/Application Support/Sublime Text 2/Packages`
* Linux: `~/.config/sublime-text-2`

```
git clone https://github.com/wch/SendText.git
```

## Program configuration

You can configure SendText by going to:

```
Preferences -> Package Settings -> SendText -> Settings - Default
```

First, choose which terminal program you want to use, and uncomment the appropriate line. For example, this tells SendText to use Terminal.app:

```
    "program": "Terminal.app",
    // "program": "iTerm",
    // "program": "tmux",
    // "program": "screen",
```

If you're using Terminal.app or iTerm, that's all you need to do.
If you use tmux or screen, you may need to explicitly set the path to make it work.
(This seems to be necessary for me on Mac OS X and with tmux installed in `/usr/local/bin`, but YMMV.)
In the `paths`, set the value for tmux or screen to the full path to the executable. For example:

```
    "paths":
    {
        "tmux": "/usr/local/bin/tmux"
        "screen": "/usr/local/bin/screen"
    }
```

## Using SendText

Using SendText is simple. Start your terminal program (of the ones listed above), then, in Sublime Text, select some text and press cmd-Enter (or ctrl-Enter).


## Configuring key bindings

To change the key bindings, go to:

```
Preferences -> Package Settings -> SendText -> Key Bindings - Default
```

The default value for Linux and Windows is:

```
[
{ "keys": ["ctrl+enter"], "command": "send_selection" }
]
```

And for Mac OS, it uses the Cmd key (`super`) instead of Ctrl:

```
[
{ "keys": ["super+enter"], "command": "send_selection" }
]
```

Change the value of `"keys"` to the key combination you want to use.
