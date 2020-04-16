#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/tujiaqi/Desktop/grc/tutorial/gr-tutorial/python
export PATH=/home/tujiaqi/Desktop/grc/tutorial/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/tujiaqi/Desktop/grc/tutorial/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/tujiaqi/Desktop/grc/tutorial/gr-tutorial/python/qa_multiply_py_ff.py 
