###### I had previously written a program in [iq-ship](https://github.com/ctrl-alt-Defeat-icpc/iq-ship) for converting different versions of Domjudge to Quera.

# Convert Hoj format samples to Quera

This program works very simply. Just copy and paste the folder containing the Hoj test cases into the contest folder. Then run the program. Finally, in the contest folder, only the folder containing the Quera formats will remain.
Finally, just upload the zip file corresponding to the question in the Quera questions and that's it!

<details><summary><strong>Quera files format</strong></summary>

```
./contest_name
    ./[problem_letter]
        problem.zip
            ./in
                input[test_case_number].txt
            ./out
                output[test_case_number].txt
            tester.cpp # tester file
```
</details>

<details><summary><strong>Hoj files format</strong></summary>

```
./contest_name
    problem_[number]_testcase_[some_numbers].zip
        [test_case_number].in
        [test_case_number].out
        info
```
</details>
