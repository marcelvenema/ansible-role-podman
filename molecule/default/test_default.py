def test_podman_installed(host):
    podman = host.package("podman")
    assert podman.is_installed