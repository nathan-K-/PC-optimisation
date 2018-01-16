#!/usr/bin/env bash
cmake .
make
export OMP_NUM_THREADS=$1
./pdc_evol_model $2
cd test && python3 non_reg_ref.py
