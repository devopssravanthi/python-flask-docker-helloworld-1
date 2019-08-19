#!/usr/bin/env bash
service nginx enable
service nginx start
uwsgi --ini uwsgi.ini