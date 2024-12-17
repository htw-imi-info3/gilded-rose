#!/bin/bash

 docker run \
    -v $(pwd):/cwd \
    -w /cwd \
    -t bkleinen/pytest \
   pwd ; pytest -vv -rxX test/happy

