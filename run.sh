#!/usr/bin/env bash
cmake .
make
echo $1
export OMP_NUM_THREADS=$1
./pdc_evol_model
cd test && python3 non_reg_ref.py
