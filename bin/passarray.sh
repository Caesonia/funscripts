#!/bin/bash
declare -a passarray
mapfile passarray < "$1"
#echo ${passarray[@]}
for i in ${passarray[@]};do
	echo 'This is your user:' "$i"
done




