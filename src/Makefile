main : clean build run

run :
	python3 ./app.pyc

build :
	python3 -O -m compileall -b app.py
	chmod +x ./app.pyc

clean :
	rm -f ./app.pyc
