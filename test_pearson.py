from pearson import mean, pearson, parse_numbers, describe

assert mean([1, 2, 3]) == 2
assert mean([]) is None

assert round(pearson([1, 2, 3], [2, 4, 6]), 4) == 1.0
assert round(pearson([1, 2, 3], [6, 4, 2]), 4) == -1.0
assert round(pearson([1, 2, 3, 4, 5], [2, 4, 5, 4, 5]), 4) == 0.7746
assert pearson([1, 1, 1], [1, 2, 3]) is None
assert pearson([1, 2], [1]) is None

assert parse_numbers("1, 2, 3.5") == [1.0, 2.0, 3.5]
assert parse_numbers("1, a") is None
assert parse_numbers("") is None

assert describe(0.95) == "Very strong positive relationship"
assert describe(-0.5) == "Moderate negative relationship"
assert describe(0.05) == "No clear relationship"

print("All tests passed")