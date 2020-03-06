INPUT=library.bib
export

default:
	gcc mendeleyBibFix.c -std=c99 -Wall -o "mendeleyBibFix"

month:
	python month_conversion.py $(INPUT)
