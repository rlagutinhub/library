#!/bin/bash

# NAME:   GET.INI.SH
# DESC:   PARS INI FILE
# DATE:   11-10-2019
# LANG:   BASH
# AUTHOR: LAGUTIN R.A.
# EMAIL:  RLAGUTIN@MTA4.RU

# cat settings.ini
# [Base]
# keys=base
# base.domain_name=MTA4RU
# base.admin_name=AdminServer
# base.admin_listen_port=7001
# base.production_mode=prod
# base.administration_port_enabled=true
# base.administration_port=9002
# base.admin_console_enabled=true
# base.derby_enabled=false

# [Security]
# keys=sec
# sec.username=weblogic
# sec.password=welcome1

# [Java]
# keys=java
# java.user_mem_args=-Xms1024m -Xmx1024m -Djava.security.egd=file:/dev/./urandom
# java.java_options=-Dweblogic.configuration.schemaValidationEnabled=false -Dfile.encoding=UTF-8 -Xdebug -Xrunjdwp:transport=dt_socket,address=1044,server=y,suspend=n -Djava.io.tmpdir=/tmp/

FILE="settings.ini"
SECTION="Base"
KEY="PRODUCTION_MODE"

# $1 - $FILE_F
# $2 - $SECTION_F
# $3 - $KEY_F
function get_ini() {

    local FILE_F=$1
    local SECTION_F=$2
    local KEY_F=$3

    if [ ! -r "$FILE_F" ]; then exit 1; fi

    while read SECTION; do

        if [ "$(echo "$SECTION" | sed 's/ *$//g')" == '['$SECTION_F']' ]; then

            SAVEIFS=$IFS; IFS='='

            while read KEY VALUE; do

                if [ "$(echo "$KEY" | sed 's/ *$//g')" == "$KEY_F" ]; then

                    echo $VALUE | sed 's/ *$//g'
                    break

                fi

            done

            IFS=$SAVEIFS

        fi

    done < $FILE_F

}

get_ini $FILE $SECTION $KEY
