#!/usr/bin/env bash
echo "This is a shell script"
echo '$1 is' "$1"
echo '$@ is' "$@"
for i in $@; do
	echo "$i"
done
