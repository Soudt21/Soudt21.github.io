import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-07-03 15:34:56 UTC",
                "state": "20/20 users created.",
                "errorCount": 0,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 21259220,
                    "auth_token": "ba23ba1e-3f38-491a-b5dd-a54b6681be04",
                    "ssn": "401454120",
                    "email": "cherly_1720021244@yahoo.com",
                    "password": "password",
                    "lending_id": "0b4117e5-a6cc-41e1-a6c4-996afec7aa02",
                    "first_name": "Noma",
                    "last_name": "Noelia",
                    "date_of_birth": "1989-10-12",
                    "address": "789 Kara Union",
                    "zip_code": "64784",
                    "phone": 9629591885,
                    "user_accounts": [
                        {
                            "id": "03umqEOO",
                            "account_number": "766018776295",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:40:51 AM",
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
                            "prn": "766018776295",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "f26279d8-c07a-41da-899b-380af988c812",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "8043004e-8d36-4483-abc6-fbc18a2718e3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "nomanoelia"
                },
                {
                    "user_id": 21259219,
                    "auth_token": "9cc4fc24-ff91-4108-b047-ab0884330a64",
                    "ssn": "010015669",
                    "email": "1720021226.minnie@hotmail.com",
                    "password": "password",
                    "lending_id": "8edf644a-9a27-4119-ad97-1d7572835742",
                    "first_name": "Wade",
                    "last_name": "Martha",
                    "date_of_birth": "1988-07-28",
                    "address": "5819 Winifred Spurs",
                    "zip_code": "95023",
                    "phone": 9505997999,
                    "user_accounts": [
                        {
                            "id": "O9uZm4V1",
                            "account_number": "766018776294",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 08:40:32 AM",
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
                            "prn": "766018776294",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "bcece63b-672e-4634-b3ac-b6f36bf6f152",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "58765bf1-e644-45fe-be17-afe9e06b7bb3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "wademartha"
                },
                {
                    "user_id": 21259218,
                    "auth_token": "ab226d29-43af-4edb-803b-ec3e985dfb96",
                    "ssn": "394295199",
                    "email": "1720021206.lala@gmail.com",
                    "password": "password",
                    "lending_id": "564a714a-42f0-4f8c-ba32-fe108cdce98c",
                    "first_name": "Kimbra",
                    "last_name": "Vicki",
                    "date_of_birth": "1975-05-03",
                    "address": "950 Sergio Summit",
                    "zip_code": "61241",
                    "phone": 3789040608,
                    "user_accounts": [
                        {
                            "id": "1QuLxyP0",
                            "account_number": "766018776293",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:40:12 AM",
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
                            "prn": "766018776293",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "3e19f648-adcc-4181-bf51-d7ea34ad4e9e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9300",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a7948d6b-4cb2-4731-a790-8208439a6edf",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9301",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "kimbravicki"
                },
                {
                    "user_id": 21259217,
                    "auth_token": "6251907e-52e4-450c-986d-119b0bd06b22",
                    "ssn": "408126652",
                    "email": "1720021189.anh@yahoo.com",
                    "password": "password",
                    "lending_id": "6f20d622-f4c5-4b0a-9824-4e85272059bd",
                    "first_name": "Joan",
                    "last_name": "Brant",
                    "date_of_birth": "1993-09-14",
                    "address": "1850 Roberts Plains",
                    "zip_code": "23502",
                    "phone": 2003891569,
                    "user_accounts": [
                        {
                            "id": "NguDY4Aa",
                            "account_number": "766018776292",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 11:40:05 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776292",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "776de111-ad23-4bfe-88e2-994e175e8741",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "9ae743d0-2d51-4acf-afef-14a9bc36869a",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "joanbrant"
                },
                {
                    "user_id": 21259215,
                    "auth_token": "22503768-1f62-43db-bb4d-30193b8ea9a6",
                    "ssn": "720816203",
                    "email": "jacquelyne_1720021170@yahoo.com",
                    "password": "password",
                    "lending_id": "cfb1edd3-98e6-40da-a712-adb4891a3214",
                    "first_name": "Krystyna",
                    "last_name": "Ed",
                    "date_of_birth": "1973-02-21",
                    "address": "2108 Veum Throughway",
                    "zip_code": "68856",
                    "phone": 9228841822,
                    "user_accounts": [
                        {
                            "id": "a8umve2K",
                            "account_number": "766018776291",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 03:39:36 PM",
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
                            "prn": "766018776291",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "0efb8d53-8a4e-444b-b0f6-0a20b2a970c0",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1c00c4c1-b685-4a1e-bec9-12fad56be0ee",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "krystynaed"
                },
                {
                    "user_id": 21259213,
                    "auth_token": "fe02ed7c-9061-4c91-b130-55275be31390",
                    "ssn": "224908112",
                    "email": "lynn.1720021151@yahoo.com",
                    "password": "password",
                    "lending_id": "56d922b0-467b-4e5d-9c60-d6fbeb33c476",
                    "first_name": "Jacob",
                    "last_name": "Trista",
                    "date_of_birth": "2002-01-03",
                    "address": "608 Veum Station",
                    "zip_code": "20037",
                    "phone": 4444624983,
                    "user_accounts": [
                        {
                            "id": "BDuoW4z5",
                            "account_number": "766018776290",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 08:39:30 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776290",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b849c778-0808-42f3-8159-b559d8718de9",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1b96044d-d0e6-4e66-96ee-a79079cc79eb",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jacobtrista"
                },
                {
                    "user_id": 21259212,
                    "auth_token": "87a40c38-ba48-4f19-8f54-cc26950e9652",
                    "ssn": "336244154",
                    "email": "willia.1720021132@gmail.com",
                    "password": "password",
                    "lending_id": "976d6113-393d-4073-862f-663bb0cd032e",
                    "first_name": "Richelle",
                    "last_name": "Akilah",
                    "date_of_birth": "1969-09-03",
                    "address": "3615 Littel Drive",
                    "zip_code": "46290",
                    "phone": 3761828710,
                    "user_accounts": [
                        {
                            "id": "Yeu07egv",
                            "account_number": "766018776289",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 11:39:11 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776289",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "1d6b85ae-1efc-49f1-a6c3-5662707d9497",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8900",
                                    "card_status": "N"
                                },
                                {
                                    "id": "01ee9e95-fd90-4a86-91ba-ab70e81270d1",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8901",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "richelleakilah"
                },
                {
                    "user_id": 21259211,
                    "auth_token": "6166e249-a623-495e-800f-db7ff5760b96",
                    "ssn": "831604099",
                    "email": "1720021114_leonor@hotmail.com",
                    "password": "password",
                    "lending_id": "931fdeee-f19f-4486-b463-39e88e2789a7",
                    "first_name": "Myra",
                    "last_name": "Glen",
                    "date_of_birth": "1975-11-23",
                    "address": "34719 Kemmer Greens",
                    "zip_code": "50044",
                    "phone": 3719661851,
                    "user_accounts": [
                        {
                            "id": "8Yugnj0W",
                            "account_number": "766018776288",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 10:38:52 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776288",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "57498dee-fc31-48eb-98f0-0f5e42074c04",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1db1fb83-5688-4644-abea-1f1fbc875cd3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "myraglen1"
                },
                {
                    "user_id": 21259210,
                    "auth_token": "3ea5e440-841a-4344-915d-368b9d38dba9",
                    "ssn": "152853044",
                    "email": "al_1720021096@yahoo.com",
                    "password": "password",
                    "lending_id": "68d0bbfb-8603-452f-977b-50944a5b83ad",
                    "first_name": "Kay",
                    "last_name": "Reba",
                    "date_of_birth": "1960-05-03",
                    "address": "9742 Tromp Corner",
                    "zip_code": "26164",
                    "phone": 3440891198,
                    "user_accounts": [
                        {
                            "id": "5WuW7gzZ",
                            "account_number": "766018776287",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 11:38:34 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776287",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "12126b67-c400-4d8b-86c1-5efb93c3495f",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "bc85ad2e-51d2-4acb-995a-58db25827683",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8701",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "kayreba"
                },
                {
                    "user_id": 21259209,
                    "auth_token": "a3defd41-7d12-4ac8-bce8-a8518170cf2b",
                    "ssn": "698436539",
                    "email": "graciela_1720021078@hotmail.com",
                    "password": "password",
                    "lending_id": "1e28354c-468c-46ea-a77a-52536a2ac8f7",
                    "first_name": "Jaqueline",
                    "last_name": "Toby",
                    "date_of_birth": "2004-05-11",
                    "address": "50904 Borer Creek",
                    "zip_code": "50312",
                    "phone": 3771457675,
                    "user_accounts": [
                        {
                            "id": "o6u4gNoW",
                            "account_number": "766018776285",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 10:38:15 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776285",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "35530b6a-bf18-4865-b3b0-ce3318ec436a",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1eabca34-d1c2-4a1c-a943-8af215a88b69",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "jaquelinetoby"
                },
                {
                    "user_id": 21259205,
                    "auth_token": "d9059962-9744-4a7a-91cf-dc2040c50f6c",
                    "ssn": "857946226",
                    "email": "1720021060.lida@yahoo.com",
                    "password": "password",
                    "lending_id": "298f2a3c-14d8-47d8-9bf0-a187781d0221",
                    "first_name": "Stewart",
                    "last_name": "Renita",
                    "date_of_birth": "2006-04-22",
                    "address": "80912 Corwin Well",
                    "zip_code": "08733",
                    "phone": 3333277502,
                    "user_accounts": [
                        {
                            "id": "3Lu9gjY5",
                            "account_number": "766018776281",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 09:37:46 AM",
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
                            "prn": "766018776281",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8983e01e-a862-4adf-9f76-893a4fe28576",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "956defad-b8ee-49e4-ad28-b293919d50de",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "stewartrenita"
                },
                {
                    "user_id": 21259198,
                    "auth_token": "1d58a829-d123-4a1f-9ddb-5a037a29244b",
                    "ssn": "537743876",
                    "email": "1720021043.sonia@gmail.com",
                    "password": "password",
                    "lending_id": "e2d6bfbb-febe-41f9-a881-6b654e48fbb4",
                    "first_name": "Garry",
                    "last_name": "Yuko",
                    "date_of_birth": "1965-04-29",
                    "address": "4354 Agatha Junction",
                    "zip_code": "48768",
                    "phone": 3759486376,
                    "user_accounts": [
                        {
                            "id": "qjuwYOrD",
                            "account_number": "766018776272",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 03:37:40 PM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776272",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "182be746-4ebe-4915-891d-03bd0646d0e1",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "d088d8f6-fb8b-4bee-8132-40930b551f0d",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "garryyuko"
                },
                {
                    "user_id": 21259188,
                    "auth_token": "7b15ea9b-4ffa-45d4-817d-30c25c736e9f",
                    "ssn": "808711828",
                    "email": "elden.1720021025@hotmail.com",
                    "password": "password",
                    "lending_id": "224e4c86-9ebc-4b4c-b7e4-4754f136e930",
                    "first_name": "Matt",
                    "last_name": "Rusty",
                    "date_of_birth": "1996-04-28",
                    "address": "748 Schmeler Wall",
                    "zip_code": "50582",
                    "phone": 3668738749,
                    "user_accounts": [
                        {
                            "id": "jlu4yw6O",
                            "account_number": "766018776263",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:37:11 AM",
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
                            "prn": "766018776263",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "39cb109a-4393-4cee-8e6b-c071454129f5",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6302",
                                    "card_status": "N"
                                },
                                {
                                    "id": "150dd03e-59b5-4385-b36b-16b98a8a10be",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "6303",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "mattrusty"
                },
                {
                    "user_id": 21259175,
                    "auth_token": "c73003b1-c9d5-4de8-b513-5d3d3b47b350",
                    "ssn": "643355796",
                    "email": "1720021008_latosha@hotmail.com",
                    "password": "password",
                    "lending_id": "7ffc35c1-cf05-4016-ae74-0620d76b37b6",
                    "first_name": "Eric",
                    "last_name": "Shelby",
                    "date_of_birth": "1967-04-18",
                    "address": "4996 Lorenzo Creek",
                    "zip_code": "02839",
                    "phone": 9229693623,
                    "user_accounts": [
                        {
                            "id": "BDuoW4A5",
                            "account_number": "766018776246",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 11:36:54 AM",
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
                            "prn": "766018776246",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "c50c691f-4168-42b1-9473-b04d32a15089",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "4602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "b04dea34-03d0-4d2b-8844-655c695ff041",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "4603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "ericshelby1"
                },
                {
                    "user_id": 21259151,
                    "auth_token": "a723ac25-fa69-4b7a-9611-9dc3a4f92dff",
                    "ssn": "313418948",
                    "email": "anibal_1720020990@hotmail.com",
                    "password": "password",
                    "lending_id": "3d06d949-1e0e-450b-91f3-de49e13297f0",
                    "first_name": "Sandy",
                    "last_name": "Nathaniel",
                    "date_of_birth": "1978-04-01",
                    "address": "92661 Perry Drive",
                    "zip_code": "52339",
                    "phone": 3889885460,
                    "user_accounts": [
                        {
                            "id": "g0uOjkKE",
                            "account_number": "766018776226",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:36:36 AM",
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
                            "prn": "766018776226",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e9682b3b-0497-4c5d-aeab-1ef5b6c84db1",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "2600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1c3f98dc-a024-405d-80f7-c3142abbdf5c",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "2601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "sandynathaniel2"
                },
                {
                    "user_id": 21259131,
                    "auth_token": "d6a02d54-4877-4dc4-aa61-4114aca231c6",
                    "ssn": "780985131",
                    "email": "1720020972.daron@yahoo.com",
                    "password": "password",
                    "lending_id": "a1bb5459-1f06-4f4c-a2f3-6f47be27e281",
                    "first_name": "Karine",
                    "last_name": "Nigel",
                    "date_of_birth": "1989-03-03",
                    "address": "129 Schultz Hill",
                    "zip_code": "83272",
                    "phone": 4447870855,
                    "user_accounts": [
                        {
                            "id": "kAuwAjEV",
                            "account_number": "766018776205",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 09:36:30 AM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776205",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "f541aae6-e15c-4000-8fd1-cf8b096b077d",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "0502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5e9a67d8-4f43-417e-8895-b2e2cf1e4244",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "0503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "karinenigel"
                },
                {
                    "user_id": 21259115,
                    "auth_token": "4ba889f2-d949-4b5f-a539-54a9dd3a6588",
                    "ssn": "697236857",
                    "email": "estefana_1720020955@gmail.com",
                    "password": "password",
                    "lending_id": "988a0926-934a-4e2e-ad2a-3f8d2d7fdab8",
                    "first_name": "Courtney",
                    "last_name": "Albert",
                    "date_of_birth": "1999-02-18",
                    "address": "78283 Mohr Corner",
                    "zip_code": "60145",
                    "phone": 3446939072,
                    "user_accounts": [
                        {
                            "id": "LMu4rQZ2",
                            "account_number": "766018776186",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:36:00 AM",
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
                            "prn": "766018776186",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b671989c-770b-44a5-b318-72b8791acc1e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "77df673d-c881-469a-95dd-9ffe653263bf",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "courtneyalbert1"
                },
                {
                    "user_id": 21259101,
                    "auth_token": "c4bbfaf1-2369-4bcd-8cf8-f3543ae1e96e",
                    "ssn": "414324983",
                    "email": "shawn_1720020938@yahoo.com",
                    "password": "password",
                    "lending_id": "6c50b185-426c-4dbe-8786-039411bcf240",
                    "first_name": "Lucille",
                    "last_name": "Adalberto",
                    "date_of_birth": "1976-03-01",
                    "address": "66969 Weissnat Ports",
                    "zip_code": "59038",
                    "phone": 9610708022,
                    "user_accounts": [
                        {
                            "id": "9au9g0PO",
                            "account_number": "766018776172",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 09:35:44 AM",
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
                            "prn": "766018776172",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "70886287-616d-43cf-bf13-f9bb5123ff0c",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5e0030af-29c0-4b50-ad50-62e0ff1ff11e",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "lucilleadalberto"
                },
                {
                    "user_id": 21259084,
                    "auth_token": "73d3cfde-35fc-4bf6-89dc-4d7b9915a020",
                    "ssn": "437700157",
                    "email": "tanner_1720020920@gmail.com",
                    "password": "password",
                    "lending_id": "431d3aa8-ad0c-4de9-94b0-d1285d4e1c9e",
                    "first_name": "Corene",
                    "last_name": "Penney",
                    "date_of_birth": "1966-05-15",
                    "address": "54454 Dominique Mount",
                    "zip_code": "68982",
                    "phone": 2115257665,
                    "user_accounts": [
                        {
                            "id": "NguDY4a6",
                            "account_number": "766018776152",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 234.0,
                            "balance_updated_at": "2024-07-03 03:35:38 PM",
                            "balances": {
                                "display": 234.0,
                                "balance": 234.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776152",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "ea040cc4-6d15-424f-91de-007d178039af",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "14eefae4-9eae-4be2-a367-6daa9a0dbfb8",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "5201",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "corenepenney"
                },
                {
                    "user_id": 21259066,
                    "auth_token": "d48159e9-a467-4954-b99e-f5c372513984",
                    "ssn": "129894323",
                    "email": "simona_1720020900@hotmail.com",
                    "password": "password",
                    "lending_id": "c50186b1-e051-4914-9523-266eeb183da2",
                    "first_name": "Lyndon",
                    "last_name": "Fidel",
                    "date_of_birth": "1972-03-05",
                    "address": "24904 Luann Street",
                    "zip_code": "79545",
                    "phone": 9503123080,
                    "user_accounts": [
                        {
                            "id": "KZuZQ7MQ",
                            "account_number": "766018776134",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:35:09 AM",
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
                            "prn": "766018776134",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "08b9708c-792d-4662-a953-ccf57be2603a",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "3402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "2e6445c4-1679-4053-b1ae-f6f890b20327",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "3403",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "lyndonfidel1"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/8033479422883903884"
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
    

