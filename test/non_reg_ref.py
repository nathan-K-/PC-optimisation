import csv

best_ref_file = "stats_best_ref.txt"
best_test_file = "../stats_best.txt"

mean_ref_file = "stats_mean_ref.txt"
mean_test_file = "../stats_mean.txt"


def compare_file(file1, file2):
    assert len(file1) == len(test_ref)

    for i in range(len(file1)):
        assert len(file1[i]) == len(file2[i])

        for j in range(len(file1[i])):
            if j != 2:
                a = round(float(file1[i][j]), 4)
                b = round(float(file2[i][j]), 4)
                assert a == b


with open(best_ref_file, 'r') as csv_best_ref, open(best_test_file, 'r') as csv_best_test:
    best_ref = list(csv.reader(csv_best_ref, delimiter=','))
    test_ref = list(csv.reader(csv_best_test, delimiter=','))

    compare_file(best_ref, test_ref)

with open(mean_ref_file, 'r') as csv_mean_ref, open(mean_test_file, 'r') as csv_mean_test:
    mean_ref = list(csv.reader(csv_mean_ref, delimiter=','))
    mean_test = list(csv.reader(csv_mean_test, delimiter=','))

    compare_file(best_ref, test_ref)

print("Non-regression test successful !")
