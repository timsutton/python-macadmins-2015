#!/usr/bin/python
#
# Some preferences for Adobe Acrobat products are painful to manage.
# Sample prefs for Reader that disable the "associate Reader with all
# PDFs" (the 'AVAlert' key), and accepting the EULA ('EULAAccepted')
#   <key>11</key>
#   <dict>
#       <key>AVAlert</key>
#       <dict>
#           <key>Checkbox</key>
#           <array>
#               <integer>8</integer>
#               <dict>
#                   <key>OptionToOwn</key>
#                   <array>
#                       <integer>1</integer>
#                       <integer>1</integer>
#                   </array>
#               </dict>
#           </array>
#       </dict>
#       <key>EULAAccepted</key>
#       <true/>
#   </dict>
#
#
# This thread regarding administrators trying to pre-accept the
# EULA for Adobe Reader is a great example. The Reader/Acrobat browser
# plugins require you to first accept the EULA to use them, which must
# be done from within the "full" application.
#
# https://forums.adobe.com/thread/1579676
# 1. There is no way to simply set this system-wide via some special file, or for
#    example using the "feature lockdown" mechanism Adobe has for Acrobat
#    (other things like disabling the built-in autoupdater can be, but not the EULA)
# 2. The preference key that stores this can be managed with something like a
#    configuration profile, but because all prefs live within a "hive" for each
#    major version, any management of that preference key would clobber all the user
#    preferences within. Config profiles can only set a top-level key, not merge
#    in various nested keys.
# 3. Posts in the thread only refer to "replacing a plist" without understanding
#    that the preferences caching daemon (cfprefsd) is already caching these behind
#    the scenes. There's a "workaround" of rebooting the machine...
#
# The solution: know the specific nested pref key that we would need to merge in,
# and do the merge ourselves, using CFPreferences, not raw plist manipulation.
# (This is not legal advice about pre-accepting EULAs)
#
# More on Acrobat "Enterprise Administration", see for example the notion
# of the "version hive":
# http://www.adobe.com/devnet-docs/acrobatetk/tools/AdminGuide/preferences.html
#
# Also this on the Customization Wizard:
# http://www.adobe.com/devnet-docs/acrobatetk/tools/MacWiz/index.html
# "Do not use this product with Adobe Reader."
#
# A sample PDF that can be opened in Safari or Firefox for testing:
# http://www.urartuuniversity.com/content_images/pdf-sample.pdf
#
# CoreFoundation release notes for 10.6-10.8:
# https://developer.apple.com/library/mac/releasenotes/DataManagement/RN-CoreFoundationOlderNotes

from Foundation import CFPreferencesAppSynchronize, \
                       CFPreferencesCopyAppValue, \
                       CFPreferencesSetMultiple, \
                       kCFPreferencesAnyHost, \
                       kCFPreferencesCurrentUser


major_versions = ['10', '11', 'DC', '2015']

final_prefs = {}

for version in major_versions:
    prefs_for_vers = CFPreferencesCopyAppValue(version, 'com.adobe.Reader')
    if prefs_for_vers:
        print "Found existing key '%s'" % version
        # if there were preferences, then make a copy and put these in
        # our final_prefs we're building
        # - mutableCopy() isn't Python, it's Objective-C - this is because
        #   the Objective-C wrapping around CFPreferences returns immutable
        #   copies, and we want to add our data (EULAAccepted) to these
        final_prefs[version] = prefs_for_vers.mutableCopy()
    else:
        # if no prefs key for this version, create the key as an empty dict
        # for us to add the EULA key to
        print "No existing key for '%s', creating new dict" % version
        final_prefs[version] = {}

    if 'EULAAccepted' not in final_prefs[version]:
        print "No EULAAccepted key present, adding to '%s'" % version
        final_prefs[version]['EULAAccepted'] = True

# We could print out all the prefs here
# print final_prefs

# Note: this seems odd that we might have Objective-C dict types
# in some keys and Python dict types in others, but PyObjC massages
# this for us and in the end we're using a standard system API to
# set the preference

# finally, the equivalent of `defaults write` this new pref we've assembled
CFPreferencesSetMultiple(
    final_prefs,                # 1. our dictionary of keys/values to set
    [],                         # 2. a list of keys to _remove_
    'com.adobe.Reader',         # 3. the domain
    kCFPreferencesCurrentUser,  # 4. current- or any-user (ie. ~/L/P or /L/P)
    kCFPreferencesAnyHost       # 5. current- or any-host (ie. ByHost or not)
)

# not required on 10.8 and higher unless you need to synchronously
# read com.adobe.Reader prefs from another process/app
CFPreferencesAppSynchronize('com.adobe.Reader')
