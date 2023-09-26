echo Setting up...
python -m build

echo Please wait...
cd dist
pip install stupidwalletapi-1.0.0-py3-none-any.whl --force-reinstall --break-system-packages
cd ..

echo Here you go!
pip show stupidwalletapi

echo Now you can DDoS Telegram datacenters!
