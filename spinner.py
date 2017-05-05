import sys

def spinner():
    spinner.current += 1
    chars = ['/', '-', '\\', '|']
    i = spinner.current % len(chars)
    sys.stdout.write(chars[i] + "\r")
    sys.stdout.flush()

spinner.current = 0
