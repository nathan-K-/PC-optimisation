import subprocess
import csv
import time

nbr_exec = 2
nbr_threads = 4

log_file = "perfs_log-" + str(int(time.time())) + ".csv"

with open(log_file, 'a') as csvfile:
    fieldnames = ["# of threads", "execution", "tests success", "total time (ms)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for thr in range(1, nbr_threads+1):

        for i in range(nbr_exec):
            ls = subprocess.run(["./run.sh", str(thr)], stdout=subprocess.PIPE)
            output = ls.stdout.decode("UTF-8")
            # print(output)
            #output = '-- Configuring done\n-- Generating done\n-- Build files have been written to: ' \
             ##        '/home/nathan/DEV/PC-optimisation\n[100%] Built target pdc_evol_model\nInit binding matrix\nDone in 440 ' \
              #       'ms\nCreate World\nDone in 165 ms\nInitialize environment\nDone in 5 ms\nInitialize random ' \
              #       'population\nSearching for a viable organism .Found !\nFilling the grid\nDone in 8630 ms\nRun ' \
              #       'evolution\nEvolution at step 0 -- Number of Organism 1024  (Dead: 9 -- Mutant: 9)-- Min Fitness: 0.006481 -- ' \
              #       'Max Fitness: 0.006481\nDone in 45958 ms\nTotal time : 55201 ms\nNon-regression test successful !\n '

            output_splitted = output.split('\n')

            if output_splitted[-2] != 'Non-regression test successful !':
                writer.writerow({"# of threads": thr, "execution": i, "tests success": False,
                                 "total time (ms)": None})
                csvfile.flush()
                continue

            actual_total_time_ms = output_splitted[-3].split(' ')[-2]

            if actual_total_time_ms.isdigit():
                writer.writerow({"# of threads": thr, "execution": i, "tests success": True,
                                 "total time (ms)": actual_total_time_ms})
                csvfile.flush()

