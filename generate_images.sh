#!/bin/bash

DISPERSION=0.89

build_path() {
  echo "images/hist-$1.png"
}


build_args() {
  echo "$DISPERSION $(build_path "$1")"
}


for arg in "3.915 $(build_args handmade-c-dev)" \
           "18.548 $(build_args handmade-py-dev)" \
           "1.871 $(build_args lib-c-dev)" \
           "2.786 $(build_args lib-py-dev)" \
           "2.341 $(build_args lib-c-network)" \
           "3.533 $(build_args lib-py-network)" \
           "2.031 $(build_args exec-c-dev)" \
           "3.246 $(build_args exec-py-dev)"
do
  python3 fake_data.py $arg
done
