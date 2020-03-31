# We're using prebuilt docker images
FROM dasbastard/jnckdclxvi:latest

#
# Clone repo and prepare working directory
#
RUN git clone https://github.com/bagus02/dirtybotx2.git /root/emilia
RUN mkdir /root/emilia/bin/
WORKDIR /root/emilia/
RUN pip3 install tswift
RUN pip3 install gTTS
RUN pip3 install pynewtonmath

CMD ["python3","-m","emilia"]
