
PYTHONPATH="src/k8s_voca" pytest tests/ \
-c pytest.ini \
--cov-report term:skip-covered \
--cov-report xml:report/coverage/coverage.xml \
--cov=. \
--junitxml=report/test/tests.xml