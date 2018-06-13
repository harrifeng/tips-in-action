#!/bin/bash
for file in `ls`; do
  newfile=`echo $file | sed 's/.format//g'`
  echo $newfile
  mv $file $newfile
done
