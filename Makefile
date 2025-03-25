#Makefile
install:	# install
	uv sync

brain-games: # start game
	uv run brain-games

build: # build project
	uv build

package-install: #install package
	uv tool install dist/*.whl
lint: # ruff check
	uv run ruff check brain_games