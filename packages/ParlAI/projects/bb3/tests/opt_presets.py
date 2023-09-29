#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


INIT_OPT = {
    'sdm_inference': 'greedy',
    'sdm_beam_min_length': 1,
    'sdm_beam_max_length': 10,
    'sdm_generation_take_last_newline': False,
    'sdm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'sdm_history_size': 1,
    'sdm_module': 'sdm',
    'sdm_max_prompt_len': 1912,
    'sdm_penalize_repetitions': False,
    'sdm_penalize_ctxt_repetitions': False,
    'sdm_exclude_knowledge_from_ctxt_penalty': False,
    'search_decision': 'compute',
    'search_decision_control_token': '',
    'search_decision_do_search_reply': 'search',
    'search_decision_dont_search_reply': 'do not search',
    'sdm_server': 'opt_server',
    'mdm_inference': 'greedy',
    'mdm_beam_min_length': 1,
    'mdm_beam_max_length': 10,
    'mdm_generation_take_last_newline': False,
    'mdm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mdm_history_size': '-1',
    'mdm_module': 'mdm',
    'mdm_max_prompt_len': 1912,
    'mdm_penalize_repetitions': False,
    'mdm_penalize_ctxt_repetitions': False,
    'mdm_exclude_knowledge_from_ctxt_penalty': False,
    'memory_decision': 'compute',
    'memory_decision_control_token': '',
    'memory_decision_do_access_reply': 'access memory',
    'memory_decision_dont_access_reply': 'do not access memory',
    'memory_decision_use_memories': True,
    'mdm_server': 'opt_server',
    'search_query_control_token': '',
    'search_server': 'default',
    'sgm_generation_take_last_newline': False,
    'sgm_inference': 'greedy',
    'sgm_beam_min_length': 1,
    'sgm_beam_max_length': 32,
    'sgm_module': 'sgm',
    'sgm_max_prompt_len': 1912,
    'sgm_exclude_knowledge_from_ctxt_penalty': False,
    'sgm_penalize_repetitions': False,
    'sgm_penalize_ctxt_repetitions': False,
    'sgm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'sgm_server': 'opt_server',
    'memory_generator_control_token': '',
    'mgm_inference': 'greedy',
    'mgm_beam_min_length': 1,
    'mgm_beam_max_length': 32,
    'mgm_generation_take_last_newline': False,
    'mgm_module': 'mgm',
    'mgm_max_prompt_len': 1912,
    'mgm_exclude_knowledge_from_ctxt_penalty': False,
    'mgm_penalize_repetitions': False,
    'mgm_penalize_ctxt_repetitions': False,
    'mgm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mgm_server': 'opt_server',
    'memory_knowledge_control_token': '',
    'mkm_inference': 'greedy',
    'mkm_beam_min_length': 1,
    'mkm_beam_max_length': 32,
    'mkm_generation_take_last_newline': False,
    'mkm_module': 'mkm',
    'mkm_max_prompt_len': 1412,
    'mkm_exclude_knowledge_from_ctxt_penalty': False,
    'mkm_penalize_ctxt_repetitions': False,
    'mkm_penalize_repetitions': True,
    'mkm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mkm_server': 'opt_server',
    'contextual_knowledge_control_token': '',
    'contextual_knowledge_decision': 'compute',
    'ckm_inference': 'greedy',
    'ckm_beam_min_length': 1,
    'ckm_beam_max_length': 32,
    'ckm_module': 'ckm',
    'ckm_max_prompt_len': 1812,
    'ckm_generation_take_last_newline': False,
    'ckm_exclude_knowledge_from_ctxt_penalty': False,
    'ckm_penalize_ctxt_repetitions': False,
    'ckm_penalize_repetitions': True,
    'ckm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'ckm_server': 'opt_server',
    'search_knowledge_control_token': '',
    'skm_inference': 'greedy',
    'skm_beam_min_length': 1,
    'skm_beam_max_length': 64,
    'skm_module': 'skm',
    'skm_max_prompt_len': 1412,
    'skm_generation_take_last_newline': False,
    'skm_penalize_ctxt_repetitions': False,
    'skm_penalize_repetitions': True,
    'skm_exclude_knowledge_from_ctxt_penalty': False,
    'skm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'skm_server': 'opt_server',
    'srm_inference': 'factual_nucleus',
    'srm_beam_min_length': 20,
    'srm_beam_max_length': 128,
    'srm_beam_size': 1,
    'srm_generation_take_last_newline': False,
    'srm_penalize_ctxt_repetitions': True,
    'srm_penalize_repetitions': True,
    'srm_exclude_knowledge_from_ctxt_penalty': True,
    'srm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'srm_module': 'srm',
    'srm_max_prompt_len': 1784,
    'srm_server': 'opt_server',
    'crm_inference': 'factual_nucleus',
    'crm_beam_min_length': 20,
    'crm_beam_max_length': 128,
    'crm_beam_size': 1,
    'crm_generation_take_last_newline': False,
    'crm_module': 'crm',
    'crm_max_prompt_len': 1880,
    'crm_penalize_ctxt_repetitions': False,
    'crm_penalize_repetitions': True,
    'crm_exclude_knowledge_from_ctxt_penalty': True,
    'crm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'crm_server': 'opt_server',
    'mrm_inference': 'factual_nucleus',
    'mrm_beam_min_length': 20,
    'mrm_beam_max_length': 128,
    'mrm_beam_size': 1,
    'mrm_module': 'mrm',
    'mrm_max_prompt_len': 1848,
    'mrm_generation_take_last_newline': False,
    'mrm_penalize_ctxt_repetitions': False,
    'mrm_penalize_repetitions': True,
    'mrm_exclude_knowledge_from_ctxt_penalty': True,
    'mrm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'mrm_server': 'opt_server',
    'vrm_inference': 'factual_nucleus',
    'vrm_beam_min_length': 20,
    'vrm_beam_max_length': 128,
    'vrm_beam_size': 1,
    'vrm_module': 'vrm',
    'vrm_max_prompt_len': 1912,
    'vrm_generation_take_last_newline': False,
    'vrm_penalize_ctxt_repetitions': False,
    'vrm_penalize_repetitions': True,
    'vrm_exclude_knowledge_from_ctxt_penalty': False,
    'vrm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'vrm_server': 'opt_server',
    'grm_inference': 'factual_nucleus',
    'grm_beam_min_length': 20,
    'grm_beam_max_length': 128,
    'grm_beam_size': 1,
    'grm_module': 'grm',
    'grm_max_prompt_len': 1880,
    'grm_generation_take_last_newline': False,
    'grm_penalize_ctxt_repetitions': False,
    'grm_penalize_repetitions': True,
    'grm_exclude_knowledge_from_ctxt_penalty': False,
    'grm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'grm_server': 'opt_server',
    'orm_inference': 'factual_nucleus',
    'orm_beam_min_length': 1,
    'orm_beam_max_length': 128,
    'orm_beam_size': 1,
    'orm_module': 'orm',
    'orm_max_prompt_len': 1412,
    'orm_generation_take_last_newline': False,
    'orm_penalize_ctxt_repetitions': False,
    'orm_penalize_repetitions': False,
    'orm_exclude_knowledge_from_ctxt_penalty': False,
    'orm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'orm_server': 'opt_server',
    'brm_inference': 'factual_nucleus',
    'brm_beam_min_length': 1,
    'brm_beam_max_length': 128,
    'brm_beam_size': 1,
    'brm_module': 'orm',
    'brm_max_prompt_len': 1412,
    'brm_generation_take_last_newline': False,
    'brm_penalize_ctxt_repetitions': False,
    'brm_penalize_repetitions': False,
    'brm_exclude_knowledge_from_ctxt_penalty': False,
    'brm_model': 'projects.bb3.agents.opt_api_agent:BB3OPTAgent',
    'brm_server': 'opt_server',
    "sdm_stop_token": "\n",
    "mdm_stop_token": "\n",
    "sgm_stop_token": "\n",
    "mgm_stop_token": "\n",
    "mkm_stop_token": "\n",
    "ckm_stop_token": "\n",
    "skm_stop_token": "\n",
    "srm_stop_token": "\n",
    "crm_stop_token": "\n",
    "mrm_stop_token": "\n",
    "vrm_stop_token": "\n",
    "grm_stop_token": "\n",
    "orm_stop_token": "\n",
    "brm_stop_token": "\n",
    "sdm_self_prefix": "Person 2",
    "mdm_self_prefix": "Person 2",
    "sgm_self_prefix": "Person 2",
    "mgm_self_prefix": "Person 2",
    "mkm_self_prefix": "Person 2",
    "ckm_self_prefix": "Person 2",
    "skm_self_prefix": "Person 2",
    "srm_self_prefix": "Person 2",
    "crm_self_prefix": "Person 2",
    "mrm_self_prefix": "Person 2",
    "vrm_self_prefix": "Person 2",
    "grm_self_prefix": "Person 2",
    "orm_self_prefix": "Person 2",
    "brm_self_prefix": "Person 2",
    "sdm_final_prefix": None,
    "mdm_final_prefix": None,
    "sgm_final_prefix": None,
    "mgm_final_prefix": None,
    "mkm_final_prefix": None,
    "ckm_final_prefix": None,
    "skm_final_prefix": None,
    "srm_final_prefix": "Person 2",
    "crm_final_prefix": "Person 2",
    "mrm_final_prefix": "Person 2",
    "vrm_final_prefix": "Person 2",
    "grm_final_prefix": "Person 2",
    "orm_final_prefix": "Opening",
    "brm_final_prefix": "AI",
    "sdm_final_prefix_space": False,
    "mdm_final_prefix_space": False,
    "sgm_final_prefix_space": False,
    "mgm_final_prefix_space": False,
    "mkm_final_prefix_space": False,
    "ckm_final_prefix_space": False,
    "skm_final_prefix_space": False,
    "srm_final_prefix_space": False,
    "crm_final_prefix_space": False,
    "mrm_final_prefix_space": False,
    "vrm_final_prefix_space": False,
    "grm_final_prefix_space": False,
    "orm_final_prefix_space": False,
    "brm_final_prefix_space": False,
    "sdm_partner_prefix": "Partner",
    "mdm_partner_prefix": "Partner",
    "sgm_partner_prefix": "Partner",
    "mgm_partner_prefix": "Partner",
    "mkm_partner_prefix": "Partner",
    "ckm_partner_prefix": "Partner",
    "skm_partner_prefix": "Partner",
    "srm_partner_prefix": "Partner",
    "crm_partner_prefix": "Partner",
    "mrm_partner_prefix": "Partner",
    "vrm_partner_prefix": "Partner",
    "grm_partner_prefix": "Partner",
    "orm_partner_prefix": "Partner",
    "brm_partner_prefix": "Partner",
    "sdm_generation_allow_newline": False,
    "mdm_generation_allow_newline": False,
    "sgm_generation_allow_newline": False,
    "mgm_generation_allow_newline": False,
    "mkm_generation_allow_newline": False,
    "ckm_generation_allow_newline": False,
    "skm_generation_allow_newline": False,
    "srm_generation_allow_newline": False,
    "crm_generation_allow_newline": False,
    "mrm_generation_allow_newline": False,
    "vrm_generation_allow_newline": False,
    "grm_generation_allow_newline": False,
    "orm_generation_allow_newline": False,
    "brm_generation_allow_newline": False,
    "self_prefix": "Person 2",
    "self_memory_prefix": "Person 2's Persona",
    "partner_prefix": "Person 1",
    "partner_memory_prefix": "Person 1's Persona",
    'datatype': 'valid',
    'inject_query_string': None,
    'loglevel': 'info',
    'model': 'projects.bb3.agents.opt_bb3_agent:BlenderBot3Agent',
    'beam_disregard_knowledge_for_srm_context_blocking': False,
    'exclude_context_in_skm_context_blocking': False,
    'include_knowledge_in_ckm_context_blocking': False,
    'knowledge_conditioning': 'combined',
    'num_shots': 0,
    'include_prompt': False,
    'knowledge_chunk_size': 100,
    'max_prompt_len': 1912,
    'all_vanilla_prompt': False,
}