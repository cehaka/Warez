pwd=`pwd`

if [ ! -d ../../VideoNamerDoc ]; then mkdir ../../VideoNamerDoc; fi

cd ../../VideoNamerDoc

git init
git remote add origin https://bigben87@github.com/bigben87/VideoNamer.git &> /dev/null

git fetch origin
git checkout gh-pages

mv source/index.rst source/index.bck
rm -rf source/*.rst
mv source/index.bck source/index.rst
sphinx-apidoc -o source/ $pwd
make html

git symbolic-ref HEAD refs/heads/gh-pages
git add .
git commit -m 'new commit to gh-pages' &> /dev/null
git push origin gh-pages

cd $pwd
