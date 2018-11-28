#!/bin/sh

# project_pipelion.sh: sources the necessary files to get PySide2 and Qt5 working using
# @author Cory Sivek

# source project environment
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source ${DIR}/project_env.sh

# To get PySide2 to work outside of any other software
export PYTHONPATH=$PYTHONPATH:/opt/hfs.current/python/lib/python2.7/site-packages-ui-forced
export QT_QPA_PLATFORM_PLUGIN_PATH=/opt/hfs.current/dsolib/Qt_plugins/platforms
export PATH=/opt/hfs.current/python/bin:$PATH
