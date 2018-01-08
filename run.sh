#!/usr/bin/env bash
cmake .
echo $1
make
export OMP_NUM_THREADS=$1
./pdc_evol_model
cd test && python3 non_reg_ref.py
