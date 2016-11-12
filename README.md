# Hypothesis: Tests that write themselves

Code and slides for my Hypothesis talk at PyCon Canada 2016.
All dependencies needed are listed in `requirements.txt`.
Was written for Python 2.7.12 but any version of 2.7 should work.

### Installation
```
pip install requirements.txt
```

### Running the code
```
pytest <example_file>.py
```
If you want to run with extra Hypothesis stats:
```
pytest --hypothesis-show-statistics <example_file>.py
```

### Following along
If you're following along with the slides the order in which to run the examples are alphabetically or more specifically.

1. add_example.py
2. book_example.py
3. book_example_fixed.py
4. cart_example1.py
5. cart_example1_fixed.py
6. cart_example2.py
7. cart_example2_fixed.py

### Extra materials
A copy of the QuickCheck paper can be found in this repo.

