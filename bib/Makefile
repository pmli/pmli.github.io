.PHONY: bibclean FORCE_MAKE

bibclean: $(wildcard *.bib)

%.bib: FORCE_MAKE
	bibclean -max-width 80 $@ > tmp.bib; mv tmp.bib $@
