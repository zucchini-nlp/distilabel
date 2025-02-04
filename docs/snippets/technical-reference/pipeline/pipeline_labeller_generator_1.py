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

import os

from distilabel.llm import InferenceEndpointsLLM, OpenAILLM
from distilabel.pipeline import Pipeline
from distilabel.tasks import TextGenerationTask, UltraFeedbackTask

pipe_full = Pipeline(
    generator=InferenceEndpointsLLM(
        endpoint_name=endpoint_name,
        endpoint_namespace=endpoint_namespace,
        token=token,
        task=TextGenerationTask(
            system_prompt="You are an expert writer of XKCD, a webcomic of romance, sarcasm, math, and language."
        ),
        max_new_tokens=512,
        do_sample=True,
        prompt_format="notus",
    ),
    labeller=OpenAILLM(
        model="gpt-3.5-turbo",
        task=UltraFeedbackTask.for_instruction_following(),
        max_new_tokens=256,
        num_threads=4,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.3,
    ),
)
