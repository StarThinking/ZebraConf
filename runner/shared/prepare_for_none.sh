#!/bin/bash

echo 'none' > reconf_vvmode
echo 'NameNode' > reconf_component
echo 'dfs.data.transfer.client.tcpnodelay' > reconf_parameter
echo '0' > reconf_point
echo '0' > reconf_v1
echo '0' > reconf_v2
