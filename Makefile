INPUT=library.bib
export

default:
	gcc mendeleyBibFix.c -std=c99 -Wall -o "mendeleyBibFix"

month: default
	python month_text_to_num.py $(INPUT)

clean:
	rm -rf *.bib mendeleyBibFix
