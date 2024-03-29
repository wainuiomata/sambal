.PHONY : build
build :
	@pip wheel --no-deps --wheel-dir build .

.PHONY : clean
clean :
	rm -rf build/ reports/

.PHONY : lint
lint :
	@ruff check

.PHONY : lint-fix
lint-fix :
	@ruff check --fix

.PHONY : format
format :
	@ruff format

.PHONY : test
test :
	@pytest
