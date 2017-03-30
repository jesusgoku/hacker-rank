Min Max
===

Test with large input data
---

```sh
python min_diff.py < test_inputs/input-test_case-7.txt | diff test_inputs/output-test_case-7.txt -
```

Profile performance
---

```sh
python -m cProfile min_diff.py < test_inputs/input-test_case-7.txt
```
