import sys, math

def progressbar(current, total, status = ""):
    bar_length = 60 - len(status)
    done = current / total
    left = 1 - done

    sys.stdout.write(" " * progressbar.last_length + "\r")

    bar = "=" * int(done * bar_length) + "-" * int(left * bar_length)
    text = "[%s] %s%s ... %s" % (bar, round(done * 100, 1), "%", status)
    sys.stdout.write(text + (" " * (progressbar.last_length - len(text))) + "\r")
    sys.stdout.flush()
    progressbar.last_length = len(text)

progressbar.last_length = 0
