#!/bin/zsh

while true; do
    clear
    # use this to stop at first failure:
    # pytest -x -vv $subdir
    # pytest test/happy test/bugs

    if [ $1 ]; then
        pytest $1
    else
        pytest test
    fi

    fswatch ./**/*.py  -1
done
