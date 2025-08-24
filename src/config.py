import os

# Get the root directory (one level up from 'src')
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Data directories
DATA_RAW = os.path.join(ROOT_DIR, "data", "raw")
DB_PATH = os.path.join(ROOT_DIR, "data", "hospital.db")

SAVED_COLUMNS = [
    "hospital_name", "state", "county", "procedure_name", "code", "code_type", "setting",
    "cash_price", "cash_discount", "payer", "plan", "allowed_amount", "min_negotiated_price",
    "max_negotiated_price", "rate_type"
]

mount_sinai_brooklyn_columns = [
            "hospital_code","procedure_name","code","code_type","revenue_code","charge_type","modifier",
            "coding_system","setting","department","sub_department","cash_price","cash_discount","payer",
            "plan","payer_contract_type","payer_rate","min_negotiated_price","max_negotiated_price",
            "allowed_amount","standard_charge","rate_type","notes","revenue_code_override","additional_info"
        ]

# URLs of hospitals for price transparency
HOSPITALS = hospital_files = [
    {
        "url": "https://www.mountsinai.org/files/mrf/135564934_mount-sinai-brooklyn_standardcharges.csv",
        "file_name": "mount-sinai-brooklyn_standardcharges.csv",
        "columns_names": mount_sinai_brooklyn_columns,
        "skip_rows": 3,
        "db_cols_mapper":{
            "hospital_name": "Mount Sinai Brooklyn",
            "state": "NY",
            "county": "Kings",
            "allowed_amount": None
        }
    },
    {
        "url": "https://www.mountsinai.org/files/mrf/131624096_mount-sinai-hospital_standardcharges.csv",
        "file_name": "mount-sinai-hospital_standardcharges.csv",
        "columns_names": mount_sinai_brooklyn_columns,
        "skip_rows": 3,
        "db_cols_mapper":{
            "hospital_name": "Mount Sinai Hospital",
            "state": "NY",
            "county": "Kings",
            "allowed_amount": None
        }
    },
    {
        "url": "https://www.mountsinai.org/files/mrf/131624096_mount-sinai-queens_standardcharges.csv",
        "file_name": "mount-sinai-queens_standardcharges.csv",
        "columns_names": mount_sinai_brooklyn_columns,
        "skip_rows": 3,
        "db_cols_mapper":{
            "hospital_name": "Mount Sinai Queens",
            "state": "NY",
            "county": "Kings",
            "allowed_amount": None
        }
    },
    {
        "url": "https://www.mountsinai.org/files/mrf/132997301_mount-sinai-morningside_standardcharges.csv",
        "file_name": "mount-sinai-morningside_standardcharges.csv",
        "columns_names": mount_sinai_brooklyn_columns,
        "skip_rows": 3,
        "db_cols_mapper":{
            "hospital_name": "Mount Sinai Morningside",
            "state": "NY",
            "county": "Kings",
            "allowed_amount": None
        }
    },
    {
        "url": "https://jhm-web-assets.s3.amazonaws.com/hopkinsmedicine/prod/charge-fees/522093120_HowardCountyGeneralHospital_standardcharges.csv",
        "file_name": "howard-county-general-hospital_standardcharges.csv",
        "skip_rows": 3,
        "columns_names": [
            "procedure_name",                 # description
            "code",                           # code|1
            "code_type",                      # code|1|type
            "code_2",                         # code|2
            "code_2_type",                    # code|2|type
            "code_3",                         # code|3
            "code_3_type",                    # code|3|type
            "billing_class",                  # billing_class
            "setting",                        # setting (inpatient/outpatient)
            "drug_unit_of_measurement",       # drug_unit_of_measurement
            "drug_type_of_measurement",       # drug_type_of_measurement
            "modifier",                       # modifiers
            "cash_price",                     # standard_charge|gross
            "cash_discount",                  # standard_charge|discounted_cash
            "payer",                          # payer_name
            "plan",                           # plan_name
            "allowed_amount",                 # standard_charge|negotiated_dollar
            "allowed_percentage",             # standard_charge|negotiated_percentage
            "negotiated_algorithm",           # standard_charge|negotiated_algorithm
            "estimated_amount",               # estimated_amount
            "rate_type",                      # standard_charge|methodology
            "min_negotiated_price",           # standard_charge|min
            "max_negotiated_price",           # standard_charge|max
            "additional_info"                 # additional_generic_notes
        ],
        "db_cols_mapper":{
            "hospital_name": "Howard County General Hospital",
            "state": "ML",
            "county": "Howard",
            "allowed_amount": None
        }
    },
    {
        "url": "https://jhm-web-assets.s3.amazonaws.com/hopkinsmedicine/prod/charge-fees/520591656_JohnsHopkinsHospital_standardcharges.csv",
        "file_name": "johns-hopkins-hospital_standardcharges.csv",
        "skip_rows": 3,
        "columns_names": [
            "procedure_name",                 # description
            "code",                           # code|1
            "code_type",                      # code|1|type
            "code_2",                         # code|2
            "code_2_type",                    # code|2|type
            "code_3",                         # code|3
            "code_3_type",                    # code|3|type
            "billing_class",                  # billing_class
            "setting",                        # setting (inpatient/outpatient)
            "drug_unit_of_measurement",       # drug_unit_of_measurement
            "drug_type_of_measurement",       # drug_type_of_measurement
            "modifier",                       # modifiers
            "cash_price",                     # standard_charge|gross
            "cash_discount",                  # standard_charge|discounted_cash
            "payer",                          # payer_name
            "plan",                           # plan_name
            "allowed_amount",                 # standard_charge|negotiated_dollar
            "allowed_percentage",             # standard_charge|negotiated_percentage
            "negotiated_algorithm",           # standard_charge|negotiated_algorithm
            "estimated_amount",               # estimated_amount
            "rate_type",                      # standard_charge|methodology
            "min_negotiated_price",           # standard_charge|min
            "max_negotiated_price",           # standard_charge|max
            "additional_info"                 # additional_generic_notes
        ],
        "db_cols_mapper":{
            "hospital_name": "Johns Hopkins Hospital",
            "state": "ML",
            "county": "Baltimore",
            "allowed_amount": None
        }
    }
]

# Database config 
DB_PATH = os.path.join(ROOT_DIR, "data", "hospital.db")