#!/bin/zsh

while true; do
    clear
    # use this to stop at first failure:
    # pytest -x -vv $subdir
    # pytest test/happy test/bugs
    pytest test
    fswatch ./**/*.py  -1
done
