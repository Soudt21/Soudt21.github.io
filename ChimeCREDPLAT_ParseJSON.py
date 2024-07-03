import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-05-29 17:47:09 UTC",
                "state": "19/20 users created.",
                "errorCount": 1,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 20774360,
                    "auth_token": "34806a7f-2cbb-484e-995d-c9c8c6885a10",
                    "ssn": "107182059",
                    "email": "1717005836.kirby@yahoo.com",
                    "password": "password",
                    "first_name": "Ngan",
                    "last_name": "Berry",
                    "date_of_birth": "1978-03-09",
                    "address": "81125 Jakubowski Light",
                    "zip_code": "68381",
                    "phone": 9881531060,
                    "user_accounts": [
                        {
                            "id": "4ouVo98M",
                            "account_number": "689118245016",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 06:04:42 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "r2ur1Bkk",
                            "account_number": "668118245035",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 06:04:34 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "lDu237N5",
                            "account_number": "668118245036",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 06:04:17 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "nxuEdVjM",
                            "account_number": "689118245057",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 06:04:41 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118245016",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "c5478d20-46e5-4567-91b3-5563cf198900",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "1604",
                                    "card_status": "N"
                                },
                                {
                                    "id": "401f0f21-1667-48b9-b92c-7f82adb988d0",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "1605",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118245036",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "0609455f-a65a-4dbc-871c-46d09d0dd7a6",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "3600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9b40242d-4737-4704-bfc5-111f5f523152",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "3601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774317,
                    "auth_token": "7678bd14-cdb4-4cc2-8776-6cbbeb1e71cb",
                    "ssn": "822383348",
                    "email": "terence.1717005783@gmail.com",
                    "password": "password",
                    "first_name": "Larissa",
                    "last_name": "Ty",
                    "date_of_birth": "2001-11-23",
                    "address": "59676 Zackary Village",
                    "zip_code": "50627",
                    "phone": 7661476187,
                    "user_accounts": [
                        {
                            "id": "78ug7KWj",
                            "account_number": "689118244970",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:03:55 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "5WuWd02e",
                            "account_number": "668118244981",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:03:47 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "8YugwbZM",
                            "account_number": "668118244982",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:03:30 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "MVu2PNqO",
                            "account_number": "689118245005",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:03:55 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244970",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "df40779f-2eed-42ee-9f60-43628e950544",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7004",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6bf5d04d-5a93-4a3d-898e-cd4702e07cf9",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7005",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244982",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "b2386aea-9f48-45c7-9078-719d482df0e3",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "b1e669a3-231a-49bc-a18f-b6d6ecfe8090",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774292,
                    "auth_token": "4860ced2-345a-4e99-8f6d-ff3a32f58439",
                    "ssn": "765140007",
                    "email": "regan_1717005735@gmail.com",
                    "password": "password",
                    "first_name": "Donella",
                    "last_name": "Jacquie",
                    "date_of_birth": "1987-07-03",
                    "address": "6459 Runolfsdottir Parkways",
                    "zip_code": "22938",
                    "phone": 7775616556,
                    "user_accounts": [
                        {
                            "id": "BDuo1YPl",
                            "account_number": "689118244944",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 02:03:02 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "r2ur1Bok",
                            "account_number": "668118244951",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 02:02:56 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "DxuY0dwg",
                            "account_number": "668118244954",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 02:02:37 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "VbuV9M6o",
                            "account_number": "689118244964",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 02:03:02 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244944",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "4add2170-f8a5-48e9-8ba3-c9875dd8a5b1",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4406",
                                    "card_status": "N"
                                },
                                {
                                    "id": "3b879145-43cc-4c0a-80e7-c2ed23d6acd3",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4407",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244954",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "0a65c776-fa35-4ad3-bbb6-a6671316837a",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a58a8f39-4601-4e9f-a840-2007e628dac6",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774261,
                    "auth_token": "e6fd9243-57ce-41d7-ad45-f5bad151806d",
                    "ssn": "712075295",
                    "email": "lon.1717005686@hotmail.com",
                    "password": "password",
                    "first_name": "Bertram",
                    "last_name": "Damian",
                    "date_of_birth": "1966-04-28",
                    "address": "487 Carl Parks",
                    "zip_code": "63549",
                    "phone": 2330738491,
                    "user_accounts": [
                        {
                            "id": "Z3uAKy4X",
                            "account_number": "689118244909",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:02:14 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "e1uodXaN",
                            "account_number": "668118244923",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:02:08 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "3Lu9yPbN",
                            "account_number": "668118244924",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:01:50 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "03umVK6a",
                            "account_number": "689118244938",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:02:14 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244909",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "ec524487-7c24-4543-b88e-e7db4c1d7261",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "8df3df60-09e1-4773-87ca-9e78d349567b",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0903",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244924",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "878060b4-fae5-4fbc-af21-984118245ace",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "2400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c83faa9e-acf6-46dd-80b0-6d96358e01f4",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "2401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774258,
                    "auth_token": "3d2244e3-ed44-44a6-b194-864ff35097c7",
                    "ssn": "780636269",
                    "email": "1717005634_davis@hotmail.com",
                    "password": "password",
                    "first_name": "Anthony",
                    "last_name": "Edgardo",
                    "date_of_birth": "1970-10-02",
                    "address": "613 Feeney Vista",
                    "zip_code": "36029",
                    "phone": 2551346073,
                    "user_accounts": [
                        {
                            "id": "xguv2zeP",
                            "account_number": "689118244904",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:01:25 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "65u2KM5x",
                            "account_number": "668118244905",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:01:21 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "Pyu7nVbK",
                            "account_number": "668118244906",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:00:59 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "nxuEdVNN",
                            "account_number": "689118244908",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:01:25 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244904",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "db7c14ea-e63c-46e7-ae49-8bad0689a22e",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0403",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5fa84387-1208-45a6-8f8e-7d8acdcddb2a",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0404",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244906",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "cddff79f-8040-43a7-99ed-247d92406708",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0604",
                                    "card_status": "N"
                                },
                                {
                                    "id": "3a30571b-ed34-4a75-ac2f-c3a001e16e6f",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0605",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774257,
                    "auth_token": "a8be9903-acfe-4a1e-ad18-2550d548d4fb",
                    "ssn": "213346708",
                    "email": "1717005576_jenifer@yahoo.com",
                    "password": "password",
                    "first_name": "Agnus",
                    "last_name": "Lazaro",
                    "date_of_birth": "1991-08-07",
                    "address": "7568 Orn Center",
                    "zip_code": "25515",
                    "phone": 3713953166,
                    "user_accounts": [
                        {
                            "id": "XzuOqaeM",
                            "account_number": "689118244898",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 02:00:34 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "r2ur1BON",
                            "account_number": "668118244899",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 02:00:26 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "lDu237Zv",
                            "account_number": "668118244900",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 02:00:05 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "AAuVk3QA",
                            "account_number": "689118244901",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 02:00:33 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244898",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "87d73833-7e55-456a-98b3-492791c6e49f",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9804",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e1a12b88-341e-4564-aad8-0c506e8c9282",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9805",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244900",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "a2adf33a-6a0c-485b-9c09-85c400699821",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0003",
                                    "card_status": "N"
                                },
                                {
                                    "id": "950d6a8a-56c6-4f2f-b8a9-4cfb55b983e0",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "0004",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774256,
                    "auth_token": "3d008ca1-af80-4be8-9a18-005ce071d987",
                    "ssn": "201600836",
                    "email": "janis_1717005523@hotmail.com",
                    "password": "password",
                    "first_name": "Rickie",
                    "last_name": "Benito",
                    "date_of_birth": "1975-07-11",
                    "address": "560 Wehner Manor",
                    "zip_code": "30220",
                    "phone": 3733717014,
                    "user_accounts": [
                        {
                            "id": "NguDjxX9",
                            "account_number": "689118244894",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:59:36 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "1QuLg52K",
                            "account_number": "668118244895",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:59:26 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "O9uZ29NE",
                            "account_number": "668118244896",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:59:08 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "03umVKja",
                            "account_number": "689118244897",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:59:35 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244894",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "13c89cc0-320c-4e50-a8bc-ee1879b0a301",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "15a636bf-3473-4994-ac54-bce9e27fa2d1",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9403",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244896",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "5f0819de-645b-4bb4-ae87-9f3fab67ae67",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1f3823bc-51f8-4d56-88c6-6a9a3bf5e942",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774255,
                    "auth_token": "edfac0fd-9053-4284-96ff-f648df1c2628",
                    "ssn": "194308504",
                    "email": "patricia.1717005471@yahoo.com",
                    "password": "password",
                    "first_name": "Kirby",
                    "last_name": "Katharine",
                    "date_of_birth": "1991-04-11",
                    "address": "599 Feeney Station",
                    "zip_code": "92661",
                    "phone": 3779819342,
                    "user_accounts": [
                        {
                            "id": "Yeu0dlol",
                            "account_number": "689118244890",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 10:58:41 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "BDuo1Yx7",
                            "account_number": "668118244891",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 10:58:34 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "kAuw6kdl",
                            "account_number": "668118244892",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 10:58:15 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "a8um3zLm",
                            "account_number": "689118244893",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 10:58:42 AM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244890",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "cd54b3fa-68c1-4ad1-a548-d31dd2c7a2f4",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "11d6a619-35a0-42ac-9a4b-259e02ad978b",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9003",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244892",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "2ab515ac-9a63-4821-97b7-e455c10280da",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "0ca7e844-0d25-4239-8abc-f2485cd2fb39",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "9201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774253,
                    "auth_token": "61cd862c-e979-481e-8d71-e0800536c762",
                    "ssn": "480694102",
                    "email": "1717005415.joe@hotmail.com",
                    "password": "password",
                    "first_name": "Arie",
                    "last_name": "Melvin",
                    "date_of_birth": "1970-12-07",
                    "address": "5201 Selene Squares",
                    "zip_code": "36736",
                    "phone": 3783102439,
                    "user_accounts": [
                        {
                            "id": "LMu46goO",
                            "account_number": "689118244885",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 12:57:50 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "W4uky41B",
                            "account_number": "668118244887",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 12:57:41 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "5WuWd0M4",
                            "account_number": "668118244888",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 12:57:23 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "8YugwbNl",
                            "account_number": "689118244889",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 12:57:50 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244885",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "93499d92-8f2b-4a60-a341-ea08b2d75294",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8505",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e98579ed-881a-443a-a0f4-a01abbf14a91",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8506",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244888",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "7032811b-8395-4f17-bc58-0e4b3a2d8ff1",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8803",
                                    "card_status": "N"
                                },
                                {
                                    "id": "ff200c69-4899-4e7c-831b-e6666c2b5e93",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8804",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774252,
                    "auth_token": "a7d3a53d-d676-4c56-8004-2394413ddba5",
                    "ssn": "606434024",
                    "email": "kyra_1717005362@hotmail.com",
                    "password": "password",
                    "first_name": "Veta",
                    "last_name": "Ned",
                    "date_of_birth": "1978-01-02",
                    "address": "578 Dibbert Fort",
                    "zip_code": "04421",
                    "phone": 7228604700,
                    "user_accounts": [
                        {
                            "id": "e1uodXkN",
                            "account_number": "689118244881",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:56:54 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "3Lu9yPrN",
                            "account_number": "668118244882",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:56:47 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "Qqu7vXnk",
                            "account_number": "668118244883",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:56:26 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "mEuKgzLw",
                            "account_number": "689118244884",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:56:53 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244881",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "c3b6e545-a15f-4777-9ab7-adcb507dd83a",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8103",
                                    "card_status": "N"
                                },
                                {
                                    "id": "b4b39356-a30b-47eb-a0c1-afa50443ebb8",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8104",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244883",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "06bcb497-a209-447a-b6eb-895a6faeba1c",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8301",
                                    "card_status": "N"
                                },
                                {
                                    "id": "fb8fd112-a426-47ef-8ffe-d4ef2903ddb7",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "8302",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774251,
                    "auth_token": "f0fca486-9aa9-44f1-b336-266f6edcdb8b",
                    "ssn": "848727622",
                    "email": "1717005310_chastity@gmail.com",
                    "password": "password",
                    "first_name": "Owen",
                    "last_name": "Vernon",
                    "date_of_birth": "1987-11-03",
                    "address": "91928 Parker Well",
                    "zip_code": "34473",
                    "phone": 2558569687,
                    "user_accounts": [
                        {
                            "id": "wVu0xglZ",
                            "account_number": "689118244877",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:56:02 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "bYunQB1z",
                            "account_number": "668118244878",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:55:53 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "4ouVo97B",
                            "account_number": "668118244879",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:55:35 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "zyu9olxo",
                            "account_number": "689118244880",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:56:02 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244877",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "26c59392-4f9e-4afa-8823-cccfe551010d",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7704",
                                    "card_status": "N"
                                },
                                {
                                    "id": "78110e80-1ccd-4763-b7f0-20c63f4f199e",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7705",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244879",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "ac0d873b-a496-4aa0-a94e-6ae27be68191",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7904",
                                    "card_status": "N"
                                },
                                {
                                    "id": "020eca5d-64ca-4aa8-b712-4a5526311722",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7905",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774250,
                    "auth_token": "6b906dc2-9545-40bd-bce0-4e29cd072f19",
                    "ssn": "651212516",
                    "email": "1717005258.antonia@hotmail.com",
                    "password": "password",
                    "first_name": "Virgina",
                    "last_name": "Jenelle",
                    "date_of_birth": "1983-09-04",
                    "address": "9424 Frida Point",
                    "zip_code": "69210",
                    "phone": 4555984933,
                    "user_accounts": [
                        {
                            "id": "qjuw07zn",
                            "account_number": "689118244873",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 05:55:09 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "dNuLPQE3",
                            "account_number": "668118244874",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 05:55:02 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "KZuZxWE0",
                            "account_number": "668118244875",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 05:54:41 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "78ug7KLr",
                            "account_number": "689118244876",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 05:55:09 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244873",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "2303967d-d826-47ae-9760-3fb71c905063",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7306",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c24c5afb-f3ed-4688-9701-aaf682b1b2d3",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7307",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244875",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "d182c7df-dd65-43f3-a258-102692e833db",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7500",
                                    "card_status": "N"
                                },
                                {
                                    "id": "071d53e9-4566-4259-9102-575905ebf639",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7501",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774249,
                    "auth_token": "941a4eaa-d23a-4100-bd0b-8361c942bb57",
                    "ssn": "579526824",
                    "email": "annette.1717005203@gmail.com",
                    "password": "password",
                    "first_name": "Mary",
                    "last_name": "Marcelo",
                    "date_of_birth": "1971-09-03",
                    "address": "14346 Witting Walk",
                    "zip_code": "04101",
                    "phone": 4005317815,
                    "user_accounts": [
                        {
                            "id": "VbuV9MPX",
                            "account_number": "689118244869",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:54:16 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "g0uO2r9z",
                            "account_number": "668118244870",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:54:09 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "9au9br6l",
                            "account_number": "668118244871",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:53:49 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "y9unKgq0",
                            "account_number": "689118244872",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:54:16 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244869",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "7cacd5e7-a89c-433f-842c-895ee4986c99",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6905",
                                    "card_status": "N"
                                },
                                {
                                    "id": "bcd8d198-29d5-4452-b554-5206305f5c29",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6906",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244871",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "b6431f21-5347-4e48-993e-2efec9581ac5",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7101",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1a67fc06-29f7-4930-a366-b92767b1dfb7",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "7102",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774247,
                    "auth_token": "b3682185-3866-4eed-8a39-a5858575f3c9",
                    "ssn": "521531377",
                    "email": "jerrold.1717005143@gmail.com",
                    "password": "password",
                    "first_name": "Esteban",
                    "last_name": "Maxwell",
                    "date_of_birth": "1973-11-18",
                    "address": "993 Hoppe Parkway",
                    "zip_code": "94501",
                    "phone": 2441602950,
                    "user_accounts": [
                        {
                            "id": "nxuEdVXN",
                            "account_number": "689118244865",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 10:53:22 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "vMuO9gDn",
                            "account_number": "668118244866",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 10:53:15 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "Z3uAKykX",
                            "account_number": "668118244867",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 10:52:54 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "MVu2PN6K",
                            "account_number": "689118244868",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 10:53:22 AM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244865",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "40a28369-8de2-4597-b333-96c8e202e81c",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6503",
                                    "card_status": "N"
                                },
                                {
                                    "id": "61239547-aa31-4f6d-99b9-e2094cb7dd88",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6504",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244867",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "c70939fd-fa3a-4f90-b7bf-d2faf1a79e00",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9d87b191-6d0b-42e6-9dc6-d47f3f72a090",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6701",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774245,
                    "auth_token": "5faece62-932b-4b90-8140-019ad80873de",
                    "ssn": "831853452",
                    "email": "damian_1717005088@hotmail.com",
                    "password": "password",
                    "first_name": "Renda",
                    "last_name": "Simona",
                    "date_of_birth": "1971-06-25",
                    "address": "23295 Pollich Way",
                    "zip_code": "77808",
                    "phone": 4555678833,
                    "user_accounts": [
                        {
                            "id": "xguv2zmP",
                            "account_number": "689118244861",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 12:52:21 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "Pyu7nVoK",
                            "account_number": "668118244862",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 12:52:15 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "jlu4qYLQ",
                            "account_number": "668118244863",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 12:51:54 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "2muE92XX",
                            "account_number": "689118244864",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 12:52:22 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244861",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "10286717-09a3-45c7-9953-bbfc18acc36e",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6103",
                                    "card_status": "N"
                                },
                                {
                                    "id": "188157c8-1283-4d18-9ec3-8b0b21b3ce6d",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6104",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244863",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "ecdeb1ec-b81a-433c-87c6-f822d81dc59b",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6301",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e32bb7a8-730d-44ae-a727-127508745889",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "6302",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774242,
                    "auth_token": "64994e4d-fd18-4c53-90b1-c527cf53be6d",
                    "ssn": "812600433",
                    "email": "marget_1717005031@gmail.com",
                    "password": "password",
                    "first_name": "Carroll",
                    "last_name": "Isiah",
                    "date_of_birth": "1978-08-04",
                    "address": "640 Koss Ferry",
                    "zip_code": "34608",
                    "phone": 4332455585,
                    "user_accounts": [
                        {
                            "id": "XzuOqaNM",
                            "account_number": "689118244857",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:51:28 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "lDu237Qv",
                            "account_number": "668118244858",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:51:18 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "AAuVk3aA",
                            "account_number": "668118244859",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:50:59 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "E6uoXm0k",
                            "account_number": "689118244860",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:51:27 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244857",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "3cd931aa-623f-48af-9783-c56c9d414b74",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5703",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a8879279-4964-40e8-a9e9-6d2a99639e01",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5704",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244859",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "1826895f-0a8c-4e10-bb36-872cd07a78c0",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5901",
                                    "card_status": "N"
                                },
                                {
                                    "id": "68ca8d24-a855-4f0c-a627-287780e2c054",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5902",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774235,
                    "auth_token": "825f05a5-f861-46ea-85d0-e94c6d933d27",
                    "ssn": "388991572",
                    "email": "levi.1717004929@gmail.com",
                    "password": "password",
                    "first_name": "Mario",
                    "last_name": "Gregorio",
                    "date_of_birth": "1972-08-09",
                    "address": "177 Ortiz Inlet",
                    "zip_code": "17320",
                    "phone": 3709797988,
                    "user_accounts": [
                        {
                            "id": "AAuVk3aq",
                            "account_number": "689118244851",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:49:49 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "BDuo1YN7",
                            "account_number": "668118244853",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 01:49:44 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "kAuw6k7l",
                            "account_number": "668118244854",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 01:49:23 PM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "NguDjxP9",
                            "account_number": "689118244855",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 01:49:49 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244851",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "af67f495-f9c1-4ab6-963a-cf919c575e36",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5108",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1ec9bc9e-6549-42d4-9cdd-f397edb31284",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5109",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244854",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "0a9cc4a7-bcee-4088-ade0-4911ef364541",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5403",
                                    "card_status": "N"
                                },
                                {
                                    "id": "2c430290-a790-4f09-9b95-542bee5a1bba",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "5404",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774230,
                    "auth_token": "21e68344-b075-422a-8cf7-6ff7939bddaa",
                    "ssn": "093965509",
                    "email": "1717004879_fred@hotmail.com",
                    "password": "password",
                    "first_name": "Odis",
                    "last_name": "Sharie",
                    "date_of_birth": "1968-11-24",
                    "address": "20403 Nicholas Fields",
                    "zip_code": "79905",
                    "phone": 9624935254,
                    "user_accounts": [
                        {
                            "id": "a8um3zQ3",
                            "account_number": "689118244846",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 11:48:48 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "1QuLg589",
                            "account_number": "668118244847",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 500.0,
                            "balance_updated_at": "2024-05-29 11:48:40 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 500.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "O9uZ29Dk",
                            "account_number": "668118244848",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 11:48:22 AM",
                            "balances": {
                                "display": 500.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "r2ur1BZV",
                            "account_number": "689118244850",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 11:48:48 AM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244846",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "34bd5563-643b-4d96-87cf-46559a2ab3af",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4601",
                                    "card_status": "N"
                                },
                                {
                                    "id": "60084977-8b81-4d1a-a64d-ae81fc805528",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4602",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244848",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "71b1cc27-72ae-41fb-bc0b-47a4afe5036d",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6ac0e299-95e8-42f5-a0d7-c9f525903625",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                },
                {
                    "user_id": 20774226,
                    "auth_token": "e3ca20c5-3825-4eb6-9176-616cd36a5681",
                    "ssn": "760374147",
                    "email": "sima_1717004830@gmail.com",
                    "password": "password",
                    "first_name": "Marcus",
                    "last_name": "Melissa",
                    "date_of_birth": "1984-09-05",
                    "address": "382 Maynard Highway",
                    "zip_code": "64671",
                    "phone": 3788384722,
                    "user_accounts": [
                        {
                            "id": "o6u4y5LO",
                            "account_number": "689118244841",
                            "account_type": "checking",
                            "routing_number": "103113357",
                            "balance": 1000.0,
                            "balance_updated_at": "2024-05-29 12:47:57 PM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "5WuWd0ND",
                            "account_number": "668118244842",
                            "account_type": "security_deposit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 12:47:36 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "8Yugwbq2",
                            "account_number": "668118244843",
                            "account_type": "secured_credit",
                            "routing_number": "103113357",
                            "balance": 0.0,
                            "balance_updated_at": "2024-05-29 12:47:35 PM",
                            "balances": {
                                "display": 0.0,
                                "balance": 0.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        },
                        {
                            "id": "BDuo1Yvz",
                            "account_number": "689118244844",
                            "account_type": "savings",
                            "routing_number": "103113357",
                            "balance": 120.0,
                            "balance_updated_at": "2024-05-29 12:47:58 PM",
                            "balances": {
                                "display": 120.0,
                                "balance": 120.0
                            },
                            "bank_name": "STRIDE",
                            "active": true
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "689118244841",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a261122d-49a0-4143-b1b5-f4c444e05fd6",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4104",
                                    "card_status": "N"
                                },
                                {
                                    "id": "faba7a80-7b7a-4a8d-bc5e-0f31cf9b523a",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4105",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "668118244843",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "6479cf76-6cac-4f74-bee0-4632fb9186cc",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4304",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a4f2c51c-7bee-468b-b3e2-dacc2d0a6024",
                                    "expiry_date": "2028-05-29",
                                    "card_number": "4305",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "cohort_id": "spotme_on_cb_new_members_variant_2",
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/868500073285800779"
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

print("\nSSNs:")
for ssn in ssns:
    print(ssn)
    

