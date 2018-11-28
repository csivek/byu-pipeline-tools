#!/bin/bash

PRODUCTION_ROOT="$1"
LOCATION="$2"

cd $PRODUCTION_ROOT

if [ ! -d $LOCATION ]; then
  rm -r $LOCATION
fi
cd $LOCATION

pwd
