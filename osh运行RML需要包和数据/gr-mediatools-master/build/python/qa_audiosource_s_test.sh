#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/tujiaqi/Desktop/grc/gr-mediatools-master/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/tujiaqi/Desktop/grc/gr-mediatools-master/build/python:$PATH
export LD_LIBRARY_PATH=/home/tujiaqi/Desktop/grc/gr-mediatools-master/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/tujiaqi/Desktop/grc/gr-mediatools-master/build/swig:$PYTHONPATH
/usr/bin/python2 /home/tujiaqi/Desktop/grc/gr-mediatools-master/python/qa_mediatools_audiosource_s.py 
