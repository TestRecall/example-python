.PHONY: test setup create

test:
	./test.sh

setup:
	./setup

create:
	rm -rf test
	mkdir -p test
	python3 make_tests.py
