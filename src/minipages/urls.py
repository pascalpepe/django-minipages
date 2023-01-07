# Copyright 2017-2023 Pascal Pepe
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
"""URL configuration for MiniPages."""

from django.urls import path

from minipages import views

app_name = "minipages"

urlpatterns = [
    path("<int:pk>/", views.PageDetail.as_view(), name="page-detail"),
    path("", views.PageList.as_view(), name="page-list"),
]
