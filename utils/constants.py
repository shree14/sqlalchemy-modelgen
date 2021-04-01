from os import getcwd, path
key_tables = 'tables'
key_columns = 'columns'
key_column_name = 'name'
key_column_type = 'type'
key_column_length = 'length'
key_extra_params = 'extra_params'
key_extra_params_name = 'name'
key_extra_params_value = 'value'
key_src_store = 'source_store'
key_database = 'database'
key_inherit_from = 'inherit_from'

templates_folder = path.join(getcwd(), 'templates')

models_folder = path.join(getcwd(), 'models')

sqlalchemy_python_types = {'smallint':'SmallInteger', 'integer':'Integer',  
                           'bigint':'BigInteger',  'short':'Integer',  'long':'BigInteger', 
                           'decimal':'Numeric',  'numeric':'Numeric',  'double':'Float', 
                           'real':'Float',  'float':'Float',  'boolean':'Boolean', 
                           'char':'String',  'varchar':'String',  'timestamp':'DateTime',
                           'date': 'Date'}
