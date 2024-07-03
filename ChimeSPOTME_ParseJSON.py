import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-06-26 16:44:56 UTC",
                "state": "19/20 users created.",
                "errorCount": 1,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 21167264,
                    "auth_token": "37a993ac-54cc-4728-9a98-8d7625a781ee",
                    "ssn": "242626808",
                    "email": "1719420628_rudy@hotmail.com",
                    "password": "password",
                    "first_name": "Leana",
                    "last_name": "Prudence",
                    "date_of_birth": "1991-11-12",
                    "address": "3324 Selina Flats",
                    "zip_code": "68855",
                    "phone": 7118693668,
                    "user_accounts": [
                        {
                            "id": "lDu2AYwa",
                            "account_number": "766018681002",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 04:50:34 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681002",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b3846107-830c-4397-8ab3-727863f58192",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9551fd02-8fa5-4ec3-b5fc-bc55c4317005",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "leanaprudence"
                },
                {
                    "user_id": 21167262,
                    "auth_token": "48b63304-bebb-4da2-9a68-dd74d8f6853f",
                    "ssn": "009563551",
                    "email": "1719420609.cruz@gmail.com",
                    "password": "password",
                    "first_name": "Teodoro",
                    "last_name": "Isaias",
                    "date_of_birth": "1998-12-30",
                    "address": "402 Derick Throughway",
                    "zip_code": "94606",
                    "phone": 2667011791,
                    "user_accounts": [
                        {
                            "id": "XzuOB2ml",
                            "account_number": "766018681001",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 09:50:16 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681001",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "dcfec9fd-c152-47a9-a22d-8d56a265a6dc",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "02eb84bb-9549-4346-b8ce-8d87fda9ed40",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "teodoroisaias"
                },
                {
                    "user_id": 21167261,
                    "auth_token": "a8d3817b-49c0-40e8-b3be-6ba3c10a9cfc",
                    "ssn": "856755701",
                    "email": "1719420592_eduardo@hotmail.com",
                    "password": "password",
                    "first_name": "Thad",
                    "last_name": "Kiera",
                    "date_of_birth": "1995-10-12",
                    "address": "391 Clayton Mission",
                    "zip_code": "62338",
                    "phone": 9333821156,
                    "user_accounts": [
                        {
                            "id": "03um8q53",
                            "account_number": "766018681000",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:49:57 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681000",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "cb743a44-bda9-4b3e-940a-59ca19b9103e",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "aacb022f-c7dc-46e9-a7b2-52bebc3b4c81",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "thadkiera"
                },
                {
                    "user_id": 21167258,
                    "auth_token": "58d67a82-aea9-4b68-baea-75693374d413",
                    "ssn": "417875574",
                    "email": "1719420574_johna@hotmail.com",
                    "password": "password",
                    "first_name": "Casey",
                    "last_name": "Tommy",
                    "date_of_birth": "1992-02-05",
                    "address": "902 Genaro Overpass",
                    "zip_code": "72070",
                    "phone": 9675912898,
                    "user_accounts": [
                        {
                            "id": "NguDlY75",
                            "account_number": "766018680999",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:49:40 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680999",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "dc7c0a7a-ee59-4401-ba52-668883c0bc71",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1a292c10-f18c-42ba-aa5a-374f30c7f4e9",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "caseytommy1"
                },
                {
                    "user_id": 21167256,
                    "auth_token": "ad4f406d-329f-46b5-811f-7f555b1e21f7",
                    "ssn": "845935475",
                    "email": "lyla.1719420555@yahoo.com",
                    "password": "password",
                    "first_name": "Ambrose",
                    "last_name": "Landon",
                    "date_of_birth": "1967-05-09",
                    "address": "180 Kyle Ways",
                    "zip_code": "46531",
                    "phone": 3758059498,
                    "user_accounts": [
                        {
                            "id": "kAuwDAeb",
                            "account_number": "766018680998",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 04:49:21 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680998",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "2fad9a27-58b2-440a-896c-090de0f859d5",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "890a6d5f-8c11-4a0d-ad12-26a28ca839f6",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "ambroselandon"
                },
                {
                    "user_id": 21167255,
                    "auth_token": "bfc2fb35-5394-4db0-81e2-eb733c39c09c",
                    "ssn": "414985765",
                    "email": "tracey.1719420538@yahoo.com",
                    "password": "password",
                    "first_name": "Clarence",
                    "last_name": "Jamison",
                    "date_of_birth": "1993-05-21",
                    "address": "310 Wilderman Mountain",
                    "zip_code": "32043",
                    "phone": 9637752839,
                    "user_accounts": [
                        {
                            "id": "BDuokWq6",
                            "account_number": "766018680997",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1100.0,
                            "balance_updated_at": "2024-06-26 12:49:15 PM",
                            "balances": {
                                "display": 1100.0,
                                "balance": 1100.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680997",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "acf1f3d4-ad52-495e-8fa7-4920660d5eb5",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "05c5e3fd-e70d-462b-87cd-1c2571b7d385",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9701",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "clarencejamison"
                },
                {
                    "user_id": 21167253,
                    "auth_token": "78914c4d-7b96-4029-a628-69f5624bfe4c",
                    "ssn": "498241691",
                    "email": "chet_1719420520@hotmail.com",
                    "password": "password",
                    "first_name": "Dede",
                    "last_name": "Alec",
                    "date_of_birth": "2002-05-24",
                    "address": "21392 Elias Square",
                    "zip_code": "95651",
                    "phone": 9615731908,
                    "user_accounts": [
                        {
                            "id": "8YugenXZ",
                            "account_number": "766018680996",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 09:48:46 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680996",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "ce477d89-bd36-473d-9108-228ed1e5a395",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c387ecd6-70d0-47f2-a6af-96a427f4c99e",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "dedealec"
                },
                {
                    "user_id": 21167251,
                    "auth_token": "e38b58f1-40aa-4886-a7a6-0229fdeb6718",
                    "ssn": "231707775",
                    "email": "1719420502_jacob@gmail.com",
                    "password": "password",
                    "first_name": "Erasmo",
                    "last_name": "Marcellus",
                    "date_of_birth": "1989-06-30",
                    "address": "9669 Corrine Bridge",
                    "zip_code": "49343",
                    "phone": 3730146308,
                    "user_accounts": [
                        {
                            "id": "W4uknBbo",
                            "account_number": "766018680995",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1100.0,
                            "balance_updated_at": "2024-06-26 04:48:40 PM",
                            "balances": {
                                "display": 1100.0,
                                "balance": 1100.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680995",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a1630a94-2dd8-41b3-86b1-c6761c28c6f3",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "d20cfffe-3ff2-4830-b0ed-c35d9ff50cda",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "erasmomarcellus"
                },
                {
                    "user_id": 21167249,
                    "auth_token": "269fed6d-58f9-45f9-8808-a73ea3ac2d09",
                    "ssn": "063122041",
                    "email": "erick_1719420484@yahoo.com",
                    "password": "password",
                    "first_name": "Erna",
                    "last_name": "Nicky",
                    "date_of_birth": "1959-12-08",
                    "address": "5649 Shawn Roads",
                    "zip_code": "11948",
                    "phone": 3334274961,
                    "user_accounts": [
                        {
                            "id": "LMu4OrYy",
                            "account_number": "766018680994",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:48:10 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680994",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "7c3aee57-b98c-4c8b-a50d-49630f13383e",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a2a6cf81-883a-4bd2-a4fc-6387e0f9f0cc",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "ernanicky"
                },
                {
                    "user_id": 21167248,
                    "auth_token": "8ba704dd-7253-4e02-b42f-4f5f2cfa604c",
                    "ssn": "172237761",
                    "email": "1719420467.verlene@yahoo.com",
                    "password": "password",
                    "first_name": "Coreen",
                    "last_name": "Zula",
                    "date_of_birth": "1962-09-19",
                    "address": "464 Maggio Ports",
                    "zip_code": "65584",
                    "phone": 9638733657,
                    "user_accounts": [
                        {
                            "id": "mEuKlMWY",
                            "account_number": "766018680993",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:47:53 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680993",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "48266653-8de6-494c-a485-b18369f45f79",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9302",
                                    "card_status": "N"
                                },
                                {
                                    "id": "7a4910a6-016a-4dc8-a89a-f36136be52bc",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9303",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "coreenzula1"
                },
                {
                    "user_id": 21167246,
                    "auth_token": "614852b2-10c4-48bb-abec-bc96e7991e86",
                    "ssn": "686178086",
                    "email": "herb_1719420449@gmail.com",
                    "password": "password",
                    "first_name": "Marnie",
                    "last_name": "Kathyrn",
                    "date_of_birth": "1965-12-28",
                    "address": "1883 Sonya Estates",
                    "zip_code": "85364",
                    "phone": 9619690038,
                    "user_accounts": [
                        {
                            "id": "3Lu97gKe",
                            "account_number": "766018680992",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 09:47:35 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680992",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a9e419b1-5b97-428c-bee9-a484e2436b64",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "fed49038-b62b-4b7a-bfc9-11939ebd78c5",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "marniekathyrn"
                },
                {
                    "user_id": 21167243,
                    "auth_token": "e94de937-3e62-4197-a7aa-c35b3c0d6a9f",
                    "ssn": "157720052",
                    "email": "1719420431.anton@gmail.com",
                    "password": "password",
                    "first_name": "Guy",
                    "last_name": "Eldon",
                    "date_of_birth": "1990-03-03",
                    "address": "89843 Matthew Burg",
                    "zip_code": "45169",
                    "phone": 3791416167,
                    "user_accounts": [
                        {
                            "id": "4ouVb0wz",
                            "account_number": "766018680991",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:47:17 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680991",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a1ed1ec9-c8b0-404e-b2f5-dd8a91a91bca",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9100",
                                    "card_status": "N"
                                },
                                {
                                    "id": "14e54339-6121-4f0a-9c92-8d59650f682b",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9101",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "guyeldon"
                },
                {
                    "user_id": 21167241,
                    "auth_token": "e2700d35-d7f2-432a-a6a1-994d51d9080d",
                    "ssn": "255253950",
                    "email": "freida.1719420412@yahoo.com",
                    "password": "password",
                    "first_name": "Antoine",
                    "last_name": "Seth",
                    "date_of_birth": "1961-12-03",
                    "address": "39815 Beau Ridges",
                    "zip_code": "25981",
                    "phone": 9449651008,
                    "user_accounts": [
                        {
                            "id": "wVu0dOLr",
                            "account_number": "766018680990",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:46:58 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680990",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "80d4a02b-9993-4ce6-822a-e51270a383bb",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9000",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e927aa89-ee2a-40ab-a349-17749fd868c3",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9001",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "antoineseth"
                },
                {
                    "user_id": 21167240,
                    "auth_token": "4a588ec9-7f36-4330-9856-95dba84adf6f",
                    "ssn": "569426613",
                    "email": "lavada.1719420391@yahoo.com",
                    "password": "password",
                    "first_name": "Lashon",
                    "last_name": "Jeri",
                    "date_of_birth": "1980-08-12",
                    "address": "9003 Klein Estate",
                    "zip_code": "72853",
                    "phone": 2669608827,
                    "user_accounts": [
                        {
                            "id": "78ugqVwe",
                            "account_number": "766018680989",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:46:37 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680989",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "6100bec4-76ab-4253-ac08-1556961af1d4",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "00ca01d7-b495-468a-a89e-6ab3db6e2440",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "lashonjeri"
                },
                {
                    "user_id": 21167239,
                    "auth_token": "c45370ae-6c72-4189-a103-d6f68971ca64",
                    "ssn": "655117870",
                    "email": "darrel.1719420373@yahoo.com",
                    "password": "password",
                    "first_name": "Benny",
                    "last_name": "Louanne",
                    "date_of_birth": "2003-01-11",
                    "address": "9425 Hirthe Mountains",
                    "zip_code": "35179",
                    "phone": 3007741871,
                    "user_accounts": [
                        {
                            "id": "KZuZPQ1v",
                            "account_number": "766018680988",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:46:19 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680988",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "23a55a01-c2c0-4fe2-92ed-9e1d26ed7f14",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8802",
                                    "card_status": "N"
                                },
                                {
                                    "id": "0ce71830-cdec-4a08-a6eb-6e787d82078f",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8803",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "bennylouanne"
                },
                {
                    "user_id": 21167236,
                    "auth_token": "e6c76cbc-bd98-4fd1-9a0e-5b4b55289d21",
                    "ssn": "853361093",
                    "email": "1719420352_fred@yahoo.com",
                    "password": "password",
                    "first_name": "Kent",
                    "last_name": "Kennith",
                    "date_of_birth": "1973-11-20",
                    "address": "5939 Thompson Roads",
                    "zip_code": "24019",
                    "phone": 9666837199,
                    "user_accounts": [
                        {
                            "id": "qjuwMYXL",
                            "account_number": "766018680987",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:45:58 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680987",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b2cd4f1e-5949-41e4-83f7-cf56a73abed5",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8702",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9978703c-a119-4e91-bed1-b031914b9dc1",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8703",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "kentkennith"
                },
                {
                    "user_id": 21167235,
                    "auth_token": "48a306f8-2aab-48db-a408-2591ac72ea3e",
                    "ssn": "052725257",
                    "email": "1719420333.letha@gmail.com",
                    "password": "password",
                    "first_name": "Marchelle",
                    "last_name": "Jolie",
                    "date_of_birth": "1967-05-07",
                    "address": "99103 Waldo Crescent",
                    "zip_code": "95116",
                    "phone": 2661732990,
                    "user_accounts": [
                        {
                            "id": "y9undBL7",
                            "account_number": "766018680986",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 09:45:39 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680986",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b1d1f5f2-e3e3-41b1-8fc5-51ba452c6af1",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e25f7c97-bb8f-40a5-b7ed-c4f5c578fa1f",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "marchellejolie"
                },
                {
                    "user_id": 21167234,
                    "auth_token": "ae7d3d4c-3c09-442b-998a-538186446707",
                    "ssn": "097091274",
                    "email": "1719420315_brian@hotmail.com",
                    "password": "password",
                    "first_name": "Minda",
                    "last_name": "Loraine",
                    "date_of_birth": "1973-06-04",
                    "address": "1695 Dylan Track",
                    "zip_code": "27315",
                    "phone": 9643105583,
                    "user_accounts": [
                        {
                            "id": "9au9vgq9",
                            "account_number": "766018680985",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:45:20 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680985",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "d989f48e-0b28-49d0-a3f5-fb6026da8469",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9b5c2ed1-68b6-4f90-bd3f-3b43cf36546b",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "mindaloraine"
                },
                {
                    "user_id": 21167232,
                    "auth_token": "ecbcb953-83ea-43ba-b7c0-d3a429f6fb78",
                    "ssn": "619470707",
                    "email": "hang.1719420296@yahoo.com",
                    "password": "password",
                    "first_name": "Brooks",
                    "last_name": "Maynard",
                    "date_of_birth": "1993-07-20",
                    "address": "5179 Schaefer Forest",
                    "zip_code": "63465",
                    "phone": 7556377538,
                    "user_accounts": [
                        {
                            "id": "VbuVZA03",
                            "account_number": "766018680983",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 11:45:02 AM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018680983",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "61353c95-167a-4260-be14-9884da398420",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8302",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5b0c175f-5a3b-4ac0-91d1-d72a5a39ae15",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8303",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "referral_token": "brooksmaynard"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/5134668288775651993"
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


    

