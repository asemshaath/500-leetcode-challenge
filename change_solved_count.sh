#!/bin/bash

NUM_LINES=$(ls -l $1 | wc -l)
echo "Number of solved leetcode problems: $NUM_LINES"

sed -i "s/Problems solved:.*/Problems solved: $NUM_LINES/" README.md
