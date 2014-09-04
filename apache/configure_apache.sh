#!/bin/bash

set -x

#for s in *.site; do 
#	bn=`basename "$s" .site`
#	sudo install -p ./$s $apache_avail_sites/$bn
#done

# enable apache modules
sudo a2enmod proxy* rewrite*


