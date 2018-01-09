import subprocess
import csv
import time
import psutil

nbr_exec = 4
nbr_threads = psutil.cpu_count()

# TODO apres un checkout, ecraser Common.h (nbr steps) et main (taille de la grille en parametre)

filename_fort = "perfs_echelle_fort-" + str(int(time.time())) + ".csv"
filename_faible = "perfs_echelle_faible-" + str(int(time.time())) + ".csv"


def passage_echelle_fort(filename_fort):
    with open(filename_fort, 'a') as csvfile:
        fieldnames = ["# of threads", "execution", "tests success", "total time (ms)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for thr in range(1, nbr_threads + 1):

            for i in range(nbr_exec):
                ls = subprocess.run(["./run.sh", str(thr)], stdout=subprocess.PIPE)
                output = ls.stdout.decode("UTF-8")

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


def passage_echelle_faible(filename_faible):
    with open(filename_faible, 'a') as csvfile:
        fieldnames = ["# of threads", "taille_grille","execution", "tests success", "total time (ms)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for thr in range(1, nbr_threads + 1):

            for i in range(nbr_exec):
                ls = subprocess.run(["./run.sh", str(thr), str(8*nbr_threads)], stdout=subprocess.PIPE)
                output = ls.stdout.decode("UTF-8")

                output_splitted = output.split('\n')

                if output_splitted[-2] != 'Non-regression test successful !':
                    writer.writerow({"# of threads": thr, "execution": i, "tests success": False,
                                     "total time (ms)": None, "taille_grille": None})
                    csvfile.flush()
                    continue

                actual_total_time_ms = output_splitted[-3].split(' ')[-2]

                if actual_total_time_ms.isdigit():
                    writer.writerow({"# of threads": thr, "execution": i, "tests success": True,
                                     "total time (ms)": actual_total_time_ms, "taille_grille": 8*nbr_threads})
                    csvfile.flush()


passage_echelle_fort(filename_fort)
passage_echelle_faible(filename_faible)