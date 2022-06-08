#!/bin/bash

DISPERSION=0.89

build_path() {
  echo "images/hist-$1.png"
}


build_args() {
  echo "$DISPERSION $(build_path "$1")"
}


for arg in "3.915  handmade-c-dev  $(build_args handmade-c-dev)" \
           "18.548 handmade-py-dev $(build_args handmade-py-dev)" \
           "1.871  lib-c-dev       $(build_args lib-c-dev)" \
           "2.786  lib-py-dev      $(build_args lib-py-dev)" \
           "2.341  lib-c-network   $(build_args lib-c-network)" \
           "3.533  lib-py-network  $(build_args lib-py-network)" \
           "2.031  exec-c-dev      $(build_args exec-c-dev)" \
           "3.246  exec-py-dev     $(build_args exec-py-dev)"
do
  python3 fake_data.py $arg
done
