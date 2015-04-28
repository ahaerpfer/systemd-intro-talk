
presentation:
	pdflatex presentation.tex

fullpresentation:
	pdflatex presentation.tex
	#bibtex presentation.aux
	#pdflatex presentation.tex
	pdflatex presentation.tex

handout:
	pdflatex handout.tex

fullhandout:
	pdflatex handout.tex
	#bibtex handout.aux
	#pdflatex handout.tex
	pdflatex handout.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.nav *.out *.snm *.toc *.vrb

all: clean fullpresentation fullhandout
	cp handout.pdf ../pdf/systemd-intro.pdf
