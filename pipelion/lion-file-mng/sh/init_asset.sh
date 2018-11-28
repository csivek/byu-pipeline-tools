#!/bin/bash

PRODUCTION_ROOT="$1"
NAME="$2"
LOCATION="$3"

cd $PRODUCTION_ROOT

if [ ! -d $LOCATION ]; then
  mkdir -p $LOCATION
fi
cd $LOCATION

echo "" > "body.json"

pwd
