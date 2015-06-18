#!/bin/sh
# clearing some app prefs for demonstrating CFPreferences from within Python
defaults write com.apple.Safari NewTabBehavior -integer 0
defaults write com.apple.Safari NewWindowBehavior -integer 0
defaults delete com.apple.Safari HomePage

defaults delete com.adobe.Reader
