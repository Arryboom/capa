# Copyright (C) 2020 FireEye, Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
# You may obtain a copy of the License at: [package root]/LICENSE.txt
# Unless required by applicable law or agreed to in writing, software distributed under the License
#  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


from fixtures import *


@lru_cache
def get_lancelot_extractor(path):
    import capa.features.extractors.lancelot

    with open(path, "rb") as f:
        buf = f.read()

    return capa.features.extractors.lancelot.LancelotFeatureExtractor(buf)


@parametrize(
    "sample,scope,feature,expected", FEATURE_PRESENCE_TESTS, indirect=["sample", "scope"],
)
def test_lancelot_features(sample, scope, feature, expected):
    do_test_feature_presence(get_lancelot_extractor, sample, scope, feature, expected)


@parametrize(
    "sample,scope,feature,expected", FEATURE_COUNT_TESTS, indirect=["sample", "scope"],
)
def test_lancelot_feature_counts(sample, scope, feature, expected):
    do_test_feature_count(get_lancelot_extractor, sample, scope, feature, expected)
