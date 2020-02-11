FROM ubuntu:bionic

RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
        && echo "Etc/UTC" > /etc/timezone \
        && apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y texlive-full \

RUN apt-get -y install locales
RUN locale-gen && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen 
            
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8    
