#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    all_names = dir()
    filtered_names = sorted(name for name in all_names if not name.startswith("__"))

    for name in filtered_names:
        print()
