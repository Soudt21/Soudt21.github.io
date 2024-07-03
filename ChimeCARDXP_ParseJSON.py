import json

# Note for whatever reason you may need to update the errors to "No errors encountered." 

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-07-03 15:16:50 UTC",
                "state": "20/20 users created.",
                "errorCount": 0,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 21258836,
                    "auth_token": "a1afb097-7627-4b35-9800-92082e46638b",
                    "ssn": "720867041",
                    "email": "Walker.1720019997+cb1@chime.com",
                    "password": "password",
                    "first_name": "Marvella",
                    "last_name": "Roma",
                    "date_of_birth": "1983-06-02",
                    "address": "448 Terrie Greens",
                    "zip_code": "24579",
                    "phone": 3754905786,
                    "user_accounts": [
                        {
                            "id": "8YugnjQk",
                            "account_number": "766018775880",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:20:03 AM",
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
                            "prn": "766018775880",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "d9db1e3c-fe86-4005-8341-0a5d6f879fa9",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "ae668f09-672a-4279-82fd-96a83853fdae",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "marvellaroma1"
                },
                {
                    "user_id": 21258835,
                    "auth_token": "8f861d3d-25fe-4dee-a89a-a6ea3af37f55",
                    "ssn": "023663306",
                    "email": "Jamey.1720019987+cb1@chime.com",
                    "password": "password",
                    "first_name": "Esther",
                    "last_name": "Greg",
                    "date_of_birth": "1978-01-21",
                    "address": "757 Lynsey Springs",
                    "zip_code": "42629",
                    "phone": 9695528251,
                    "user_accounts": [
                        {
                            "id": "5WuW7gXE",
                            "account_number": "766018775879",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 03:19:53 PM",
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
                            "prn": "766018775879",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "48a45ff1-b36d-40fe-bf40-0b403df49d90",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "dfa27f5e-f5b7-45ed-9de4-870f276bb1c6",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "esthergreg1"
                },
                {
                    "user_id": 21258834,
                    "auth_token": "de4e5cee-61de-4632-b5c1-076b019ed75f",
                    "ssn": "629504572",
                    "email": "Hipolito.1720019977+cb1@chime.com",
                    "password": "password",
                    "first_name": "Lucio",
                    "last_name": "Kasi",
                    "date_of_birth": "1969-08-15",
                    "address": "6887 Lang Tunnel",
                    "zip_code": "44442",
                    "phone": 3747991568,
                    "user_accounts": [
                        {
                            "id": "LMu4rQnM",
                            "account_number": "766018775878",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:19:43 AM",
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
                            "prn": "766018775878",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "3152574c-a385-4155-92dc-dd33320fb405",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7802",
                                    "card_status": "N"
                                },
                                {
                                    "id": "b4c8caa1-bdf2-4920-b2ba-4628afd8449e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7803",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "luciokasi1"
                },
                {
                    "user_id": 21258831,
                    "auth_token": "f42c30b0-f711-49e3-a5cb-fa906873f1c2",
                    "ssn": "323951142",
                    "email": "Krystina.1720019967+cb1@chime.com",
                    "password": "password",
                    "first_name": "Lisandra",
                    "last_name": "Kory",
                    "date_of_birth": "1984-03-11",
                    "address": "21486 Freda Shoal",
                    "zip_code": "03234",
                    "phone": 3005484142,
                    "user_accounts": [
                        {
                            "id": "zyu94adn",
                            "account_number": "766018775875",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:19:33 AM",
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
                            "prn": "766018775875",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "17cea2a0-a1c8-4b62-b757-70a55c4f54e6",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "302b04a3-e31d-4b71-b3a6-5a8900f952d4",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "lisandrakory"
                },
                {
                    "user_id": 21258830,
                    "auth_token": "7d2a8a2a-04d0-48f5-b17e-8284e20796b6",
                    "ssn": "634972031",
                    "email": "Leo.1720019958+cb1@chime.com",
                    "password": "password",
                    "first_name": "Sydney",
                    "last_name": "Shayne",
                    "date_of_birth": "1977-11-25",
                    "address": "823 Von Way",
                    "zip_code": "20861",
                    "phone": 3782764175,
                    "user_accounts": [
                        {
                            "id": "4ouV0a86",
                            "account_number": "766018775874",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:19:23 AM",
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
                            "prn": "766018775874",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "85b78e4e-0e43-4a74-87f5-1aeec26cf7c4",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "48f66c13-1737-4627-a7d9-b039ef46f131",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7403",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "sydneyshayne2"
                },
                {
                    "user_id": 21258829,
                    "auth_token": "68a606a2-cdff-4305-b8fd-22c47b09b626",
                    "ssn": "221104917",
                    "email": "Janey.1720019948+cb1@chime.com",
                    "password": "password",
                    "first_name": "Jay",
                    "last_name": "Sharyl",
                    "date_of_birth": "1989-06-21",
                    "address": "1687 Alison Spurs",
                    "zip_code": "24924",
                    "phone": 3725406121,
                    "user_accounts": [
                        {
                            "id": "bYun8Z2V",
                            "account_number": "766018775873",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:19:14 AM",
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
                            "prn": "766018775873",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8c69341f-a6ed-4f1d-9f0b-d0713cfb9c93",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7300",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e1c6e8da-1890-457a-bc35-80d223159c7b",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7301",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jaysharyl2"
                },
                {
                    "user_id": 21258827,
                    "auth_token": "6bffe4c7-4207-4b96-9443-30fdb63cb856",
                    "ssn": "849442816",
                    "email": "Penny.1720019938+cb1@chime.com",
                    "password": "password",
                    "first_name": "Sol",
                    "last_name": "Lawrence",
                    "date_of_birth": "1987-07-10",
                    "address": "1427 Reichel Grove",
                    "zip_code": "81149",
                    "phone": 3115689238,
                    "user_accounts": [
                        {
                            "id": "78ugVbmg",
                            "account_number": "766018775872",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 09:19:04 AM",
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
                            "prn": "766018775872",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "119fe2c8-830d-4ac4-a575-d24c34463b0f",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "3180ca56-b72f-43a9-874d-24d5a47330e2",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "sollawrence"
                },
                {
                    "user_id": 21258826,
                    "auth_token": "633a1f9a-5fd6-4670-aa82-0139b93d355c",
                    "ssn": "469554329",
                    "email": "Huey.1720019928+cb1@chime.com",
                    "password": "password",
                    "first_name": "Mei",
                    "last_name": "Jodie",
                    "date_of_birth": "1974-04-14",
                    "address": "16771 Cristina Flats",
                    "zip_code": "44112",
                    "phone": 3708442659,
                    "user_accounts": [
                        {
                            "id": "KZuZQ73w",
                            "account_number": "766018775871",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:18:54 AM",
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
                            "prn": "766018775871",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "3991ff42-3ddc-4193-9c9d-cf2eb5b444e0",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9181c51a-9598-4e6c-919b-d3d6ae816f11",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "meijodie"
                },
                {
                    "user_id": 21258825,
                    "auth_token": "12833cde-7867-4ac4-ad80-cdb036a89af4",
                    "ssn": "773065957",
                    "email": "Heath.1720019919+cb1@chime.com",
                    "password": "password",
                    "first_name": "Lon",
                    "last_name": "Jarod",
                    "date_of_birth": "1962-04-16",
                    "address": "3333 Rachell Meadows",
                    "zip_code": "79423",
                    "phone": 7443281266,
                    "user_accounts": [
                        {
                            "id": "dNuLbjvB",
                            "account_number": "766018775870",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:18:44 AM",
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
                            "prn": "766018775870",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e96983c2-fde9-41ab-8973-26cb19fb7e2e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "fc3bffc1-d97d-450e-a7c3-38c9243aec06",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "lonjarod"
                },
                {
                    "user_id": 21258824,
                    "auth_token": "d8b7f7ed-4078-4d0b-98aa-a3cdf65b1ee5",
                    "ssn": "401956683",
                    "email": "Carlyn.1720019908+cb1@chime.com",
                    "password": "password",
                    "first_name": "Herma",
                    "last_name": "Walker",
                    "date_of_birth": "2005-04-15",
                    "address": "73336 Ezequiel Road",
                    "zip_code": "68719",
                    "phone": 9558467846,
                    "user_accounts": [
                        {
                            "id": "qjuwYO67",
                            "account_number": "766018775869",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 03:18:34 PM",
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
                            "prn": "766018775869",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "942b41b5-d787-4cc7-aa14-bd4c6f9b6d8e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "8685d09c-af67-4876-983e-de1a4e8363cc",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "hermawalker9"
                },
                {
                    "user_id": 21258823,
                    "auth_token": "d8da2761-b9a9-47eb-a452-2ff100b88925",
                    "ssn": "863480294",
                    "email": "Rosendo.1720019898+cb1@chime.com",
                    "password": "password",
                    "first_name": "Hai",
                    "last_name": "Kenia",
                    "date_of_birth": "2003-03-15",
                    "address": "5034 Kory Hill",
                    "zip_code": "61453",
                    "phone": 4558823386,
                    "user_accounts": [
                        {
                            "id": "y9unBxDb",
                            "account_number": "766018775868",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:18:24 AM",
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
                            "prn": "766018775868",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b79f16cf-3799-4599-9076-775c231e6431",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a809ad61-ac45-447d-b07d-944c082f9462",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "haikenia"
                },
                {
                    "user_id": 21258822,
                    "auth_token": "5a4ac781-2d9c-4064-9678-5b4b014dc0de",
                    "ssn": "013604886",
                    "email": "Effie.1720019888+cb1@chime.com",
                    "password": "password",
                    "first_name": "Lin",
                    "last_name": "Gillian",
                    "date_of_birth": "1960-09-13",
                    "address": "198 Legros Burg",
                    "zip_code": "72952",
                    "phone": 3330362118,
                    "user_accounts": [
                        {
                            "id": "9au9g0kq",
                            "account_number": "766018775867",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:18:14 AM",
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
                            "prn": "766018775867",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "cb5c039d-5c64-4d98-9170-9ab7a8857a3a",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6702",
                                    "card_status": "N"
                                },
                                {
                                    "id": "dafe4fd9-6923-4f8c-a5ec-37ba0c6cff00",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6703",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "lingillian"
                },
                {
                    "user_id": 21258821,
                    "auth_token": "ab7926fc-7b91-4c97-8c79-e3f6105d4f28",
                    "ssn": "146903164",
                    "email": "Shonda.1720019879+cb1@chime.com",
                    "password": "password",
                    "first_name": "Vicky",
                    "last_name": "Suellen",
                    "date_of_birth": "1960-08-14",
                    "address": "2652 Mann Glens",
                    "zip_code": "35118",
                    "phone": 9678415771,
                    "user_accounts": [
                        {
                            "id": "g0uOjkej",
                            "account_number": "766018775866",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:18:05 AM",
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
                            "prn": "766018775866",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "61da312a-9d5c-4531-ab72-aee0f505fbad",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "98302c25-0ebc-4aec-97a5-f5e707e45342",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "vickysuellen"
                },
                {
                    "user_id": 21258820,
                    "auth_token": "f606f79d-a90d-457f-85a1-e7e99ed3c8b9",
                    "ssn": "802352600",
                    "email": "Hollis.1720019869+cb1@chime.com",
                    "password": "password",
                    "first_name": "Mikki",
                    "last_name": "Cari",
                    "date_of_birth": "2001-09-26",
                    "address": "3768 Bosco Inlet",
                    "zip_code": "97233",
                    "phone": 3113282298,
                    "user_accounts": [
                        {
                            "id": "VbuVAkQm",
                            "account_number": "766018775865",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 08:17:55 AM",
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
                            "prn": "766018775865",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "dc1e6672-7265-414f-99d4-7838556c3351",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6500",
                                    "card_status": "N"
                                },
                                {
                                    "id": "273c04b1-d2c1-4643-92c2-57a406e73f20",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6501",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "mikkicari"
                },
                {
                    "user_id": 21258818,
                    "auth_token": "3155c578-f054-4c1c-8fbb-007d498dc56e",
                    "ssn": "518922838",
                    "email": "Madalyn.1720019859+cb1@chime.com",
                    "password": "password",
                    "first_name": "Toney",
                    "last_name": "Hung",
                    "date_of_birth": "1965-01-01",
                    "address": "1450 Schultz Coves",
                    "zip_code": "61080",
                    "phone": 3772591908,
                    "user_accounts": [
                        {
                            "id": "jlu4ywEq",
                            "account_number": "766018775863",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:17:45 AM",
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
                            "prn": "766018775863",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "2f1af580-32de-43c1-89de-b5c93de03aee",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6302",
                                    "card_status": "N"
                                },
                                {
                                    "id": "932adac6-0a90-4b1d-9f3d-704a5d641e82",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6303",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "toneyhung1"
                },
                {
                    "user_id": 21258816,
                    "auth_token": "59d2aa6e-9dfc-49c3-89e1-ecc9b5407e7b",
                    "ssn": "258444077",
                    "email": "Denny.1720019850+cb1@chime.com",
                    "password": "password",
                    "first_name": "Leah",
                    "last_name": "Richard",
                    "date_of_birth": "1980-02-21",
                    "address": "34751 Apryl Road",
                    "zip_code": "12770",
                    "phone": 3331978140,
                    "user_accounts": [
                        {
                            "id": "65u2wnNE",
                            "account_number": "766018775861",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:17:36 AM",
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
                            "prn": "766018775861",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "f76332ae-405e-4186-90a8-638cd714ea0c",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "ed9b446b-e953-4fde-b8d1-30c36712579e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "leahrichard2"
                },
                {
                    "user_id": 21258815,
                    "auth_token": "3499b53a-6c4b-4a4c-94c3-54e25eba72a5",
                    "ssn": "801763926",
                    "email": "Hiram.1720019840+cb1@chime.com",
                    "password": "password",
                    "first_name": "Tatiana",
                    "last_name": "Gerry",
                    "date_of_birth": "1993-01-28",
                    "address": "77292 Cyril Lane",
                    "zip_code": "01949",
                    "phone": 9678798299,
                    "user_accounts": [
                        {
                            "id": "xguvnEOr",
                            "account_number": "766018775860",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:17:25 AM",
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
                            "prn": "766018775860",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "6c364dcc-47b1-4010-9b5b-0059967fa7a3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f5f8a6d8-e2ec-4ce8-bff4-a7f74e10bf63",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "tatianagerry1"
                },
                {
                    "user_id": 21258813,
                    "auth_token": "6b703f67-a7ee-47ad-9e89-f348cc096cec",
                    "ssn": "130370912",
                    "email": "Jason.1720019830+cb1@chime.com",
                    "password": "password",
                    "first_name": "Roman",
                    "last_name": "Tom",
                    "date_of_birth": "1987-09-15",
                    "address": "5398 Weldon Extension",
                    "zip_code": "39341",
                    "phone": 9551258599,
                    "user_accounts": [
                        {
                            "id": "DxuYNaQq",
                            "account_number": "766018775859",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:17:16 AM",
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
                            "prn": "766018775859",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "d3c246c1-2f92-48a4-9983-3bc6942d9a68",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c797832e-6269-4418-8d71-373294612d9d",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "romantom1"
                },
                {
                    "user_id": 21258811,
                    "auth_token": "659dce42-2f8f-4d5e-a50c-a511eee79f28",
                    "ssn": "448911543",
                    "email": "Shelli.1720019821+cb1@chime.com",
                    "password": "password",
                    "first_name": "Eldon",
                    "last_name": "Irvin",
                    "date_of_birth": "1990-01-14",
                    "address": "921 Nathanael Rue",
                    "zip_code": "84086",
                    "phone": 3774234204,
                    "user_accounts": [
                        {
                            "id": "03umqElg",
                            "account_number": "766018775858",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 09:17:06 AM",
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
                            "prn": "766018775858",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8a611627-ae1e-43b5-81bd-3026ba2b7ea9",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5802",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f1fc879f-5afd-44d0-8d81-f4933980c1fc",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5803",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "eldonirvin"
                },
                {
                    "user_id": 21258808,
                    "auth_token": "2c2eef1c-b33e-434e-909b-3caeedf9dcbc",
                    "ssn": "698336800",
                    "email": "Marisha.1720019810+cb1@chime.com",
                    "password": "password",
                    "first_name": "Felix",
                    "last_name": "Lanita",
                    "date_of_birth": "1990-12-29",
                    "address": "66187 Will Parkway",
                    "zip_code": "88265",
                    "phone": 6666302373,
                    "user_accounts": [
                        {
                            "id": "NguDY4EE",
                            "account_number": "766018775855",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 09:16:57 AM",
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
                            "prn": "766018775855",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "665bf8df-8eef-446c-aa30-76e77a038833",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5500",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f941b5b0-3ddc-45d1-aba5-89ca2f2a7283",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5501",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "felixlanita"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/515598619885056120"
}
'''

# Assuming the JSON is stored in a variable named 'json_data'
data = json.loads(json_data)

# Extract emails and SSNs
emails = [user['email'] for user in data['data']['getBulkUsers']['users']]
ssns = [user['ssn'] for user in data['data']['getBulkUsers']['users']]
userIds = [user['user_id'] for user in data['data']['getBulkUsers']['users']]

print("Emails:")
for email in emails:
    print(email)

print("\nSSNs:")
for ssn in ssns:
    print(ssn)


