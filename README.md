# nagios-plugins-sdc-replication-manager
SDC Replication Manager: A probe to check the functionality of SDC Replication Manager

## Usage

### NAME

```
      replication_manager_check.py - SDC Replication Manager Nagios plugin
```

### SYNOPSIS

```
      replication_manager_check.py  [--help] [--verbose <level>]
                   [--timeout <threshold> ] --hostname <host> [--rpath <rpat>] [--port <port>]
```

      Options:
       --help,-h         : Display this help.
       --verbose,-v      : Same as debug option (0-9) (supports 1 at the moment)
       --rpath, -r       : The path of the replication manager
       --timeout,-t      : Time threshold to wait before timeout (in second).

       --hostname,-H     : The replication service server host <name or IP).
       --port         : The replication service  port.

### OPTIONS

    --help
         Display this help.

    --verbose 
         Same as debug option.

    --timeout
         Time threshold in second to wait before timeout (default to 30).

    --hostname <host>
         The replication service server host. It can be a DNS name or an IP address.

    --port <port>
         The replication service server port (default to 80).


### EXAMPLES
      Using  script:

```
   ./replication_manager_check.py -H www.replication-service.fr -p 443
```

