#!/usr/bin/python

# ^^ often we will see a shebang line of #!/usr/bin/env python,
# however we sometimes want to ensure we're really using Apple's
# system python binary - either for use of PyObjC, or because
# we just want to ensure that this specific Python version will
# be run

import glob
import plistlib

from sys import stderr
from xml.parsers.expat import ExpatError

CATALOG_TO_ADD = 'new-business-unit'

for plist_file in glob.glob('pkgsinfo/*.plist'):
    print "Parsing %s.." % plist_file

    try:
        pkginfo = plistlib.readPlist(plist_file)
    except ExpatError:
        print >> stderr, "Malformed plist %s, skipping.." % plist_file
        continue
    except IOError:
        print >> stderr, "Permissions issue reading %s, skipping.." % plist_file
        continue

    # add the new catalog to the existing list, only
    # if it doesn't exist already
    if CATALOG_TO_ADD not in pkginfo['catalogs']:
        pkginfo['catalogs'].append(CATALOG_TO_ADD)

    try:
        # write the plist back to disk, overwriting the original
        plistlib.writePlist(pkginfo, plist_file)
    except IOError:
        print >> stderr, "Could not write %s to disk.. verify write permissions!" % plist_file
