# fortinet_flexvm_api

*This Python Code uses the Fortinet Flex VM API to grab information about VM configurations.  The API is documented on fndn.fortinet.net.  API credentials can be created and downloaded using the below link

  https://docs.fortinet.com/document/forticloud/21.2.0/identity-access-management-iam/282341/adding-an-api-user
  
  You can get your configuration ID using flexvm_config_list.py.  Once you have this, you can populate the configID in flexvm_creat_entitlement.py  The idea here is to completely automate generation of the flexVM entitlement token.  Once you have this, you can use it as part of your FortiGate and/or FortiWeb VM bootstapping process.
