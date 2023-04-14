#!/bin/bash

commands=(ls cp mkdir touch vi)

for cmd in "${commands[@]}"; do
  man -P cat "$cmd" > "$cmd"
done


