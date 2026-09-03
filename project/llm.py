import os
from openai import AsyncOpenAI
client =    AsyncOpenAI(base_url="https://integrate.api.nvidia.com/v1",
                        api_key = os.getenv("NVIDIA_API_KEY"))
async def generate_llm_response( text : str) -> str :
    response = await client.chat.completions.create(model = "nvidia/nemotron-3-ultra-550b-a55b",
                                                    messages = [{"role": "user",
                                                                 "content": text}])
    return response.choices[0].message.content
