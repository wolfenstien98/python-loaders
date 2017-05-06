import sys

def spinner(status = ""):
    spinner.current += 1
    chars = ['/', '-', '\\', '|']
    i = spinner.current % len(chars)
    sys.stdout.write(chars[i] + status  + "\r")
    sys.stdout.flush()

spinner.current = 0
