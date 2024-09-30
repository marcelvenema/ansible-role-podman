# RedHat Podman

<table border="0">
  <tr>
    <td width="160px" valign="top"><img src="media/icon_podman.png" align="left" height="128" width="128" /></td>
    <td>Ansible role voor installatie en configuratie van RedHat Podman<br/>
        <br/>
        Website van leverancier: `https://podman.io`<br/>
        <br/>
    </td>
  </tr>
</table>

# Diensten:

## Deployment
Acties voor deployment.<br/>

action: **install**<br/>
Installatie van laatste versie van RedHat Podman. Basis configuratie.<br/>
variables:<br/>
<kbd>uninstall</kbd> (optioneel) : true/false, de-installatie voordat installatie plaatsvindt.<br/>
<kbd>podman_data_folder</kbd> (optioneel) : Lokale folder voor opslag Podman data, standaard `/data`.<br/>

Voorbeeld:
```
- name: Install and configure Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : install
       uninstall : true
```
<br/>

action: **uninstall**<br/>
De-installatie van RedHat Podman.<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>

Voorbeeld:
```
- name: Uninstall Podman
  hosts: localhost
  become: true
  roles:
   - role: podman
     vars:
       action : uninstall
```
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

## Configuratie
Acties voor configuratie.<br/>

**Geen actions gedefinieerd.**

## Beheer
Acties voor beheer.<br/>

action: **export_image**<br/>
Export Podman image naar tarball.<br/>
variables:<br/>
<kbd>podman_repository_url</kbd> : URL met locatie van container repository.<br/>
<kbd>podman_repository_tag</kbd> (optioneel) : release of versienummer van het container image. standaard is 'latest'.<br/>
<kbd>podman_export_folder</kbd> Folder voor export images, bijvoorbeeld '/tmp/'.<br/>

Voorbeeld:
```
- name: Export Podman image
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : export_image
       podman_repository_url: docker.io/hashicorp/vault
       podman_export_folder: /data/export
```

action: **start**<br/>
Start container. (IN ONTWIKKELING)<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>

Voorbeeld:
```
- name: Export Podman image
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : start
```

action: **stop**<br/>
Stop container. (IN ONTWIKKELING)<br/>
variables:<br/>
<kbd>(geen)</kbd> : Geen variablen benodigd.<br/>

Voorbeeld:
```
- name: Export Podman image
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : stop
```


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
Afhankelijkheden zijn benoemd in het **requirements.yml** bestand. Gebruik `ansible-galaxy install -r requirements.yml --force` voor installatie.<br/>

Indien deze role in andere playbooks of Ansible projecten wordt gebruikt, dient de URL van deze rol te worden toegevoegd aan het `requirements.yml` bestand. Via bovenstaand command wordt de rol dan in de juiste folderstructuur geplaatst.<br/>
<br/>


## Installatie en configuratie
Installatie via de action variabele <kbd>install</kbd>. (Her-)configuratie via de action variabele <kbd>configure</kbd>.<br/>

Bij gebruik van deze rol in andere playbooks of Ansible projecten:<br/>
```
- name: Install and configure Podman
  hosts: localhost
  become: true
  roles:
   - role: podman
     vars:
       action : install
```
<br/>

Bij gebruik als stand-alone Ansible project:<br/>
```
- name: Install and configure Podman
  hosts: localhost
  tasks:

    - name: Install Podman
      ansible.builtin.include_tasks:
        file: tasks/install.yml
```
<br/>


## Overige informatie
(geen).<br/>


## Licentie
MIT


## Auteur
Marcel Venema
