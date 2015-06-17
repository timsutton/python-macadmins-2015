#!/bin/sh
# sets up demo environment for this unit

if [ $UID -ne 0 ]; then
  echo "Run me with sudo!"
  exit 1
fi

rm -f FoundationPlist.pyc
rm -rf pkgsinfo

cp -R pkgsinfo_orig ./pkgsinfo
chown -R $SUDO_USER ./pkgsinfo

defaults write /Library/Preferences/com.apple.commerce AutoUpdate -bool false
defaults write /Library/Preferences/com.apple.alf globalstate -integer 0
