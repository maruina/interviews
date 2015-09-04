{% from 'elasticsearch/map.jinja' import elasticsearch with context %}


{% if salt['grains.get']('os_family') == 'Debian' %}

Ensure Elasticsearch Debian repository is configured:
  pkgrepo.managed:
    - humanname: Elasticsearch
    - name: deb http://packages.elastic.co/elasticsearch/1.7/debian stable main
    - file: /etc/apt/sources.list.d/elasticsearch-1.7.list
    - key_url: https://packages.elastic.co/GPG-KEY-elasticsearch

{% endif %}

Ensure Elasticsearch is installed:
  pkg.installed:
    - name: {{ elasticsearch.lookup.package }}