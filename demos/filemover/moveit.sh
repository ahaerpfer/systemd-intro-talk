#!/bin/bash

cd /var/tmp
for file in `ls ./in`; do
    mv in/${file} /var/tmp/out/${file}.moved
done
