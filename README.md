# RedHat Podman

<table border="0">
  <tr>
    <td width="160px" valign="top"><img src="media/icon_podman.png" align="left" height="128" width="128" /></td>
    <td>Ansible role to install, configure and administer RedHat Podman.<br/>
        <br/>
        Supplier website: `https://podman.io`<br/>
        <br/>
    </td>
  </tr>
</table>

# Services:

## Deployment
Deployment actions:<br/>

action: **install**<br/>
Install basic version of RedHat Podman. Basic configuration.<br/>
variables:<br/>
<kbd>uninstall</kbd> (optional) : true/false, uninstallation of Podman before installation.<br/>
<kbd>podman_data_folder</kbd> (optional) : Local folder for storing Podman data, default `/data`.<br/>

Example:
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
Uninstallation of RedHat Podman.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>
<br/>

action: **update**<br/>
Update of RedHat Podman.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>
<br/>

## Configuration
Configuration actions:<br/>

action: **configure**<br/>
Configure RedHat Podman.<br/>
<kbd>(none)</kbd> : No variables needed.<br/>
<br/>

## Management
Management actions:<br/>

action: **start**<br/>
Start RedHat Podman service.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>
<br/>

action: **stop**<br/>
Start RedHat Podman service.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>
<br/>





action: **export_image**<br/>
Export Podman image to tarball.<br/>
variables:<br/>
<kbd>podman_repository_url</kbd> : URL with location of container repository.<br/>
<kbd>podman_repository_tag</kbd> (optional) : release or version number of the container image. default is 'latest'.<br/>
<kbd>podman_export_folder</kbd> Folder for export images, for example '/tmp/'.<br/>

Example:
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
Start container. (IN DEVELOPMENT)<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>

Example:
```
- name: Export Podman image
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : start
```

action: **stop**<br/>
Stop container. (IN DEVELOPMENT)<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables needed.<br/>

Example:
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
  Change log.<br/>
  See [changelog](CHANGELOG.md)<br/>



- **roadmap**<br/>
  Vision and future developments.<br/>
  See [roadmap](ROADMAP.md)<br/>

***

## Preparations
(none).<br/>


## Dependencies
Dependencies are listed in the **requirements.yml** file. Use `ansible-galaxy install -r requirements.yml --force` for installation.<br/>

If this role is used in other playbooks or Ansible projects, the URL of this role should be added to the `requirements.yml` file. Using the above command, the role will be placed in the correct folder structure.<br/>
<br/>


## Installation and configuration
Installation via the action variable <kbd>install</kbd>. (Re-)configuration via the action variable <kbd>configure</kbd>.<br/>

When using this role in other playbooks or Ansible projects:<br/>
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

When used as a stand-alone Ansible project:<br/>
```
- name: Install and configure Podman
  hosts: localhost
  tasks:

    - name: Install Podman
      ansible.builtin.include_tasks:
        file: tasks/install.yml
```
<br/>


## Other information
(none).<br/>

## License
MIT


## Author
Marcel Venema
