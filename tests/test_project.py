# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from polyaxon_schemas.project import ProjectConfig


class TestProjectConfigs(TestCase):
    def test_project_config(self):
        config_dict = {'name': 'test', 'description': '', 'is_public': True}
        config = ProjectConfig.from_dict(config_dict)
        assert config.to_dict() == config_dict
