doxygen:
	doxygen
	python DoxyCleaner.py
	rm .git/index
	rm Doxyfile
	rm -rf filmlists/
	rm *.*
	mv html/* .
	git symbolic-ref HEAD refs/heads/gh-pages
	git add .
	git commit -m 'new commit to gh-pages'
	git push origin gh-pages
	git checkout master
