import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-07-03 15:25:58 UTC",
                "state": "15/20 users created.",
                "errorCount": 0,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 21258971,
                    "auth_token": "6e50b30b-ab5c-49a2-9ff8-1c6eb850c409",
                    "ssn": "570337742",
                    "email": "Jay.1720020799+cb1@chime.com",
                    "password": "password",
                    "first_name": "Jennine",
                    "last_name": "Everette",
                    "date_of_birth": "1971-07-30",
                    "address": "344 Roxann Corner",
                    "zip_code": "53924",
                    "phone": 3712903914,
                    "user_accounts": [
                        {
                            "id": "r2urX09m",
                            "account_number": "766018776020",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 10:33:36 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018776020",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "beb5f0df-3661-4a62-9f43-abdd334717d5",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "2002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5f8997ae-a068-458a-9530-7d4bfbaea1fe",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "2003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "jennineeverette"
                },
                {
                    "user_id": 21258950,
                    "auth_token": "cb47e708-7956-4d9e-9484-35276b91af44",
                    "ssn": "246042226",
                    "email": "Kisha.1720020769+cb1@chime.com",
                    "password": "password",
                    "first_name": "Adolfo",
                    "last_name": "Martin",
                    "date_of_birth": "2004-11-05",
                    "address": "229 Reichert Islands",
                    "zip_code": "82646",
                    "phone": 4009692568,
                    "user_accounts": [
                        {
                            "id": "Qqu78aDg",
                            "account_number": "766018775992",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 09:33:06 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775992",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "80fa9ce3-5177-48f2-aa8a-ba652c32c898",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9202",
                                    "card_status": "N"
                                },
                                {
                                    "id": "62cbb96f-eb6d-47fc-9123-c3a226d04790",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9203",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "adolfomartin1"
                },
                {
                    "user_id": 21258932,
                    "auth_token": "4615fd20-f883-4fab-aa06-8dcfb8ebfb75",
                    "ssn": "482611671",
                    "email": "Lenna.1720020739+cb1@chime.com",
                    "password": "password",
                    "first_name": "Andrea",
                    "last_name": "Myong",
                    "date_of_birth": "1990-04-20",
                    "address": "88786 King Extension",
                    "zip_code": "84532",
                    "phone": 4443291029,
                    "user_accounts": [
                        {
                            "id": "xguvnEgz",
                            "account_number": "766018775970",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 09:32:36 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775970",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "9e3a2fe9-9187-4f87-81f5-9fbef7b9f8a3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "7021a117-e95a-48d3-a0ca-673e98697c00",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "7003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "andreamyong"
                },
                {
                    "user_id": 21258907,
                    "auth_token": "360f1252-32c7-448e-b5c7-6a3b3b112257",
                    "ssn": "725930105",
                    "email": "Rodger.1720020709+cb1@chime.com",
                    "password": "password",
                    "first_name": "Delbert",
                    "last_name": "Rubin",
                    "date_of_birth": "1965-12-12",
                    "address": "8047 Yahaira Ports",
                    "zip_code": "67480",
                    "phone": 9655748182,
                    "user_accounts": [
                        {
                            "id": "qjuwYObV",
                            "account_number": "766018775939",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 03:31:54 PM",
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
                            "prn": "766018775939",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "225bae02-dc80-4931-861e-94f07639d171",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "3902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "23cc6a97-f9c5-4c5b-a6bc-5e9b3c4c23ba",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "3903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "delbertrubin2"
                },
                {
                    "user_id": 21258874,
                    "auth_token": "3e405ef7-df0a-4872-a73e-43de5411dc2c",
                    "ssn": "359024374",
                    "email": "Mirtha.1720020680+cb1@chime.com",
                    "password": "password",
                    "first_name": "Cherly",
                    "last_name": "Mary",
                    "date_of_birth": "1974-05-16",
                    "address": "971 DuBuque Burgs",
                    "zip_code": "62819",
                    "phone": 3331629475,
                    "user_accounts": [
                        {
                            "id": "kAuwAj5d",
                            "account_number": "766018775904",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 10:31:36 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775904",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e0eee614-d7a7-43b9-bcd5-f1c59e11f0f2",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "0402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "95d7615e-fed2-4169-b4c0-41d45a77e711",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "0403",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "cherlymary"
                },
                {
                    "user_id": 21258864,
                    "auth_token": "2cf176d5-7eb4-4732-af13-2546fe738304",
                    "ssn": "330834343",
                    "email": "Mozelle.1720020647+cb1@chime.com",
                    "password": "password",
                    "first_name": "Elliot",
                    "last_name": "Vera",
                    "date_of_birth": "1976-10-22",
                    "address": "83494 Merlin Cove",
                    "zip_code": "59853",
                    "phone": 3788418608,
                    "user_accounts": [
                        {
                            "id": "3Lu9gjwB",
                            "account_number": "766018775895",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 09:31:07 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775895",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "82a29c60-36c4-41e7-a1ec-977ecd1cfbae",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "cf28b72f-8f8a-4a71-adb1-56c729f273db",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "elliotvera"
                },
                {
                    "user_id": 21258863,
                    "auth_token": "93f389c7-af89-4df8-8378-6239116351a7",
                    "ssn": "492750703",
                    "email": "Abel.1720020615+cb1@chime.com",
                    "password": "password",
                    "first_name": "Reuben",
                    "last_name": "Erick",
                    "date_of_birth": "1985-12-08",
                    "address": "519 Brain Estate",
                    "zip_code": "15027",
                    "phone": 2555123757,
                    "user_accounts": [
                        {
                            "id": "e1uoEmgW",
                            "account_number": "766018775894",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 11:30:35 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775894",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "fb3348cf-813d-460f-a185-11c389316cf0",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9402",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1d2adce2-30ca-4302-9c31-32f2239a42ab",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9403",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "reubenerick"
                },
                {
                    "user_id": 21258862,
                    "auth_token": "12e407bd-9828-4988-b67e-2e6daecf8442",
                    "ssn": "877606508",
                    "email": "Dia.1720020583+cb1@chime.com",
                    "password": "password",
                    "first_name": "Lewis",
                    "last_name": "Chance",
                    "date_of_birth": "1980-07-15",
                    "address": "51190 Schultz Skyway",
                    "zip_code": "31075",
                    "phone": 7337805189,
                    "user_accounts": [
                        {
                            "id": "zyu94awn",
                            "account_number": "766018775893",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 11:30:03 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775893",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e224fd4b-a6e1-41db-82f4-9e58edda8ecf",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9302",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c72c47ad-3349-4fbb-b736-127936df26c3",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9303",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "lewischance"
                },
                {
                    "user_id": 21258861,
                    "auth_token": "000d9863-04aa-4892-af0e-863e45d7f5e6",
                    "ssn": "383374857",
                    "email": "Paris.1720020551+cb1@chime.com",
                    "password": "password",
                    "first_name": "Kim",
                    "last_name": "Trenton",
                    "date_of_birth": "1967-12-09",
                    "address": "92938 Lind Prairie",
                    "zip_code": "78245",
                    "phone": 9630357821,
                    "user_accounts": [
                        {
                            "id": "bYun8ZLV",
                            "account_number": "766018775891",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 10:29:32 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775891",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8c05b58b-94ba-401e-9bd8-20183e3a44dc",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e6c0c15d-c977-490a-a18e-9f7e4d8bac10",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9103",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "kimtrenton"
                },
                {
                    "user_id": 21258860,
                    "auth_token": "cba4306c-2855-45c2-9c00-ea5f4e6d208e",
                    "ssn": "256621911",
                    "email": "Rueben.1720020520+cb1@chime.com",
                    "password": "password",
                    "first_name": "Nikita",
                    "last_name": "Divina",
                    "date_of_birth": "1962-10-10",
                    "address": "1166 Logan Estate",
                    "zip_code": "91361",
                    "phone": 4221720270,
                    "user_accounts": [
                        {
                            "id": "wVu0ODQ2",
                            "account_number": "766018775890",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 08:28:59 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775890",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "d552c8ce-6d37-46ea-9582-63715241ff2c",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9002",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6d1102fd-51ba-4fa9-afee-168a132926c2",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "9003",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "nikitadivina"
                },
                {
                    "user_id": 21258859,
                    "auth_token": "4b834ace-2a03-405b-9545-65139fa2709a",
                    "ssn": "049708180",
                    "email": "Brett.1720020487+cb1@chime.com",
                    "password": "password",
                    "first_name": "Alvaro",
                    "last_name": "Jacinto",
                    "date_of_birth": "1997-12-13",
                    "address": "90188 Mervin Views",
                    "zip_code": "05450",
                    "phone": 4220445227,
                    "user_accounts": [
                        {
                            "id": "78ugVbNg",
                            "account_number": "766018775889",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-07-03 10:28:14 AM",
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
                            "prn": "766018775889",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "254b1d97-fed3-4423-918b-7c37ffc5cc3d",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "dfef6d57-5441-4669-880a-0be35c52e607",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8903",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "alvarojacinto"
                },
                {
                    "user_id": 21258858,
                    "auth_token": "9833019a-dd2a-4e9d-bcbd-d96048379514",
                    "ssn": "532954729",
                    "email": "Denae.1720020455+cb1@chime.com",
                    "password": "password",
                    "first_name": "Logan",
                    "last_name": "Evan",
                    "date_of_birth": "1996-12-18",
                    "address": "25576 Maricela Brook",
                    "zip_code": "75235",
                    "phone": 9331545530,
                    "user_accounts": [
                        {
                            "id": "KZuZQ7ew",
                            "account_number": "766018775888",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 10:27:54 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775888",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8730d05f-5cf4-4ca4-8251-fd02e8ceff38",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8802",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e7a3080e-7c84-447a-9ff8-221e183ebf84",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8803",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "loganevan2"
                },
                {
                    "user_id": 21258857,
                    "auth_token": "258f5d9a-d8c5-4666-ae42-6513ae39845c",
                    "ssn": "200040369",
                    "email": "Roberto.1720020422+cb1@chime.com",
                    "password": "password",
                    "first_name": "Dana",
                    "last_name": "Maple",
                    "date_of_birth": "1968-09-22",
                    "address": "7934 Riley Rapid",
                    "zip_code": "83272",
                    "phone": 9639353223,
                    "user_accounts": [
                        {
                            "id": "dNuLbjOB",
                            "account_number": "766018775887",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 09:27:23 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775887",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "ff8bf91b-58ef-4650-855d-9a771e60b1ee",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8702",
                                    "card_status": "N"
                                },
                                {
                                    "id": "cb277d3d-760a-441b-b818-68a4c0722f0c",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8703",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "danamaple"
                },
                {
                    "user_id": 21258856,
                    "auth_token": "fb6fa370-b5d7-412d-9983-df5e7255dc44",
                    "ssn": "790241048",
                    "email": "Buster.1720020390+cb1@chime.com",
                    "password": "password",
                    "first_name": "Mallory",
                    "last_name": "Erasmo",
                    "date_of_birth": "1975-02-25",
                    "address": "84366 Edward Ports",
                    "zip_code": "15237",
                    "phone": 3794707301,
                    "user_accounts": [
                        {
                            "id": "qjuwYOv7",
                            "account_number": "766018775886",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 11:26:49 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775886",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "24760ea7-f02c-4524-8675-c2305c7b9d71",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "5dc60b0f-0093-4224-8973-9d833db9a178",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "malloryerasmo"
                },
                {
                    "user_id": 21258855,
                    "auth_token": "e942e0ce-5b1b-48fe-8f33-ab33b0074f22",
                    "ssn": "444847805",
                    "email": "Anne.1720020358+cb1@chime.com",
                    "password": "password",
                    "first_name": "Alfonso",
                    "last_name": "Chia",
                    "date_of_birth": "1983-06-07",
                    "address": "602 Hauck Pine",
                    "zip_code": "76023",
                    "phone": 3220511880,
                    "user_accounts": [
                        {
                            "id": "y9unBxEb",
                            "account_number": "766018775885",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1000.0,
                            "balance_updated_at": "2024-07-03 10:26:19 AM",
                            "balances": {
                                "display": 1000.0,
                                "balance": 1000.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018775885",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8d30597b-207f-46cd-8cab-d54c2e156901",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8502",
                                    "card_status": "N"
                                },
                                {
                                    "id": "6e312d80-ad71-4e9c-a951-d0469a4b7277",
                                    "expiry_date": "2028-07-03",
                                    "card_number": "8503",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "spotme_eligible": true,
                    "spotme_eligible_and_funded": true,
                    "spotme_enrolled": [
                        "checking"
                    ],
                    "referral_token": "alfonsochia"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/1537487088562668560"
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

    

