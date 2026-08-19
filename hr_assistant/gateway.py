"""  Step 6b: Route the LLM through Portkey
Portkey stores the real Groq credentials behind a slug (setup once in the portkey dashboard)
Our code never sees the raw Groq key. If the primary slug/models fails, Portkey automatically retries request 
against the fallback target below.
"""

import json
from langchain_openai import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

from hr_assistant import config
from hr_assistant.logger import get_logger

logger= get_logger(__name__)

## REPLACED FROM PORTKEY DASHBOARD CONFIG DUE TO CONFIG_ENABLE:TRUE AND CANNOT BE UNSET FOR PUBLIC
#primary model
# PRIMARY_TARGET = {"provider": "@hrpolicy", "override_parms":{"model": config.LLM_MODEL_NAME}}
#fallbackup model
# FALLBACK_TARGET = {"provider": "@hrpolicybackup", "override_parms":{"model": "openai/gpt-oss-20b"}}

# Public Config set of rules(otherwise can be set in portkey dashboard-configs)
# GATEWAY_CONFIG= {
#     "strategy" :{
#         "mode": "fallback"
#     },
#     "targets":[PRIMARY_TARGET, FALLBACK_TARGET],
# }

#Access Gateway
def get_gateway_llm() -> ChatOpenAI:
    """ Returns a chat model routed throguh Portkey, with automatic fallback"""
    logger.info("Routing LLM through Portkey")
    headers= createHeaders(
        api_key= config.PORTKEY_API_KEY,
        config= config.PORTKEY_CONFIG_NAME
    )
    return ChatOpenAI(
        api_key="portkey",
        base_url=PORTKEY_GATEWAY_URL,
        default_headers=headers
    )

