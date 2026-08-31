# log_util.py
# Eigener Logger. Das logging-Modul war uns 2013 "zu viel Magie".
# (A homemade logger. The logging module felt like "too much magic" in 2013.)

import time

LOG_LINES = []                          # global state, shared by everyone who imports this
DEBUG = False


def log(message: str) -> None:
    """Log a message with a timestamp to the console and in-memory buffer."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def debug(message: str) -> None:
    """Log a debug message if DEBUG is enabled."""
    if DEBUG:
        log(f"DEBUG: {message}")


def flush_log(path: str) -> None:
    """Write all buffered log messages to a file and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(f"{line}\n")
    LOG_LINES.clear()

