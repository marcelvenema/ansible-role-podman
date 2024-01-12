# RedHat Podman

<table border="0">
  <tr>
    <td width="160px" valign="top"><img src="media/icon_semaphore.png" align="left" height="128" width="128" /></td>
    <td>Ansible role voor installatie en configuratie van RedHat Podman<br/> 
        <br/>
        Website van leverancier: `https://podman.io`<br/>
        <br/>
    </td>
  </tr>
</table>

# Diensten:


action: **install**<br/>
Installatie van laatste versie van RedHat Podman. Basis configuratie.<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>

Voorbeeld:
```
- name: Install and configure Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : install
```
<br/>
<br/>


action: **uninstall**<br/>
De-installatie van RedHat Podman.<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>

Voorbeeld:
```
- name: Uninstall Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : uninstall
```
<br/>
<br/>


action: **update**<br/>
Update van RedHat Podman.<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>
<br/>

Voorbeeld:
```
- name: Update Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : update
```
<br/>
<br/>


***

- **changelog**<br/>
  Wijzigingen logboek.<br/>
  Zie [changelog](CHANGELOG.md)<br/>



- **roadmap**<br/>
  Visie en toekomstige ontwikkelingen.<br/>
  Zie [roadmap](ROADMAP.md)<br/>

***

## Voorbereidingen
(geen).<br/>


## Afhankelijkheden
Afhankelijkheden zijn benoemd in het **requirements.yml** bestand. Gebruik `ansible-galaxy install ./requirements.yml --force` voor installatie.<br/>


## Installatie en configuratie
Installatie via action 'install'.<br/>
Voorbeeld voor installatie RedHat Podman:


## Overige informatie
(geen).<br/>


## Licentie
MIT


## Auteur
Marcel Venema
