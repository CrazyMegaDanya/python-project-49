#Makefile
istall:	# install
	uv sync

brain-games: # start game
	uv run brain-games

build: # build project
	uv build

package-install: #install package
	uv tool install dist/*.whl