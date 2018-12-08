#!/bin/bash

DIRECTORY="$1"

if [ ! -d $DIRECTORY ]; then
  mkdir -p $DIRECTORY
fi
