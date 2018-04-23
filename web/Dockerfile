FROM centos:7

MAINTAINER ISOBE Kazuhiko <muramasa64 at gmail.com>

RUN curl -L -O https://github.com/zmartzone/mod_auth_openidc/releases/download/v2.3.3/mod_auth_openidc-2.3.3-1.el7.centos.x86_64.rpm; \
    curl -L -O https://github.com/zmartzone/mod_auth_openidc/releases/download/v2.3.0/cjose-0.5.1-1.el7.centos.x86_64.rpm

RUN yum -y install epel-release; \
    yum -y install python-pip httpd mod_wsgi; \
    yum -y install mod_auth_openidc-2.3.3-1.el7.centos.x86_64.rpm cjose-0.5.1-1.el7.centos.x86_64.rpm; \
    yum clean all;

ADD setup/httpd-entrypoint.sh /httpd-entrypoint.sh
RUN chmod -v +x /httpd-entrypoint.sh

COPY setup/vhost-wsgi.conf /etc/httpd/conf.d/vhost-wsgi.conf
RUN sed -ri \
        -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
        -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
        /etc/httpd/conf/httpd.conf

RUN curl -L -o /etc/httpd/conf.d/auth_openidc.conf https://raw.githubusercontent.com/zmartzone/mod_auth_openidc/365149755130b0e67146a64029c34dbf5ecf0983/auth_openidc.conf

EXPOSE 80

COPY setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD code /var/www/html
WORKDIR /var/www/html

CMD ["/httpd-entrypoint.sh"]

