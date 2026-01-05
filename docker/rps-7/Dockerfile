FROM networkstatic/iperf3

# RUN mount -o remount,rw '/sys/class/net/'
# RUN chmod -R 777 /sys/class/net/
RUN apt-get update
RUN apt-get install dos2unix

COPY enable_rps.sh /usr/local/bin/enable_rps.sh
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN dos2unix /usr/local/bin/enable_rps.sh
RUN dos2unix /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/enable_rps.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
