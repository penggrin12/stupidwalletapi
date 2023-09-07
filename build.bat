@echo off

echo building...
python -m build

echo installing...
cd dist
python -m pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall
cd ..

echo done!
