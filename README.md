# Pearson Regression (Python)

A command-line tool that calculates the Pearson correlation coefficient (`r`) for two sets of numbers, explains the result in plain English, and draws a scatter chart with a best-fit line. Built as a beginner Python project to turn a maths formula into code.

## Features
- Calculates Pearson `r` for two lists of numbers
- Explains the result in words, like "Strong positive relationship"
- Draws a scatter plot with a red best-fit (regression) line using matplotlib
- Checks the input: numbers only, same count in both lists, at least 2 values
- Handles the case where all values in a list are the same
- Runs in a loop until you type `q`
- Includes tests using `assert`

## What the result means
| r value | Meaning |
|---|---|
| Close to 1 | When one goes up, the other goes up |
| Close to -1 | When one goes up, the other goes down |
| Close to 0 | No clear relationship |

| Size of r (ignoring the sign) | Description |
|---|---|
| Below 0.2 | No clear relationship |
| 0.2 to 0.4 | Weak |
| 0.4 to 0.6 | Moderate |
| 0.6 to 0.8 | Strong |
| 0.8 and above | Very strong |

## How it works
1. Find the mean (average) of each list.
2. For each pair, multiply how far `x` is from its mean by how far `y` is from its mean, and add them all up (the top of the formula).
3. Add up the squared distances for `x` and for `y`, multiply them and take the square root (the bottom).
4. `r = top / bottom`

The best-fit line uses `y = slope * x + intercept`, where the slope is the top divided by the sum of the squared `x` distances.

## Requirements
- Python 3.6 or newer
- matplotlib (for the chart)

Install the requirements:
```
python -m pip install -r requirements.txt
```

## How to run
```
python pearson.py
```
Enter the x values and y values separated by commas. Answer `y` to see the chart. Type `q` to quit.

## Example
```
Enter x values separated by commas (or q to quit): 1,2,3,4,5
Enter y values separated by commas: 2,4,5,4,5
Pearson r = 0.7746
Strong positive relationship
Show chart? (y/n): y
```
A window opens with blue data points and a red best-fit line.

| x values | y values | Result |
|---|---|---|
| `1,2,3` | `2,4,6` | r = 1.0000 (very strong positive) |
| `1,2,3` | `6,4,2` | r = -1.0000 (very strong negative) |
| `1,2,3,4,5` | `2,4,5,4,5` | r = 0.7746 (strong positive) |

## Functions
| Function | What it does |
|---|---|
| `mean(numbers)` | Average of a list, or `None` if it is empty |
| `pearson(x, y)` | Returns `r`, or `None` if it cannot be calculated |
| `regression_line(x, y)` | Returns the slope and intercept of the best-fit line |
| `describe(r)` | Turns `r` into a plain-English sentence |
| `parse_numbers(text)` | Turns `"1, 2, 3"` into `[1.0, 2.0, 3.0]`, or `None` if invalid |
| `show_chart(x, y, r)` | Draws the scatter plot and the best-fit line |
| `main()` | Menu loop that asks for input and prints the result |

## Run the tests
```
python test_pearson.py
```
If everything works, it prints `All tests passed`. The tests do not need matplotlib.

## Project structure
```
PearsonRegression/
├── pearson.py          # maths, input checks, chart and command-line menu
├── test_pearson.py     # tests using assert
├── requirements.txt    # libraries needed (matplotlib)
├── .gitignore          # ignores __pycache__ and .vscode
└── README.md
```

## What I learned
- A maths formula can be broken into small steps and turned into code, one function at a time.
- `zip()` lets me loop through two lists at the same time.
- `try / except ValueError` stops the program crashing when someone types text instead of a number, and `math.isfinite` blocks values like `nan` and `inf`.
- Importing matplotlib inside the chart function means the maths and tests still work without it.
- Correlation is not causation: two things can move together without one causing the other.
- A computer can have more than one Python install. The one running my code must be the one where the library is installed, and `python -m pip` installs into the right one.

## Limitations
- Pearson `r` only measures straight-line relationships, so a curved pattern can give a low `r`.
- One extreme value (an outlier) can change `r` a lot.
- Only typed input is supported, with no files yet.

## Ideas for improvement
- Read the numbers from a CSV file
- Save the chart as an image
- Add Spearman correlation for curved relationships