FROM ubuntu:16.04


RUN apt-get update -y && apt-get install -y \
	git \
	wget \
    software-properties-common \
    curl \
    apt-transport-https \
    python3-pip \
	supervisor




# install indy sdk - libindy
# options: master, rc, stable
ARG channel="master" 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 68DB5E88
RUN add-apt-repository "deb https://repo.sovrin.org/sdk/deb xenial $channel"
RUN apt-get update
RUN apt-get install -y libindy


RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install -y python3.6



# install indy sdk wrapper
RUN python3.6 -m pip install python3-indy==1.6.7


# just to keep a process alive. Remove later
CMD /bin/bash -c "while true; do sleep 1000; done" &

