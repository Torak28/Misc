lint:
	importchecker .
	isort .
	black .
	mypy .
	pylint --recursive=y .

clean:
	pyclean -v .
	rm -rf .mypy_cache
	rm -rf .pytest_cache

test:
	pytest -v tests/

pylint_report:
	pylint --recursive=y --reports=y .

