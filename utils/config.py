import ConfigParser
from sim_constants import *

def setupConfigFile(data, config_path):
    config = ConfigParser.RawConfigParser()
    config.read(DEFAULT_CONFIG)

    print data['total_cores']

    config.set('general', 'total_cores', data['total_cores'])
    config.set('general', 'technology_node', data['technology_node'])
    config.set('general', 'temperature', data['temperature'])

    config.set('core/static_instruction_costs', 'generic', data['generic'])
    config.set('core/static_instruction_costs', 'mov', data['mov'])
    config.set('core/static_instruction_costs', 'ialu', data['ialu'])
    config.set('core/static_instruction_costs', 'imul', data['imul'])
    config.set('core/static_instruction_costs', 'idiv', data['idiv'])
    config.set('core/static_instruction_costs', 'falu', data['falu'])
    config.set('core/static_instruction_costs', 'fmul', data['fmul'])
    config.set('core/static_instruction_costs', 'fdiv', data['fdiv'])
    config.set('core/static_instruction_costs', 'xmm_ss', data['xmm_ss'])
    config.set('core/static_instruction_costs', 'xmm_sd', data['xmm_sd'])
    config.set('core/static_instruction_costs', 'xmm_ps', data['xmm_ps'])

    config.set('branch_predictor', 'mispredict_penalty', data['mispredict_penalty'])

    config.set('l1_icache/T1', 'cache_line_size', data['l1i_cache_line_size'])
    config.set('l1_icache/T1', 'cache_size', data['l1i_cache_size'])
    config.set('l1_icache/T1', 'associativity', data['l1i_associativity'])
    config.set('l1_icache/T1', 'num_banks', data['l1i_num_banks'])
    config.set('l1_icache/T1', 'replacement_policy', data['l1i_replacement_policy'])
    config.set('l1_icache/T1', 'data_access_time', data['l1i_data_access_time'])
    config.set('l1_icache/T1', 'tags_access_time', data['l1i_tags_access_time'])
    config.set('l1_icache/T1', 'perf_model_type', data['l1i_perf_model_type'])
    config.set('l1_icache/T1', 'track_miss_types', data['l1i_track_miss_types'])

    config.set('l1_dcache/T1', 'cache_line_size', data['l1d_cache_line_size'])
    config.set('l1_dcache/T1', 'cache_size', data['l1d_cache_size'])
    config.set('l1_dcache/T1', 'associativity', data['l1d_associativity'])
    config.set('l1_dcache/T1', 'num_banks', data['l1d_num_banks'])
    config.set('l1_dcache/T1', 'replacement_policy', data['l1d_replacement_policy'])
    config.set('l1_dcache/T1', 'data_access_time', data['l1d_data_access_time'])
    config.set('l1_dcache/T1', 'tags_access_time', data['l1d_tags_access_time'])
    config.set('l1_dcache/T1', 'perf_model_type', data['l1d_perf_model_type'])
    config.set('l1_dcache/T1', 'track_miss_types', data['l1d_track_miss_types'])

    config.set('l2_cache/T1', 'cache_line_size', data['l2_cache_line_size'])
    config.set('l2_cache/T1', 'cache_size', data['l2_cache_size'])
    config.set('l2_cache/T1', 'associativity', data['l2_associativity'])
    config.set('l2_cache/T1', 'num_banks', data['l2_num_banks'])
    config.set('l2_cache/T1', 'replacement_policy', data['l2_replacement_policy'])
    config.set('l2_cache/T1', 'data_access_time', data['l2_data_access_time'])
    config.set('l2_cache/T1', 'tags_access_time', data['l2_tags_access_time'])
    config.set('l2_cache/T1', 'perf_model_type', data['l2_perf_model_type'])
    config.set('l2_cache/T1', 'track_miss_types', data['l2_track_miss_types'])

    config.set('l2_directory', 'max_hw_sharers', data['l2_dir_max_hw_sharers'])
    config.set('l2_directory', 'directory_type', data['l2_dir_directory_type'])

    config.set('dram_directory', 'total_entries', data['dram_dir_total_entries'])
    config.set('dram_directory', 'associativity', data['dram_dir_associativity'])
    config.set('dram_directory', 'max_hw_sharers', data['dram_dir_max_hw_sharers'])
    config.set('dram_directory', 'directory_type', data['dram_dir_directory_type'])
    config.set('dram_directory', 'access_time', data['access_time'])

    config.set('limitless', 'software_trap_penalty', data['software_trap_penalty'])

    config.set('caching_protocol', 'type', data['type'])

    config.set('dram', 'latency', data['latency'])
    config.set('dram', 'per_controller_bandwidth', data['per_controller_bandwidth'])
    config.set('dram', 'num_controllers', data['num_controllers'])

    config.set('network', 'user', data['user'])
    config.set('network', 'memory', data['memory'])

    config.set('log', 'disabled_modules', '""')
    config.set('log', 'enabled_modules', '""')
    config.set('dram', 'controller_positions', '""')
    print "Writing config file"
    with open(config_path, 'wb') as f:
        config.write(f)
