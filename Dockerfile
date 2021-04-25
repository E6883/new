# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b master https://github.com/E6883/new /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/E6883/new/master/requirements.txt

CMD ["python3","-m","userbot"]
