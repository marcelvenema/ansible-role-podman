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

# Actions:

action: **configure**<br/>
Configure RedHat Podman.<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **copy_to_volume**<br/>
Copy data to container volume.<br/>
<kbd>volume_src</kbd> : No variables defined.<br/>
<kbd>volume_dest</kbd> : No variables defined.<br/>
<kbd>volume_owner</kbd> : No variables defined.<br/>
<br/>

action: **create_volumes**<br/>
Create container volume.<br/>
<kbd>container_volumes</kbd> : No variables defined.<br/>
<br/>

action: **destroy_volumes**<br/>
Create container volume.<br/>
<kbd>container_volumes</kbd> : No variables defined.<br/>
<br/>

action: **export_container**<br/>
Export Podman container. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **export_image**<br/>
Export Podman image to tarball.<br/>
variables:<br/>
<kbd>podman_repository_url</kbd> : URL with location of container repository.<br/>
<kbd>podman_repository_tag</kbd> (optional) : release or version number of the container image. default is 'latest'.<br/>
<kbd>podman_export_folder</kbd> Folder to export images, for example '/tmp/'.<br/>

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

action: **import_container**<br/>
Start Podman container.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<kbd>container_repository_url</kbd> : URL with location of container repository.<br/>
<kbd>container_name</kbd> : <br/>
<kbd>container_ports</kbd> : <br/>
<kbd>container_volumes</kbd> : <br/>
<kbd>container_env</kbd> : <br/>

action: **install**<br/>
Install basic version of RedHat Podman. Basic configuration.<br/>
variables:<br/>
<kbd>uninstall</kbd> (optional) : true/false, uninstall Podman before installation.<br/>
<kbd>podman_data_folder</kbd> (optional) : Local folder to store Podman data, default `/data`.<br/>

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

action: **start**<br/>
Start RedHat Podman service. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **start_container**<br/>
Start Podman container. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **stop**<br/>
Stop RedHat Podman service. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **stop_container**<br/>
Stop Podman container. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>
<br/>

action: **uninstall**<br/>
Uninstallation of RedHat Podman.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>

action: **update**<br/>
Update of RedHat Podman to latest version.<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>

action: **update_container**<br/>
Update-upgrade Podman container. `NOT (YET) IMPLEMENTED`<br/>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br/>


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
Installation via the action variable <kbd>install</kbd>. Configuration via the action variable <kbd>configure</kbd>.<br/>

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
