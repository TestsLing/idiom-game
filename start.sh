/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3.8 install -r frontend/requirements.txt
python3 frontend/main.py &
npm i && npm run serve
