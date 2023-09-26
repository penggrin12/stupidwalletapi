echo Installing latest Python...
apk add python3
apk add py3-pip
echo Installing dependencies...
pip3 install build
pip3 instal httpx
echo Building...
python3 -m build
cd dist
pip3 install
echo Done! Now you can DDoS Telegram datacenters!

