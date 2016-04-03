import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('default_config.cfg')

config.set('general', 'num_processes', '1')
config.set('general', 'total_cores', '64')
config.set('general', 'technology_node', '45')
config.set('general', 'max_frequency', '2.0')
config.set('general', 'temperature', '300')

config.set('core/static_instruction_costs', 'generic', '1')
config.set('core/static_instruction_costs', 'mov', '1')
config.set('core/static_instruction_costs', 'ialu', '1')
config.set('core/static_instruction_costs', 'imul', '3')
config.set('core/static_instruction_costs', 'idiv', '18')
config.set('core/static_instruction_costs', 'falu', '3')
config.set('core/static_instruction_costs', 'fmul', '5')
config.set('core/static_instruction_costs', 'fdiv', '6')
config.set('core/static_instruction_costs', 'xmm_ss', '6')
config.set('core/static_instruction_costs', 'xmm_sd', '6')
config.set('core/static_instruction_costs', 'xmm_ps', '6')


config.set('branch_predictor', 'type', 'one_bit')
config.set('branch_predictor', 'mispredict_penalty', '14')
config.set('branch_predictor', 'size', '1024')

config.set('l1_icache/T1', 'cache_line_size', '64')
config.set('l1_icache/T1', 'cache_size', '16')      
config.set('l1_icache/T1', 'associativity', '4')
config.set('l1_icache/T1', 'num_banks', '1')
config.set('l1_icache/T1', 'replacement_policy', 'lru')
config.set('l1_icache/T1', 'data_access_time', '1')
config.set('l1_icache/T1', 'tags_access_time', '1')
config.set('l1_icache/T1', 'perf_model_type', 'parallel')
config.set('l1_icache/T1', 'track_miss_types', 'false')

config.set('l1_dcache/T1', 'cache_line_size', '64')
config.set('l1_dcache/T1', 'cache_size', '32')                        
config.set('l1_dcache/T1', 'associativity', '4')
config.set('l1_dcache/T1', 'num_banks', '1')
config.set('l1_dcache/T1', 'replacement_policy', 'lru')
config.set('l1_dcache/T1', 'data_access_time', '1')                 
config.set('l1_dcache/T1', 'tags_access_time', '1')                    
config.set('l1_dcache/T1', 'perf_model_type', 'parallel')             
config.set('l1_dcache/T1', 'track_miss_types', 'false')

config.set('l2_cache/T1', 'cache_line_size', '64')
config.set('l2_cache/T1', 'cache_size', '512')                        
config.set('l2_cache/T1', 'associativity', '8')
config.set('l2_cache/T1', 'num_banks', '2')
config.set('l2_cache/T1', 'replacement_policy', 'lru')
config.set('l2_cache/T1', 'data_access_time', '8')                 
config.set('l2_cache/T1', 'tags_access_time', '3')                    
config.set('l2_cache/T1', 'perf_model_type', 'parallel')             
config.set('l2_cache/T1', 'track_miss_types', 'false')

config.set('l2_directory', 'max_hw_sharers', '64')
config.set('l2_directory', 'directory_type', 'full_map')

config.set('dram_directory', 'total_entries', 'auto')                      
config.set('dram_directory', 'associativity', '16')
config.set('dram_directory', 'max_hw_sharers', '64')                      
config.set('dram_directory', 'directory_type', 'full_map')             
config.set('dram_directory', 'access_time', 'auto')                   

config.set('limitless', 'software_trap_penalty', '200')                   

config.set('caching_protocol', 'type', 'pr_l1_pr_l2_dram_directory_msi') 

config.set('dram', 'latency', '100') 
config.set('dram', 'per_controller_bandwidth', '5')              
config.set('dram', 'num_controllers', 'ALL')

config.set('dram/queue_model', 'enabled', 'true')
config.set('dram/queue_model', 'type', 'history_tree')

config.set('network', 'user', 'atac')
config.set('network', 'memory', 'atac')

config.set('log', 'disabled_modules', '""')
config.set('log', 'enabled_modules', '""')
config.set('dram', 'controller_positions', '""')
with open("example.cfg", 'wb') as f:
    config.write(f)
