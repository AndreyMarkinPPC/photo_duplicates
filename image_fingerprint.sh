#!/bin/bash
convert $1 -sample 160x160! \
	-colorspace Gray \
	-blur 3x99 \
	"$1_temp.jpg"
