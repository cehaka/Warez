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

    #this might fail
	git commit -m 'new commit to gh-pages' &> /dev/null
	git push origin gh-pages
	git checkout master
