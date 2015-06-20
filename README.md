# Python for Mac Admins

This is a collection of Python code snippets and scripts that was used throughout my Python for Mac Admins sessions, which took place at the [MacDeploy](http://macdeployment.ca) and [MacDevOpsYVR](http://www.macdevops.ca) western Canada conferences in June 2015. The slides are also available in this repo.

Most of the talk used "interactive" Python. For this you're free to use the standard `python` executable you will find on every OS X system, but I use [IPython](http://ipython.org) for a few added niceties. IPython is _not_ required for running any of these examples.

It can be installed like any other Python package. If you're not familiar with tools like `pip` or `easy_install`, you can still easily install IPython globally (for all users) in a single step: `sudo easy_install ipython`.

For example:

```
➜  ~  sudo easy_install ipython

Searching for ipython
Reading https://pypi.python.org/simple/ipython/
Best match: ipython 3.1.0
Downloading https://pypi.python.org/packages/source/i/ipython/ipython-3.1.0.zip#md5=dfa0766ee4b035f6048740e8fcc9b8bb
Processing ipython-3.1.0.zip
Writing /tmp/easy_install-97WOa8/ipython-3.1.0/setup.cfg
Running ipython-3.1.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-97WOa8/ipython-3.1.0/egg-dist-tmp-mujQVZ
              readline: yes
rebuilding css and sourcemaps failed (not a problem)
invoke is required to rebuild css (pip install invoke)
checking package data
Adding ipython 3.1.0 to easy-install.pth file
Installing ipengine2 script to /usr/local/bin
Installing iptest script to /usr/local/bin
Installing ipython2 script to /usr/local/bin
Installing ipcluster2 script to /usr/local/bin
Installing ipcluster script to /usr/local/bin
Installing ipython script to /usr/local/bin
Installing ipcontroller2 script to /usr/local/bin
Installing ipcontroller script to /usr/local/bin
Installing iptest2 script to /usr/local/bin
Installing ipengine script to /usr/local/bin

Installed /Library/Python/2.7/site-packages/ipython-3.1.0-py2.7.egg
Processing dependencies for ipython
Finished processing dependencies for ipython
```

At this point, you should be able to simply type `ipython` into a terminal, press return, and:

```bash
➜  ~  ipython
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```

Have fun!
