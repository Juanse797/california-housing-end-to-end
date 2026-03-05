.PHONY: data-load

data-load:
	uv run python -m housing.data.load
