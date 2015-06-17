#!/bin/sh

defaults write com.apple.Safari NewTabBehavior -integer 0
defaults write com.apple.Safari NewWindowBehavior -integer 0
defaults delete com.apple.Safari HomePage
