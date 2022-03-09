# Home Assistant Add-on: SNMP server

## Installation

From the supervisor add-on store, add the following repository:

https://github.com/darthsebulba04/hassio-addons

Then, in the new list of add-ons, install `SNMP Server`

## How to use

1. Set the `community` option, eg, `public`.  Fill in the other options if you wish.
2. Set the port under network, eg, `161`.
3. Save the add-on configuration by clicking the "SAVE" button.
4. Start the add-on.

## Configuration

The SNMP server add-on can be changed to your likings. This section
describes each of the add-on configuration options.

Example add-on configuration:

```yaml
community: public
location: Home
name: RPi
email: rpi@me.com
```

### Option: `community`

The community your SNMP monitor is looking for, eg `public`

### Option `location`

The SNMP location, eg `Home`

### Option `name`

The SNMP contact name, eg `RPi`

### Email `email`

The SNMP contact email address, eg `rpi@me.com`

## Support

In case you've found a bug, please [open an issue on my GitHub][issue].

[issue]: https://github.com/darthsebulba04/hassio-snmpd/issues
[repository]: https://github.com/darthsebulba04/hassio-snmpd/
