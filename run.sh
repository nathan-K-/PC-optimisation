cmake .
make
./pdc_evol_model
cd test && python3 non_reg_ref.py