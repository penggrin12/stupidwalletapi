echo ставим питухон
apk add python3
apk add py3-pip
echo ставим зависимости
pip3 install build
pip3 instal httpx
echo строим
python3 -m build
cd dist
pip3 install
echo вроде все...

