from os import path


def test_assert_pillar_top_file_exists():
    pillar_top_path = '/srv/pillar/top.sls'
    assert path.exists(pillar_top_path)

    with open(pillar_top_path, 'r') as f:
        contents = f.read()

    assert 'my_test' in contents


def test_can_run_salt_client():
    import salt.config
    import salt.loader

    __opts__ = salt.config.minion_config('/etc/salt/minion')
    __grains__ = salt.loader.grains(__opts__)
    __opts__['grains'] = __grains__
    __salt__ = salt.loader.minion_mods(__opts__)
    assert __salt__['test.ping']()
