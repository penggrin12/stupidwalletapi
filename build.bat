@echo off

echo Building...
python -m build

echo Installing...
cd dist
python -m pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall
cd ..

echo Done!
