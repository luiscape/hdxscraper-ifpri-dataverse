#!/bin/bash

#
# Run tests with coverage.
#
source venv/bin/activate
nosetests --with-cov \
          --no-byte-compile \
          --nologcapture \
          -v
