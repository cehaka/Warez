doc:
	mkdir ../VideoNamerDoc &> /dev/null
	cd ../VideoNamerDoc && git init
	cd ../VideoNamerDoc && git remote add origin git@github.com:bigben87/VideoNamer.git &> /dev/null
	cd ../VideoNamerDoc && git fetch origin
	cd ../VideoNamerDoc && git checkout gh-pages

	cd ../VideoNamerDoc && sphinx-apidoc -o source/ ../VideoNamer
	cd ../VideoNamerDoc && make html

	cd ../VideoNamerDoc && git symbolic-ref HEAD refs/heads/gh-pages
	cd ../VideoNamerDoc && git add .
	cd ../VideoNamerDoc && git commit -m 'new commit to gh-pages' &> /dev/null
	cd ../VideoNamerDoc && git push --force origin gh-pages

clean:
	rm -f *.pyc
