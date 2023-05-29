lint:
	importchecker .
	isort .
	black .
	mypy .
	pylint --recursive=y .

clean:
	pyclean -v .

pylint_report:
	pylint --recursive=y --reports=y .