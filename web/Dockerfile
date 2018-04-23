FROM centos:7

MAINTAINER ISOBE Kazuhiko <muramasa64 at gmail.com>

RUN yum -y install epel-release; \
    yum -y install python-pip httpd mod_wsgi; \
    yum clean all;

ADD setup/run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

COPY setup/vhost-wsgi.conf /etc/httpd/conf.d/vhost-wsgi.conf
RUN sed -ri \
        -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
        -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
        /etc/httpd/conf/httpd.conf

EXPOSE 80

COPY setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD code /var/www/html
WORKDIR /var/www/html

CMD ["/httpd-entrypoint.sh"]

