# Contingent Input Botherer

A very simple python script that, every whipstitch or so, checks to see if the keyboard has been used or if the mouse has moved noticeably from the last place it was spotted. If not, it toggles the cmd key (AKA the "meta" or "super" key, e.g. Windows key) and moves the mouse back or forth a little bit.

There is no termination condition, so when you don't want it any more you have to kill it yourself.

## Parameters

* `sleepinterval`: time in seconds between checks
* `dx`, `dy`: Both "how far does the mouse need to move to count as significant" and "how far does the script move the mouse when the script moves the mouse".
* `verbose`: If supplied, the script will output a timestamp and explanation each time it decides whether or not to bother the input.

## Usage

`python contingent_input_botherer.py [sleepinterval: default 60 seconds] [dx: default 5px] [dy: default 5px] [verbose: default False]`
