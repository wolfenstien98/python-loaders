import sys

def indetermineate_progressbar():
    indetermineate_progressbar.current += 1;
    bar_length = 60;

    i = indetermineate_progressbar.current % bar_length

    start = i
    end = bar_length - i - 1
''
    bar = "[" + "." * start + " " * end + "]\r"

    sys.stdout.write(bar)
    sys.stdout.flush()


indetermineate_progressbar.current = 0;
