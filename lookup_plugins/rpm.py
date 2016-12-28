# -*- coding: utf-8 -*-

# Copyright 2016 Martin Bukatovič <martin.bukatovic@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import subprocess

from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        results = []
        for package_name in terms:
            try:
                package_nevra = subprocess.check_output(
                    ['rpm', '-q', package_name])
                package_nevra = package_nevra.rstrip('\n')
            except subprocess.CalledProcessError:
                package_nevra = ""
            results.append(package_nevra)
        return results
