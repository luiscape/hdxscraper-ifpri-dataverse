#!/bin/bash

#
# Run tests with coverage.
#
source venv/bin/activate
nosetests --rednose \
          --with-cov \
          --no-byte-compile \
          --nologcapture \
          -v
