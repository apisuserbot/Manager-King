# We're using prebuilt docker images
FROM dasbastard/dirty:latest

# Docker
# Clone repo and prepare working directory
# Docker
RUN git clone 'https://github.com/apisuserbot/Manager-King.git' /root/emilia
RUN mkdir /root/emilia/bin/
WORKDIR /root/emilia/

# Try Upgrade some requirements
# RUN pip3 install -r requirements.txt --upgrade

# Finishim
CMD ["python3","-m","emilia"]
