#!/bin/zsh

#echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=tests
fi
# echo "-----subdir: ----$subdir"

while true; do
    clear
    # use this to stop at first failure:
    # pytest -x -vv $subdir
    #  pytest -vv -rxX $subdir --impl functional
    echo "--------------------------------------------------------------------------------------------------------------"
    echo "--------------------------------------------------------------------------------------------------------------"
    echo
    echo
    echo "                   $0"
    echo
    echo
    echo "--------------------------------------------------------------------------------------------------------------"
    echo "--------------------------------------------------------------------------------------------------------------"
    pytest $subdir --impl original
    pytest $subdir --impl refactored

    pytest $subdir --impl fun_plain
    pytest $subdir --impl fun_decorators
    pytest $subdir --impl inheritance
    pytest $subdir --impl registry


    fswatch ./**/*.py  -1
done

#-r chars              Show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed, (P)assed with output, (a)ll except passed (p/P), or (A)ll. (w)arnings are enabled by default (see --disable-warnings), 'N' can be used to reset the list. (default: 'fE').
