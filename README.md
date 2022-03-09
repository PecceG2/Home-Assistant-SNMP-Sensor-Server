<br />
<center>
  <a href="https://github.com/PecceG2/StudioLED">
    <img src="https://raw.githubusercontent.com/PecceG2/Home-Assistant-SNMP-Sensor-Server/main/icon.png" alt="Logo" width="80" height="80">
  </a>

<p align="center">
  <h3 align="center">Home Assistant SNMP Sensor Server</h3>


  <img align="center">
    HA Add-on to expose the different sensors, entities and objects via SNMP automatically.</br>
    It provides monitoring of the system, hardware and HA integrations via external monitoring software like LibreNMS or Nagios.
    <br />
    <br />
    <a href="https://github.com/PecceG2/"><strong>View my projects »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PecceG2/Home-Assistant-SNMP-Sensor-Server/issues">Report a Bug</a>
    ·
    <a href="https://github.com/PecceG2/Home-Assistant-SNMP-Sensor-Server/blob/master/LICENSE.md">View License</a>
    ·
    <a href="https://github.com/PecceG2/Home-Assistant-SNMP-Sensor-Server/issues">Request Feature</a>
  </p>
</p>

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

</center>

**Installation**
---

1. In your HA panel, go to `Configuration` -> `Add-ons, Backup & supervisor`.

2. In the lower right corner, click on `Add-on Store` button.

3. Go to the `three dots` on the top right screen and open `Repositories`

4. Copy and paste this link in Add box, and press "Add" button: 
`https://github.com/PecceG2/Home-Assistant-SNMP-Sensor-Server`

5. Close Add-on pop-up, refresh the page with F5 and go to `Configuration` -> `Add-ons, Backup & supervisor`.

6. Find "SNMP Sensor Server" add-on and click them. Now, install it.


**Configuration and usage**
---
Coming soon usage docs


<br />


[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

This is a modification of the original [darthsebulba04 project](https://github.com/darthsebulba04/hassio-snmpd/) under the MIT license to add sensor functionality and HA control via SNMP.