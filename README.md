VideoNamer
==========

A python script to rename movies and series.

GitHub Pages Procedure
----------------------

    $ doxygen
    $ rm .git/index
    $ ls
    $ rm Doxyfile
    $ rm -rf filmlists/
    $ rm *.*
    $ mv html/* .
    $ git symbolic-ref HEAD refs/heads/gh-pages
    $ git add .
    $ git commit -m 'new commit to gh-pages'
    $ git push origin gh-pages
    $ git checkout master
