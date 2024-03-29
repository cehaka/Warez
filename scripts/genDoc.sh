temp=`pwd`
pwd=${temp%/scripts}

if [ ! -d $pwd/../VideoNamerDoc ]; then mkdir $pwd/../VideoNamerDoc; fi

if [ -n `echo PYTHONPATH` ]; then PYTHONPATH=$pwd/; export PYTHONPATH; fi

cd $pwd/../VideoNamerDoc

git init
git remote add origin git@github.com:bigben87/VideoNamer.git &> /dev/null

git pull origin gh-pages

mv source/index.rst source/index.bck
rm -rf source/*.rst
mv source/index.bck source/index.rst

sphinx-apidoc -o source/ $pwd/
make html

git symbolic-ref HEAD refs/heads/gh-pages
git add .
git commit -m 'new commit to gh-pages' &> /dev/null

git push origin gh-pages

cd $pwd/
