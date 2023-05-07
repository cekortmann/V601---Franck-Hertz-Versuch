all: build/v601.pdf

build/v601.pdf: v601.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v601.tex
	lualatex  --output-directory=build v601.tex
	biber build/v601.bcf
	lualatex  --output-directory=build v601.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
