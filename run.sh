#!/bin/bash
docker run --rm -v $(pwd):/src pyml python3 /src/test.py
