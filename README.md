# Ansible role: RedHat Podman

<table style="border:0px; width:100%"><tr><td width=160px valign=top><img src="media/icon_podman.png" alt="Cockpit icon" width=128 height=128></td>
<td>
Ansible role for installation, configuration, usage and management of RedHat Podman.
Red Hat Podman is an open-source container management tool designed for building, running, and managing containers and container images. It provides a lightweight and daemon-less alternative to Docker, focusing on simplicity, security, and compatibility<br><br>Official website: `https://podman.io`<br><br>
</td>
</tr></table>

Ansible role Podman : [Design](docs/DESIGN.md)  | [Administration](docs/ADMIN.md) | [Examples](examples)  |  [Test](molecule)  |  [Issues]()  |<br><br>
Latest release: <kbd>R1</kbd> - See [RELEASES] for more information.<br>

## Actions summary:

<table style="border:0px; width:100%">
<tr><th><a href="#Deployment">Deployment</a></th><th><a href="#Administration">Administration</a></th><th><a href="#Containers">Containers</a></th><td><a href="#Images">Images</a></th><th><a href="#Volumes">Volumes</th></tr>
<tr>
  <td valign=top>install<br>uninstall<br>update</td>
  <td valign=top>configure<br>start<br>stop<br>configure_vault</td>
  <td valign=top>
    import_container<br>export_container<br>start_container<br>stop_container<br>restart_container<br>update_container<br>run_container_command<br>
  </td>
  <td valign=top>export_image<br>import_image</td>
  <td valign=top>copy_to_volume<br>create_volumes<br>destroy_volumes</td>
</tr></table>

## Default variables:
This role uses the `podman` variable for configuration parameters. See [defaults/main.yml](defaults/main.yml) for a comprehensive list of available options and their descriptions.<br>

# Actions

## Deployment

action: **install**<br>
Install basic version of RedHat Podman. Basic configuration.<br>
variables:<br/>
<kbd>uninstall</kbd> (optional) : true/false, uninstall Podman before installation.<br>
<kbd>data_folder</kbd> (optional) : Local folder to store Podman data, default `/data`.<br>
<kbd>service_user</kbd> (optional) :
<kbd>service_group</kbd> (optional) :

```
- name: Install and configure Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : install
       podman:
         data_folder:  "\data"
         uninstall : true
```

action: **uninstall**<br>
Uninstallation of RedHat Podman.<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```
- name: Uninstall Podman
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : uninstall
       keep_data: true
```

action: **update**<br>
Update RedHat Podman to latest version.<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```
- name: Update Podman to latest version
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : update
```


## Administration

action: **configure**<br>
Configure RedHat Podman.<br>
<kbd>(none)</kbd> : No variables defined.<br>

```
- name: Configure Podman
  hosts: localhost
  roles:
    - role: podman
      vars:
        action: configure
```

action: **start**<br>
Start RedHat Podman service. `ROADMAP`<br>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **stop**<br/>
Stop RedHat Podman service. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>


```

```

action: **configure_vault**<br>
Configure Vault for RedHat Podman.<br>
<kbd>(none)</kbd> : No variables defined.<br>

```
- name: Configure Vault for Podman
  hosts: localhost
  roles:
    - role: podman
      vars:
        action: configure_vault
```


## Containers

action: **import_container**<br>
Start Podman container.<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>
<kbd>container_repository_url</kbd> : URL with location of container repository.<br>
<kbd>container_name</kbd> : <br>
<kbd>container_ports</kbd> : <br>
<kbd>container_volumes</kbd> : <br>
<kbd>container_env</kbd> : <br>

```

```

action: **export_container**<br>
Export Podman container. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **start_container**<br/>
Start Podman container. `ROADMAP`<br>
variables:<br/>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **stop_container**<br>
Stop Podman container. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **restart_container**<br>
Restart Podman container. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **update_container**<br>
Update-upgrade Podman container. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```

```

action: **run_container_command**<br>
run command in Podman container. `ROADMAP`<br>
variables:<br>
<kbd>(none)</kbd> : No variables defined.<br>

```

```



## Images

action: **import_image**<br>
Import Podman image from tarball.<br>
variables:<br>
<kbd>podman_repository_url</kbd> : URL with location of container repository.<br>
<kbd>podman_repository_tag</kbd> (optional) : release or version number of the container image. default is 'latest'.<br>
<kbd>podman_import_folder</kbd> Folder to import images, for example '/tmp/'.<br>

```
- name: Export Podman image
  hosts: localhost
  roles:
   - role: podman
     vars:
       action : import_image
       podman_repository_url: docker.io/hashicorp/vault
       podman_import_folder: /data/import
```


action: **export_image**<br>
Export Podman image to tarball.<br>
variables:<br>
<kbd>podman_repository_url</kbd> : URL with location of container repository.<br>
<kbd>podman_repository_tag</kbd> (optional) : release or version number of the container image. default is 'latest'.<br>
<kbd>podman_export_folder</kbd> Folder to export images, for example '/tmp/'.<br>

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



## Volumes

action: **copy_to_volume**<br>
Copy data to container volume.<br>
<kbd>volume_src</kbd> : No variables defined.<br>
<kbd>volume_dest</kbd> : No variables defined.<br>
<kbd>volume_owner</kbd> : No variables defined.<br>

```
- name: Copy data to Podman volume
  hosts: localhost
  roles:
    - role: podman
      vars:
        action: copy_to_volume

```

action: **create_volumes**<br>
Create container volume.<br>
<kbd>container_volumes</kbd> : No variables defined.<br>

```

```

action: **destroy_volumes**<br>
Create container volume.<br>
<kbd>container_volumes</kbd> : No variables defined.<br>

```

```



























***

- **changelog**<br>
  Change log.
  See [changelog](CHANGELOG.md)

- **roadmap**<br/>
  Vision and future developments.
  See [roadmap](docs/ROADMAP.md)

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
