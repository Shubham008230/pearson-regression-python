import math


def mean(numbers):
    """Average of a list, or None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def pearson(x, y):
    """Return the Person correlation r (-1 to 1), or None if it can't be calculated."""
    if len(x) != len(y) or len(x) <2:
        return None
    mx = mean(x)
    my = mean(y)
    top = 0
    sum_x2 =0
    sum_y2 =0
    for a, b in zip(x, y):                      # go through the pairs together
        top += (a - mx) * (b - my)
        sum_x2 += (a - mx) ** 2
        sum_y2 += (b - my) ** 2
    bottom = math.sqrt(sum_x2 * sum_y2)
    if bottom == 0:                             # all x (or all y) are the same
        return None
    return top / bottom


def regression(x, y):
    """Return (slope, intercept) of the best-fit line, or None."""
    mx = mean(x)
    my = mean(y)
    top = 0
    bottom = 0
    for a, b in zip(x, y):
        top += (a - mx) * (b - my)
        bottom += (a - mx) ** 2
    if bottom == 0:
        return None
    slope = top / bottom
    return slope, my - slope * mx

def describe(r):
    """Turn r into a plain-English sentence."""
    size = abs(r)
    if size < 0.2:
        return "No clear relationship"
    if size < 0.4:
        word = "Weak"
    elif size < 0.6:
        word = "Moderate"
    elif size < 0.8:
        word = "Strong"
    else:
        word = "Very strong"
    direction = "positive" if r > 0 else "negative"
    return f"{word} {direction} relationship"

def parse_numbers(text):
    """Turn '1, 2, 3.5' into [1.0, 2.0, 3.5]. Return None if anything is not a number."""
    numbers = []
    for  part in text.split(","):
        try:
            value = float(part)
        except ValueError:    
            return None
        if not math.isfinite(value):            # blocks 'nan' and 'inf'
            return None
        numbers.append(value)
    return numbers

def show_chart(x, y, r):
    """Draw a scatter plot with the best-fit line."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("The chart needs matplotlib. Install it with: pip install matplotlib")
        return

    plt.scatter(x, y, label="Data points")
    line = regression(x, y)
    if line is not None:
        slope, intercept = line
        x_min, x_max = min(x), max(x)
        plt.plot(
            [x_min, x_max],
            [slope * x_min + intercept, slope * x_max + intercept],
            color="red",
            label="Best-fit line",
        )
    plt.title(f"Pearson r = {r:.3f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        text_x = input("Enter x values separated by commas (or q to quit): ").strip()
        if text_x.lower() == "q":
            break
        text_y = input("Enter y values separated by commas: ").strip()
        x = parse_numbers(text_x)
        y = parse_numbers(text_y)
        if x is None or y is None:
            print("Error: enter number only, separated by commas.")
            continue
        if len(x) != len(y) or len(x) < 2:
            print("Error: x and y need the same count, with at least 2 values each.")
            continue
        r = pearson(x, y)
        if r is None:
            print("Cannot calculate: all x values (or all y values) are the same.")
            continue
        print(f"Pearson r = {r:.4f}")
        print(describe(r))
        if input("Show chart? (y/n): ").lower() == "y":
            show_chart(x, y, r)


if __name__ == "__main__":
    main()