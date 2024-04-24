# IVS Project 2 - Golden Calculator
#
# @brief: Makefile for the project
#
# @author: Murad Mikogaziev (xmikog00)
# @file Makefile
# @date 2024-22-04

ARCHIVE = xpushkm00_xkazna01_xkalut00_xmikog00

all:
	pip install pytest
	pip install tk
	pip install regex

pack:
	mkdir -p ../../$(ARCHIVE)/doc
	mkdir -p ../../$(ARCHIVE)/install
	mkdir -p ../../$(ARCHIVE)/repo
	cp -a ../doc/* ../../$(ARCHIVE)/doc
	cp -a ../setup.exe ../../$(ARCHIVE)/install
	cp -a ../* ../../$(ARCHIVE)/repo
	rm -rf ../../$(ARCHIVE)/repo/doc
	rm -rf ../../$(ARCHIVE)/repo/installer
	cd ../.. && zip -r $(ARCHIVE).zip $(ARCHIVE)

clean:
	rm -rf ../profiling/__pycache__
	rm -rf ../src/__pycache__
	rm -rf ../src/.pytest_cache

test: ../tests/calc_test.py
	pytest ../tests/calc_test.py

doc:
	doxygen Doxyfile

run: app.py
	python3 app.py

profile: profiling.py
	python3 profiling.py