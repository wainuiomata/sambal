.PHONY : build
build :
	@pip wheel --no-deps --wheel-dir build .

.PHONY : lint
lint :
	@ruff check

.PHONY : test
test :
	@pytest
