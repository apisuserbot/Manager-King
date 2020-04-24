# We're using prebuilt docker images
FROM dasbastard/dirty:latest

#
# Clone repo and prepare working directory
#
RUN git clone 'https://github.com/AnggaR96s/dirtybotx2.git' /root/emilia
RUN mkdir /root/emilia/bin/
WORKDIR /root/emilia/

# Try Upgrade some requirements
# RUN pip3 install -r requirements.txt --upgrade

CMD ["python3","-m","emilia"]
