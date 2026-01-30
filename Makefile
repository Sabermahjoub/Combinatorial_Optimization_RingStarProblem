PY=python3
PKGDIR=.packages

.PHONY: install check run clean

install:
	@mkdir -p $(PKGDIR)
	$(PY) -m pip install --target $(PKGDIR) pulp matplotlib

check:
	PYTHONPATH=$(PKGDIR) $(PY) -c "import pulp, matplotlib; print('OK: pulp et matplotlib OK')"

run:
	PYTHONPATH=$(PKGDIR) $(PY) sae.py

clean:
	rm -rf $(PKGDIR) __pycache__ *.pyc