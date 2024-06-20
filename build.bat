@echo off

echo строим питхон
python -m build

echo устанавливаем фигню
cd dist
python -m pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall
cd ..

echo тепер можеш дудосит
