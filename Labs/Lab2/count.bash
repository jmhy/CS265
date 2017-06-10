#!/bin/bash
#By Joseph Haggerty

ls -a | while read file; do
	if [ -f "$file" ] ; then
		name="$(basename "$file")"
		echo "$name" "$(wc -l < "$file")" "$(wc -w < "$file")"
	fi
done
