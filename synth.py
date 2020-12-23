# Copyright 2020 Google LLC
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

"""This script is used to synthesize generated parts of this library."""
import os

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Generate Recommendations AI GAPIC layer
# ----------------------------------------------------------------------------
versions = ["v1beta1"]
for version in versions:
    library = gapic.py_library(
        service="recommendationengine",
        version=version,
        bazel_target=f"//google/cloud/recommendationengine/{version}:recommendationengine-{version}-py"
    )

    s.move(library, excludes=["setup.py", "docs/index.rst"])


# rename library to recommendations ai, to be consistent with product branding
s.replace(["google/**/*.py", "tests/**/*.py"], "google-cloud-recommendationengine", "google-cloud-recommendations-ai")

# surround path with * with ``
s.replace("google/**/*.py", '''"(projects/\*/.*)"\.''', "``\g<1>``" )
s.replace("google/**/import_.py", "gs://bucket/directory/\*\.json", "``gs://bucket/directory/*.json``")

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=100, microgenerator=True)
s.move(templated_files, excludes=[".coveragerc"])  # the microgenerator has a good coveragerc file

s.shell.run(["nox", "-s", "blacken"], hide_output=False)