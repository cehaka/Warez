html:
	sphinx-build -b html source/ build/

	git symbolic-ref HEAD refs/heads/gh-pages
	git add .
	git commit -m 'new commit to gh-pages' &> /dev/null
	git push origin gh-pages
