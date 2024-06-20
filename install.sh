echo строим дом
python -m build

echo установка каркаса
cd dist
pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall --break-system-packages
cd ..

echo ты здесь
pip show stupidwalletapi

echo тепер можешь дудосить тгк каналы квадроберов
