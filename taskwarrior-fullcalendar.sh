#!/bin/bash

python taskwarrior-fullcalendar.py "$(task $@ export)" > output.html
sensible-browser output.html &
