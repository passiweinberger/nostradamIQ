FROM numenta/nupic:latest
ADD . /opt/numenta/catastrophe
WORKDIR /opt/numenta/catastrophe
RUN pip install -r requirements.txt
