#/bin/bash!
source venv/bin/activate
pip3 install -r requirements.txt
/usr/bin/rm -f reports/*
~/.local/bin/behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
~/allure/bin/allure serve reports/ > id 2>&1 &
PID=$!
sleep 5
if [ -s id ]; then
        /usr/bin/cp -rf /tmp/`/usr/bin/grep 'tmp' id | /usr/bin/cut -d '/' -f 3`/allure-report/* /var/lib/jenkins/workspace/testreport/
fi
/usr/bin/kill -9 $PID
/usr/bin/rm id
