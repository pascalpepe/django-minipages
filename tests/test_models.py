# Copyright (C) 2017-2020 Pascal Pepe
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
"""Tests for miniPages models."""

from django.test import TestCase

from minipages.models import Page


class PageModelTest(TestCase):
    """Tests for the page model."""

    @classmethod
    def setUpTestData(cls):
        """Create objects for all tests."""
        cls.page = Page.objects.create(title='Foo', content='bar')

    def test_title_max_length(self):
        max_length = self.page._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_object_string_representation(self):
        self.assertEquals(str(self.page), self.page.title)

    def test_get_absolute_url(self):
        self.assertEquals(self.page.get_absolute_url(), '/pages/1/')
