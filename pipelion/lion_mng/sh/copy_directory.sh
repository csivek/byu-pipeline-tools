#!/bin/bash

ORIGIN="$1"
DESTINATION="$2"


#check if directory already exists
if [ -d $ORIGIN ]; then
  cp -r $ORIGIN"/." $DESTINATION
fi
