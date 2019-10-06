#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# cat settings.properties
# [DomainLogging]
# keys=admin access datasource diagnostic domain
# log.admin.path=/Servers/AdminServer/Log/AdminServer
# log.admin.file=/u01/oracle/logs/mta4ru/AdminServer.log
# log.admin.fileMinSize=10000
# log.admin.fileCount=50
# log.admin.rotateLogOnStartup=True
# log.access.path=/Servers/AdminServer/WebServer/AdminServer/WebServerLog/AdminServer
# log.access.file=/u01/oracle/logs/mta4ru/access.log
# log.access.fileMinSize=10000
# log.access.fileCount=50
# log.access.rotateLogOnStartup=True
# log.datasource.path=/Servers/AdminServer/DataSource/AdminServer/DataSourceLogFile/AdminServer
# log.datasource.file=/u01/oracle/logs/mta4ru/datasource.log
# log.datasource.fileMinSize=10000
# log.datasource.fileCount=50
# log.datasource.rotateLogOnStartup=True
# log.diagnostic.path=/Servers/AdminServer/ServerDiagnosticConfig/AdminServer
# log.diagnostic.file=/u01/oracle/logs/mta4ru/diagnostic_images
# log.diagnostic.fileMinSize=null
# log.diagnostic.fileCount=null
# log.diagnostic.rotateLogOnStartup=null
# log.domain.path=/Log/MTA4RU
# log.domain.file=/u01/oracle/logs/mta4ru/base_domain.log
# log.domain.fileMinSize=10000
# log.domain.fileCount=50
# log.domain.rotateLogOnStartup=True

# [DataSources]
# keys=example1 example2
# example1.url=jdbc:oracle:thin:@db.example.com:1521:example1
# example1.user=example
# example1.password=example
# example1.Name=dsExample1
# example1.jndiName=jdbc/dsExample1
# example1.GlobalTransactionsProtocol=EmulateTwoPhaseCommit
# example1.driver=oracle.jdbc.xa.client.OracleXADataSource
# example1.MaxCapacity=50
# example1.ConnectionCreationRetryFrequencySeconds=10
# example1.TestTableName=SQL SELECT 1 FROM DUAL
# example1.XaSetTransactionTimeout=True
# example1.XaTransactionTimeout=7200
# example2.url=jdbc:oracle:thin:@db.example.com:1521:example2
# example2.user=example
# example2.password=example
# example2.Name=dsExample2
# example2.jndiName=jdbc/dsExample2
# example2.GlobalTransactionsProtocol=None
# example2.driver=oracle.jdbc.OracleDriver
# example2.MaxCapacity=50
# example2.ConnectionCreationRetryFrequencySeconds=10
# example2.TestTableName=SQL SELECT 1 FROM DUAL
# example2.XaSetTransactionTimeout=null
# example2.XaTransactionTimeout=null

# [Deployments]
# keys=jaxrs hello1 hello2
# jaxrs.name=jax-rs#2.0@2.22.4.0
# jaxrs.type=Library
# jaxrs.sourcePath=/u01/oracle/wlserver/common/deployable-libraries/jax-rs-2.0.war
# jaxrs.securityDDModel=DDOnly
# hello1.name=hello1
# hello1.type=AppDeployment
# hello1.sourcePath=/u01/oracle/files/hello1.war
# hello1.securityDDModel=DDOnly
# hello2.name=hello2
# hello2.type=AppDeployment
# hello2.sourcePath=/u01/oracle/files/hello2.war
# hello2.securityDDModel=DDOnly


import os
import sys
import json
import configparser


settings_file = 'settings.properties'
section = 'Deployments'
keys='keys'


class ConfigParserClass(object):

    def __init__(self, file_value=None, keys_value=None, section_value=None):
        
        self.file_value = file_value
        self.keys_value = keys_value
        self.section_value = section_value

        self.config = configparser.ConfigParser()

        try:
            # open(self.file_value, 'rb').read(1)
            self.config.read(self.file_value)

        except:
            pass

        self.params = self.__get_param()
        self.sections = self.__get_sections()
        self.keys = self.__get_keys()
        self.settings = self.__get_settings()

    def __get_param(self):

        if str(self.section_value).lower() == 'deployments':
            param_name = 'name'
            param_type = 'type'
            param_source_path = 'sourcePath'
            param_security_dd_model = 'securityDDModel'

            return [
                param_name,
                param_type,
                param_source_path,
                param_security_dd_model
            ]

        elif str(self.section_value).lower()  == 'domainlogging':
            param_path = 'path'
            param_file = 'file'
            param_fileMinSize = 'fileMinSize'
            param_fileCount = 'fileCount'
            param_rotateLogOnStartup = 'rotateLogOnStartup'

            return [
                param_path,
                param_file,
                param_fileMinSize,
                param_fileCount,
                param_rotateLogOnStartup
            ]

        elif str(self.section_value).lower()  == 'datasources':
            param_url = 'url'
            param_user = 'user'
            param_password = 'password'
            param_Name = 'Name'
            param_jndiName = 'jndiName'
            param_GlobalTransactionsProtocol = 'GlobalTransactionsProtocol'
            param_driver = 'driver'
            param_MaxCapacity = 'MaxCapacity'
            param_ConnectionCreationRetryFrequencySeconds = 'ConnectionCreationRetryFrequencySeconds'
            param_TestTableName = 'TestTableName'
            param_XaSetTransactionTimeout = 'XaSetTransactionTimeout'
            param_XaTransactionTimeout = 'XaTransactionTimeout'

            return [
                param_url,
                param_user,
                param_password,
                param_Name,
                param_jndiName,
                param_GlobalTransactionsProtocol,
                param_driver,
                param_MaxCapacity,
                param_ConnectionCreationRetryFrequencySeconds,
                param_TestTableName,
                param_XaSetTransactionTimeout,
                param_XaTransactionTimeout
            ]

        else:
            return None

    def __get_sections(self):

        sections_items = self.config.sections()

        if not sections_items:
            return None

        else:
            return sections_items

    def __get_keys(self):

        if not self.section_value or not self.keys_value:
            return None

        keys = list()

        try:
            keys_get = self.config.get(self.section_value, self.keys_value)

        except:
            return None

        for key in keys_get.split():
            keys.append(key)

        # print(json.dumps(keys, indent=4))
        return keys

    def __get_settings(self):

        if not self.section_value or not self.keys_value or not self.keys or not self.params:
            return None

        settings = dict()

        for key_item in self.keys:

            settings_item = dict()

            for param_item in self.params:

                key_param = key_item + "." + param_item

                if not self.config.has_option(self.section_value, key_param):
                    continue

                key_value = self.config.get(self.section_value, key_param)
                settings_item[param_item] = key_value
            
            settings[key_item] = settings_item.copy()
            settings_item.clear()

        # print(json.dumps(settings, indent=4))
        return settings


def main():

    pars = ConfigParserClass(file_value=settings_file, keys_value=keys, section_value=section)
    print("Params: ", pars.params)
    print("Sections: ", pars.sections)
    print("Keys: ", pars.keys)
    print("Settings: ", pars.settings)


if __name__ == '__main__':

    sys.exit(main())
