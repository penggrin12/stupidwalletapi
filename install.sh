echo ставим модуль
python -m build

echo щас ставится уже жди залупа
cd dist
pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall
cd ..

echo вроде все, чекай
pip show stupidwalletapi
