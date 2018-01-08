import subprocess

nbr_exec = 5

moyenne_total_time_ms = 0

num_threads = 2
for i in range(nbr_exec):
    # ls = subprocess.run(["./run.sh", num_threads], stdout=subprocess.PIPE)
    # output = ls.stdout.decode("UTF-8")
    # print(output)
    output = '-- Configuring done\n-- Generating done\n-- Build files have been written to: ' \
             '/home/nathan/DEV/PC-optimisation\n[100%] Built target pdc_evol_model\nInit binding matrix\nDone in 440 ' \
             'ms\nCreate World\nDone in 165 ms\nInitialize environment\nDone in 5 ms\nInitialize random ' \
             'population\nSearching for a viable organism .Found !\nFilling the grid\nDone in 8630 ms\nRun ' \
             'evolution\nEvolution at step 0 -- Number of Organism 1024  (Dead: 9 -- Mutant: 9)-- Min Fitness: 0.006481 -- ' \
             'Max Fitness: 0.006481\nDone in 45958 ms\nTotal time : 55201 ms\nNon-regression test successful !\n '

    output_splitted = output.split('\n')

    assert output_splitted[-2] == 'Non-regression test successful !'

    actual_total_time_ms = output_splitted[-3].split(' ')[-2]

    assert actual_total_time_ms.isdigit()
    moyenne_total_time_ms += int(actual_total_time_ms)


total_time_ms = moyenne_total_time_ms / nbr_exec
print(total_time_ms)