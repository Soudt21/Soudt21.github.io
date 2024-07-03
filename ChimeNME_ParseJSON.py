import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-06-12 19:47:53 UTC",
                "state": "18/20 users created.",
                "errorCount": 2,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 20967800,
                    "auth_token": "d5fee4cc-ee19-4657-8e9d-70d751d640ff",
                    "ssn": "348387036",
                    "email": "Leonia.1718221879+cb1@chime.com",
                    "password": "password",
                    "first_name": "Dominic",
                    "last_name": "Xavier",
                    "date_of_birth": "1961-03-26",
                    "address": "299 Steuber Cove",
                    "zip_code": "61018",
                    "phone": 9669564206,
                    "user_accounts": [
                        {
                            "id": "Qqu7AAQ9",
                            "account_number": "766018453814",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:51:24 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "mEuKyy4M",
                            "account_number": "766018453815",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:51:27 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453814",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "6d11d0c0-19e8-4db6-b403-8745e568997e",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a07e1e94-26b7-49db-85bd-71c489d23986",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1403",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "dominicxavier"
                },
                {
                    "user_id": 20967799,
                    "auth_token": "313b9efd-32f8-47e6-9e84-01b6cba4dee1",
                    "ssn": "075906036",
                    "email": "Malik.1718221869+cb1@chime.com",
                    "password": "password",
                    "first_name": "Antonetta",
                    "last_name": "Kurtis",
                    "date_of_birth": "1990-10-05",
                    "address": "4039 Reichert Overpass",
                    "zip_code": "18901",
                    "phone": 6660037719,
                    "user_accounts": [
                        {
                            "id": "e1uo887v",
                            "account_number": "766018453812",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:51:15 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "3Lu9NNL7",
                            "account_number": "766018453813",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:51:18 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453812",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "df7a84e3-e4d2-4ab4-b494-b6bbd6a174fe",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6b19ee32-1577-4751-a36d-1583e622a91d",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "antonettakurtis1"
                },
                {
                    "user_id": 20967797,
                    "auth_token": "4c3331f2-650d-41ae-8783-03b950280a50",
                    "ssn": "662541252",
                    "email": "Giselle.1718221859+cb1@chime.com",
                    "password": "password",
                    "first_name": "Jae",
                    "last_name": "Britni",
                    "date_of_birth": "1994-07-20",
                    "address": "6054 Jakubowski Mission",
                    "zip_code": "84660",
                    "phone": 4114206541,
                    "user_accounts": [
                        {
                            "id": "bYunNNEW",
                            "account_number": "766018453810",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 01:51:04 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "4ouVQQBQ",
                            "account_number": "766018453811",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 01:51:08 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453810",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a292a7d7-4bd1-4370-bad7-944a63a1e6b3",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1000",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c86c71de-7717-4c3a-b8af-66db2f0d2f26",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "1001",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jaebritni"
                },
                {
                    "user_id": 20967796,
                    "auth_token": "6659311e-2607-418c-820e-f01c1005ca3b",
                    "ssn": "588407544",
                    "email": "Jenice.1718221848+cb1@chime.com",
                    "password": "password",
                    "first_name": "Thad",
                    "last_name": "Russell",
                    "date_of_birth": "2005-10-11",
                    "address": "51068 Lakin Curve",
                    "zip_code": "90210",
                    "phone": 3888985735,
                    "user_accounts": [
                        {
                            "id": "78ugvvoo",
                            "account_number": "766018453808",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 12:50:54 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "wVu011Kx",
                            "account_number": "766018453809",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 12:50:58 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453808",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "f98b816a-0e40-43cc-b0e5-f16ae54b7ad1",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6686214b-b090-4d3c-8f2c-77d078086a65",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "thadrussell"
                },
                {
                    "user_id": 20967794,
                    "auth_token": "36af46b3-724a-4c48-b4f5-4475684d2b87",
                    "ssn": "345604207",
                    "email": "Lisha.1718221838+cb1@chime.com",
                    "password": "password",
                    "first_name": "Matha",
                    "last_name": "Craig",
                    "date_of_birth": "1974-09-19",
                    "address": "4735 Dane Manors",
                    "zip_code": "11599",
                    "phone": 2883101635,
                    "user_accounts": [
                        {
                            "id": "qjuwPPyB",
                            "account_number": "766018453806",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:50:44 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "dNuLllMy",
                            "account_number": "766018453807",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:50:48 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453806",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "31fd6cf6-bc7e-4d18-adbb-42f51f03b8a3",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e5450ed0-b856-48ec-ad47-0087c4780214",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "mathacraig"
                },
                {
                    "user_id": 20967793,
                    "auth_token": "39d6c605-6dd0-4a1e-83c8-c543da3275e0",
                    "ssn": "502102819",
                    "email": "Arlinda.1718221828+cb1@chime.com",
                    "password": "password",
                    "first_name": "Isiah",
                    "last_name": "Wilmer",
                    "date_of_birth": "1981-10-04",
                    "address": "857 Harley Estate",
                    "zip_code": "72908",
                    "phone": 3780300275,
                    "user_accounts": [
                        {
                            "id": "9au9DDoK",
                            "account_number": "766018453804",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:50:33 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "y9unkkX5",
                            "account_number": "766018453805",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:50:38 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453804",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "5294a282-fcad-4d1f-bc3d-e9936d90ac3c",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "8735af4c-3099-41a0-a9dc-830bc21d3067",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "isiahwilmer"
                },
                {
                    "user_id": 20967791,
                    "auth_token": "e64beb81-8cfc-471d-8288-544caff4b5c7",
                    "ssn": "886435984",
                    "email": "Fritz.1718221819+cb1@chime.com",
                    "password": "password",
                    "first_name": "Sylvester",
                    "last_name": "Ileana",
                    "date_of_birth": "1963-07-11",
                    "address": "52615 Roxanna Bridge",
                    "zip_code": "99224",
                    "phone": 2440330139,
                    "user_accounts": [
                        {
                            "id": "MVu2rr8X",
                            "account_number": "766018453802",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 12:50:24 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "VbuVoon5",
                            "account_number": "766018453803",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 12:50:27 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453802",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "0df8f599-de36-4388-b542-399ffd73355e",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "83473c75-ca1c-4907-be48-46a772a5ea82",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "sylvesterileana"
                },
                {
                    "user_id": 20967789,
                    "auth_token": "5d90a983-ec37-4cbd-b25f-2d3cbab13813",
                    "ssn": "009493287",
                    "email": "Roland.1718221809+cb1@chime.com",
                    "password": "password",
                    "first_name": "Allyson",
                    "last_name": "Consuela",
                    "date_of_birth": "1998-07-20",
                    "address": "956 Jerde Mission",
                    "zip_code": "76238",
                    "phone": 2449190095,
                    "user_accounts": [
                        {
                            "id": "nxuEaaY4",
                            "account_number": "766018453800",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:50:14 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "vMuOzzPr",
                            "account_number": "766018453801",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:50:18 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453800",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "7f04c99b-5538-4066-9baa-002d3cba9ece",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0000",
                                    "card_status": "N"
                                },
                                {
                                    "id": "56a4e184-1494-4150-8e68-7d41291bf966",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "0001",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "allysonconsuela"
                },
                {
                    "user_id": 20967787,
                    "auth_token": "a0e0ad8f-3d41-41c8-acea-7162eec0c7a0",
                    "ssn": "267180994",
                    "email": "Manda.1718221798+cb1@chime.com",
                    "password": "password",
                    "first_name": "Danial",
                    "last_name": "Jaqueline",
                    "date_of_birth": "1978-03-22",
                    "address": "44147 Petrina Mount",
                    "zip_code": "34949",
                    "phone": 8113092831,
                    "user_accounts": [
                        {
                            "id": "Pyu7113b",
                            "account_number": "766018453798",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:50:04 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "jlu4jjz0",
                            "account_number": "766018453799",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:50:08 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453798",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "f8e62c7b-2bc1-40a6-9a98-6e22b2055383",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f3d765d3-ffa1-4e48-ba9c-865cf29c1e62",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "danialjaqueline1"
                },
                {
                    "user_id": 20967785,
                    "auth_token": "78aa77f1-6194-4ed8-8a36-219236f5742c",
                    "ssn": "025432258",
                    "email": "Donald.1718221788+cb1@chime.com",
                    "password": "password",
                    "first_name": "Reginald",
                    "last_name": "Dina",
                    "date_of_birth": "1969-11-23",
                    "address": "134 Malik Grove",
                    "zip_code": "78521",
                    "phone": 4889026539,
                    "user_accounts": [
                        {
                            "id": "E6uoAANK",
                            "account_number": "766018453796",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:49:53 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "xguv5583",
                            "account_number": "766018453797",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:49:57 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453796",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "4a6baadb-6b23-4979-a631-f118f18c4283",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "78fa193d-1361-4473-b16b-79e89b04d4fc",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "reginalddina"
                },
                {
                    "user_id": 20967784,
                    "auth_token": "288d90f2-4f65-4db9-8018-1b3d1dfe364f",
                    "ssn": "600755365",
                    "email": "Erin.1718221778+cb1@chime.com",
                    "password": "password",
                    "first_name": "Jenette",
                    "last_name": "Franchesca",
                    "date_of_birth": "1962-08-21",
                    "address": "11994 Lindsay Forks",
                    "zip_code": "02920",
                    "phone": 2884966909,
                    "user_accounts": [
                        {
                            "id": "lDu2118O",
                            "account_number": "766018453793",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:49:44 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "DxuYmmVn",
                            "account_number": "766018453795",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:49:47 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453793",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "5a942855-af09-45cc-879f-e26774eaf89f",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9300",
                                    "card_status": "N"
                                },
                                {
                                    "id": "025c008d-f31a-4242-8c52-039592e5f70e",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "9301",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jenettefranchesca"
                },
                {
                    "user_id": 20967780,
                    "auth_token": "ee2ced37-cc6e-4dcd-a688-b969d829d66e",
                    "ssn": "401704182",
                    "email": "Dominic.1718221758+cb1@chime.com",
                    "password": "password",
                    "first_name": "Eugene",
                    "last_name": "Merlene",
                    "date_of_birth": "1974-08-23",
                    "address": "29011 Marcel Pike",
                    "zip_code": "80026",
                    "phone": 2110324544,
                    "user_accounts": [
                        {
                            "id": "NguDBBn8",
                            "account_number": "766018453788",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 01:49:24 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "O9uZBBz6",
                            "account_number": "766018453789",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 01:49:28 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453788",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "ce07eb46-47ba-4521-af37-31ddfa4c653d",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "8800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "7f22ebc7-40fc-47b8-8e2c-c8aa9adbbdbb",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "8801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "eugenemerlene1"
                },
                {
                    "user_id": 20967776,
                    "auth_token": "251cd89f-e9df-44d6-a28e-18872b9d5301",
                    "ssn": "003096875",
                    "email": "Mignon.1718221725+cb1@chime.com",
                    "password": "password",
                    "first_name": "Sung",
                    "last_name": "Micheal",
                    "date_of_birth": "1959-07-14",
                    "address": "55976 Little Forge",
                    "zip_code": "70047",
                    "phone": 3556420714,
                    "user_accounts": [
                        {
                            "id": "LMu4xxjY",
                            "account_number": "766018453779",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:50 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "W4ukjj84",
                            "account_number": "766018453781",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:54 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453779",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "23350b37-157e-43ad-a1aa-3a45a688fc61",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9045a994-ec97-480b-9e58-8d27d532d93f",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "sungmicheal"
                },
                {
                    "user_id": 20967774,
                    "auth_token": "a6e3bbe0-481f-4871-8f02-b2d238e5c4d7",
                    "ssn": "447034779",
                    "email": "Richie.1718221715+cb1@chime.com",
                    "password": "password",
                    "first_name": "Amina",
                    "last_name": "Armanda",
                    "date_of_birth": "1982-08-29",
                    "address": "503 Marcellus Meadow",
                    "zip_code": "14603",
                    "phone": 2222385637,
                    "user_accounts": [
                        {
                            "id": "3Lu9NNY7",
                            "account_number": "766018453776",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:48:41 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "Qqu7AA29",
                            "account_number": "766018453777",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:48:44 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453776",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "c95ade3f-52f3-46b1-ab8c-e61bbad12886",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a4e39822-e46a-4316-88bd-67b83f71599b",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "aminaarmanda"
                },
                {
                    "user_id": 20967771,
                    "auth_token": "f3c74bb5-2325-4006-b8bb-5e9dba448ca9",
                    "ssn": "503387230",
                    "email": "Morgan.1718221706+cb1@chime.com",
                    "password": "password",
                    "first_name": "Waneta",
                    "last_name": "Hanna",
                    "date_of_birth": "1965-02-28",
                    "address": "8396 Haag Mount",
                    "zip_code": "78747",
                    "phone": 9687854509,
                    "user_accounts": [
                        {
                            "id": "wVu011wx",
                            "account_number": "766018453772",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:31 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "zyu9776j",
                            "account_number": "766018453774",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:34 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453772",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "9b131387-cb70-457f-9353-e9f46b5b38fe",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "4df86a23-7a0a-4d1a-8fb2-8e24bd082002",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "7203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "wanetahanna1"
                },
                {
                    "user_id": 20967770,
                    "auth_token": "9f9a55db-547e-4ee3-b147-82edba551bda",
                    "ssn": "111525744",
                    "email": "Tessa.1718221696+cb1@chime.com",
                    "password": "password",
                    "first_name": "Clementine",
                    "last_name": "Felix",
                    "date_of_birth": "1997-09-17",
                    "address": "54814 Cruickshank Vista",
                    "zip_code": "02152",
                    "phone": 9881710892,
                    "user_accounts": [
                        {
                            "id": "dNuLllZy",
                            "account_number": "766018453769",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:48:22 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "78ugvv9o",
                            "account_number": "766018453771",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 03:48:25 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453769",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "d4bea117-d6b2-4343-9c2b-de5cd8136d0e",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6900",
                                    "card_status": "N"
                                },
                                {
                                    "id": "59dfbb15-6b47-412f-8614-95fba024f9b9",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6901",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "clementinefelix"
                },
                {
                    "user_id": 20967768,
                    "auth_token": "091e717a-e1be-4eb5-a6a1-3157228408c5",
                    "ssn": "109866733",
                    "email": "Titus.1718221686+cb1@chime.com",
                    "password": "password",
                    "first_name": "Cedrick",
                    "last_name": "Salina",
                    "date_of_birth": "1971-12-19",
                    "address": "8712 Stokes Orchard",
                    "zip_code": "68941",
                    "phone": 3669404978,
                    "user_accounts": [
                        {
                            "id": "9au9DDMK",
                            "account_number": "766018453766",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 07:48:12 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "y9unkkO5",
                            "account_number": "766018453767",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 07:48:15 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453766",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "3bb29249-83e1-4b5b-bf4f-583531b41c21",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "3d635910-f719-4712-b414-092d33ee9800",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "cedricksalina"
                },
                {
                    "user_id": 20967766,
                    "auth_token": "fce84290-3ac4-46eb-a8c1-2028fed01dd3",
                    "ssn": "805763784",
                    "email": "Tyler.1718221675+cb1@chime.com",
                    "password": "password",
                    "first_name": "Jeremiah",
                    "last_name": "Lashell",
                    "date_of_birth": "1968-05-23",
                    "address": "490 Rudolph Springs",
                    "zip_code": "63113",
                    "phone": 9339119701,
                    "user_accounts": [
                        {
                            "id": "Z3uAwwv8",
                            "account_number": "766018453762",
                            "account_type": "checking",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:01 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        },
                        {
                            "id": "VbuVoox5",
                            "account_number": "766018453764",
                            "account_type": "savings",
                            "routing_number": "031101279",
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-12 02:48:05 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018453762",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "863dd5b5-172e-4c25-84a8-3cb137885400",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e24d5b72-52af-4bbe-b732-c873ff5595a0",
                                    "expiry_date": "2028-06-12",
                                    "card_number": "6203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jeremiahlashell"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/2133671446635595960"
}
'''

# Assuming the JSON is stored in a variable named 'json_data'
data = json.loads(json_data)

# Extract emails and SSNs
emails = [user['email'] for user in data['data']['getBulkUsers']['users']]
ssns = [user['ssn'] for user in data['data']['getBulkUsers']['users']]

print("Emails:")
for email in emails:
    print(email)

    

