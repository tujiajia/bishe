#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/tujiaqi/Desktop/grc/gr-mapper-master/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/tujiaqi/Desktop/grc/gr-mapper-master/build/python:$PATH
export LD_LIBRARY_PATH=/home/tujiaqi/Desktop/grc/gr-mapper-master/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/tujiaqi/Desktop/grc/gr-mapper-master/build/swig:$PYTHONPATH
/usr/bin/python2 /home/tujiaqi/Desktop/grc/gr-mapper-master/python/qa_preamble_sync_demapper.py 
