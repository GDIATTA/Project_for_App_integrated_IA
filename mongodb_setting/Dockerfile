FROM mongo:latest

COPY config-replica.js /
COPY .bashrc /data/db/.bashrc
COPY requirements.txt /
RUN mkdir /scratch_space
ADD change_streams /tutorials/change_streams
ADD source_connector /tutorials/source_connector
ADD sink_connector /tutorials/sink_connector
ADD cdc_handler /tutorials/cdc_handler
ADD time_series /tutorials/time_series
ADD utils /usr/local/bin
RUN chmod +x /usr/local/bin/cx
RUN chmod +x /usr/local/bin/del
RUN chmod +x /usr/local/bin/kc
RUN chmod +x /usr/local/bin/status

RUN apt-get -y update
RUN apt-get -y upgrade
#RUN apt-get install -y --no-install-recommends apt-utilsdocker
RUN apt-get install -y curl
RUN apt-get install -y python3-pip python3-venv
RUN apt-get install -y nano
RUN apt-get install -y bsdmainutils
RUN apt-get install -y kafkacat
RUN apt-get install -y git
RUN apt-get install -y dos2unix
RUN git clone https://github.com/RWaltersMA/stockgenmongo.git


RUN dos2unix /usr/local/bin/*
RUN dos2unix /data/db/.bashrc

# --- venv pour éviter PEP 668 ---
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip \
 && pip install -r /requirements.txt \
 && pip install -r /stockgenmongo/requirements.txt