# Copyright 2023-present, Argilla, Inc.
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

ds_labelled.select_columns(["input", "generations", "rating", "rationale"])[0]
# {
#     "input": "Describe the capital of Spain in 25 words.",
#     "generations": ["Santo Domingo is the capital of Dominican Republic"],
#     "rating": [1.0],
#     "rationale": [
#         "The text is irrelevant to the instruction. It describes the capital of the Dominican Republic instead of Spain."
#     ],
# }
