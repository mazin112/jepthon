FROM jepthoniq/jepthon:slim-buster

#clonning repo 
RUN git clone https://github.com/jepthoniq/jepthon /root/jepthon
#working directory 
WORKDIR /root/jepthon

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","jepthon"]
