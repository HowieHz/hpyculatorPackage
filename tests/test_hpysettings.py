import os
import random

import pytest

from . import hpysettings

setting_file_path = os.getcwd()

instance_json_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name="json",
    settings_file_format="json",
)

instance_toml_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name="toml",
    settings_file_format="toml",
)

instance_yaml_settings_file = hpysettings.load(
    settings_dir_path=setting_file_path,
    settings_file_name="yaml",
    settings_file_format="yaml",
)

test_text = random.randint(0, 9999)
test_key = str(random.randint(0, 9999)) + str("test_key")
test_value = random.randint(0, 9999)
test_value2 = True
test_value3 = test_text


def test_settings_file():
    for instance_settings_file in (
        instance_yaml_settings_file,
        instance_toml_settings_file,
        instance_json_settings_file,
    ):
        instance_settings_file.add(test_key, test_value)
        assert test_value == instance_settings_file.read(test_key)
        assert {test_key: test_value} == instance_settings_file.readAll()

        instance_settings_file.modify(test_key, test_value2)
        assert test_value2 == instance_settings_file.read(test_key)
        assert {test_key: test_value2} == instance_settings_file.readAll()

        instance_settings_file.delete(test_key)
        instance_settings_file.add(test_key, test_value3)
        assert instance_settings_file.exists(test_key) is True

        assert instance_settings_file.setting_file_path == setting_file_path
