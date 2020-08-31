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
"""miniPages models."""

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    """Model representing a page."""

    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
    )
    content = models.TextField(
        blank=True,
        verbose_name=_('content'),
    )

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('minipages:page-detail', args=[str(self.id)])
