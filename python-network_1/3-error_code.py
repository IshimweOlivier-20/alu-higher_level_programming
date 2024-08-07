#!/usr/bin/python3
"""My Documentation"""
if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resq:
            print(resq.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
