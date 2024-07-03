import json

# NOTE Update the errors to "No errors encountered." 
# NOTE Remove all the warnings before running this code. This can be done by using the text editor.

json_data = '''
{
    "data": {
        "getBulkUsers": {
            "status": {
                "start": "2024-06-26 17:04:52 UTC",
                "state": "15/20 users created.",
                "errorCount": 1,
                "errors": "No errors encountered."
            },
            "users": [
                {
                    "user_id": 21167598,
                    "auth_token": "b70ba89d-544c-482b-939d-e75993401eeb",
                    "ssn": "348665557",
                    "email": "quinton.1719421963@gmail.com",
                    "password": "password",
                    "first_name": "Joshua",
                    "last_name": "Kristeen",
                    "date_of_birth": "1999-01-20",
                    "address": "851 Thomasine Mill",
                    "zip_code": "95664",
                    "phone": 4778392551,
                    "user_accounts": [
                        {
                            "id": "kAuwDAM0",
                            "account_number": "766018681519",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 10:13:17 AM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "1QuLNx38",
                            "account_number": "726018681536",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 10:13:17 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "XzuOB2Lr",
                            "account_number": "725018681538",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 10:13:04 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681519",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "112bac99-bf6a-45d1-b1fa-027d320326ae",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "14a573b4-6cff-4706-8ab8-55dc2ab3d9e1",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1903",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681538",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "91a083cf-1b1e-4a9d-b99e-f65fe5e1a782",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "2a2240c5-d397-4460-8c5b-238e0e599558",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "joshuakristeen"
                },
                {
                    "user_id": 21167586,
                    "auth_token": "a8080456-1cbb-4013-a577-c622d24fa749",
                    "ssn": "642083552",
                    "email": "frank.1719421931@gmail.com",
                    "password": "password",
                    "first_name": "Malissa",
                    "last_name": "Richie",
                    "date_of_birth": "1976-03-11",
                    "address": "7013 Hoppe Fords",
                    "zip_code": "67519",
                    "phone": 2665743772,
                    "user_accounts": [
                        {
                            "id": "2muEZA51",
                            "account_number": "766018681490",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 05:12:42 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "e1uoDEmd",
                            "account_number": "726018681508",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 05:12:42 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "3Lu97gj0",
                            "account_number": "725018681509",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 05:12:29 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681490",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a971de9e-5df9-4440-aade-67714d1eeaa0",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9000",
                                    "card_status": "N"
                                },
                                {
                                    "id": "0e5d2b2c-5b18-4a1c-ba14-7e40ffb11eed",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9001",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681509",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "307ab7c8-7c31-4c75-9beb-9afefc3ff9df",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0900",
                                    "card_status": "N"
                                },
                                {
                                    "id": "4d0be056-eb69-4735-9afa-0626011cd457",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0901",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "malissarichie"
                },
                {
                    "user_id": 21167572,
                    "auth_token": "ddbfbe44-9fe2-4102-af60-a206fc7b4ed9",
                    "ssn": "073868176",
                    "email": "broderick.1719421900@gmail.com",
                    "password": "password",
                    "first_name": "Victor",
                    "last_name": "Georgianna",
                    "date_of_birth": "1992-10-04",
                    "address": "48289 Rutherford Lodge",
                    "zip_code": "98408",
                    "phone": 4338402060,
                    "user_accounts": [
                        {
                            "id": "dNuLwbn6",
                            "account_number": "766018681457",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 10:12:10 AM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "e1uoDEnd",
                            "account_number": "726018681464",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 10:12:10 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "3Lu97gB0",
                            "account_number": "725018681466",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 10:11:57 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681457",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "76b8e1e6-180c-4313-bf8a-057f3c077c72",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "5700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "78d57c1c-9dd3-48c7-8131-b46ce67ba88a",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "5701",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681466",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "6d4fa7cf-8728-43f1-8271-1316e4566de7",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "6600",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e2574dde-b424-4498-826f-553ac67a6e72",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "6601",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "victorgeorgianna"
                },
                {
                    "user_id": 21167566,
                    "auth_token": "c7857a8b-4b98-41af-9b10-fb2a31d6bcc1",
                    "ssn": "425056245",
                    "email": "1719421865_kristal@hotmail.com",
                    "password": "password",
                    "first_name": "Everett",
                    "last_name": "Vina",
                    "date_of_birth": "1997-02-28",
                    "address": "930 Quitzon Spurs",
                    "zip_code": "14901",
                    "phone": 4000800473,
                    "user_accounts": [
                        {
                            "id": "65u2lwY8",
                            "account_number": "766018681444",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 01:11:38 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "2muEZAO1",
                            "account_number": "726018681447",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 01:11:38 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "nxuE3LwX",
                            "account_number": "725018681448",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 01:11:25 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681444",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "7777f1e1-a908-47a1-bc80-68fbf78d72a9",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "47cf6103-f621-4684-9a22-214e4dab7716",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4401",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681448",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "a7708942-0157-4f57-a03e-4feab2d9b6d3",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "db0a8d85-3852-40f1-8e1e-ef2181066c52",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4801",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "everettvina"
                },
                {
                    "user_id": 21167561,
                    "auth_token": "288feade-cc0a-43c3-be69-56443b8fade9",
                    "ssn": "691995762",
                    "email": "1719421832.albertha@hotmail.com",
                    "password": "password",
                    "first_name": "Felton",
                    "last_name": "Jamey",
                    "date_of_birth": "1970-09-09",
                    "address": "4271 Lueilwitz Passage",
                    "zip_code": "15126",
                    "phone": 2005536110,
                    "user_accounts": [
                        {
                            "id": "a8umZv4a",
                            "account_number": "766018681432",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 01:11:05 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "1QuLNx1E",
                            "account_number": "726018681435",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 01:11:04 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "03um8qyb",
                            "account_number": "725018681436",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 01:10:51 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681432",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "5eb2b9e1-6aab-4634-b686-aa1c46d38d45",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3200",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f3c7103e-0bbe-45da-b8eb-1d1887fc03dc",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3201",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681436",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "e39a0f83-1501-4810-a9e2-85eaa19542d4",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3601",
                                    "card_status": "N"
                                },
                                {
                                    "id": "ceebd36e-3f6b-4e77-8f64-837196eac5dd",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3602",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "feltonjamey1"
                },
                {
                    "user_id": 21167559,
                    "auth_token": "7d12cee6-36bc-4f8e-9577-e3df253e18de",
                    "ssn": "579057724",
                    "email": "deeanna_1719421797@gmail.com",
                    "password": "password",
                    "first_name": "Wally",
                    "last_name": "Gwenda",
                    "date_of_birth": "1959-08-11",
                    "address": "2323 Alice Crossroad",
                    "zip_code": "31054",
                    "phone": 3762068156,
                    "user_accounts": [
                        {
                            "id": "AAuVE4L4",
                            "account_number": "766018681427",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 01:10:30 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "BDuokW3Y",
                            "account_number": "726018681430",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 01:10:30 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "kAuwDAQ0",
                            "account_number": "725018681431",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 01:10:16 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681427",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "434fd1ff-1942-4563-9876-741fe614fe19",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "2700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1bfebebb-cf82-4bcb-88e4-23051f4633a8",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "2701",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681431",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "2e6a4ffa-e1a1-442a-8e12-551c7af6d0b3",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3101",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c87b5ae7-3c62-4906-8656-c92ebf72b565",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3102",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "wallygwenda1"
                },
                {
                    "user_id": 21167555,
                    "auth_token": "237f80fe-f68c-48b8-b600-3c4fad9b8f2f",
                    "ssn": "497868974",
                    "email": "1719421761.christiana@yahoo.com",
                    "password": "password",
                    "first_name": "Ulysses",
                    "last_name": "Valentine",
                    "date_of_birth": "1965-10-27",
                    "address": "4547 Otis Gardens",
                    "zip_code": "33547",
                    "phone": 9696424697,
                    "user_accounts": [
                        {
                            "id": "8YugenB6",
                            "account_number": "766018681415",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 01:09:56 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "kAuwDAO9",
                            "account_number": "726018681418",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 01:09:57 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "a8umZvkA",
                            "account_number": "725018681419",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 01:09:42 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681415",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "519fa9d4-2420-4595-a81c-ab66864c9542",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1500",
                                    "card_status": "N"
                                },
                                {
                                    "id": "b8929a6f-47ee-4c5b-81b9-aaebac5a3584",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1501",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681419",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "5ccd8cbf-3506-4560-9933-b738d3e1633a",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1900",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c87c862f-bfa7-4b01-aadd-d94ca39c998b",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1901",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "ulyssesvalentine1"
                },
                {
                    "user_id": 21167553,
                    "auth_token": "faa0a5d7-7d71-48ee-90f3-82e33bd1faa7",
                    "ssn": "678790266",
                    "email": "1719421726_maryanne@yahoo.com",
                    "password": "password",
                    "first_name": "Clarisa",
                    "last_name": "Jermaine",
                    "date_of_birth": "2004-12-11",
                    "address": "5761 Roman Stravenue",
                    "zip_code": "47932",
                    "phone": 9336706249,
                    "user_accounts": [
                        {
                            "id": "LMu4OrL0",
                            "account_number": "766018681411",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 05:09:19 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "W4uknBZq",
                            "account_number": "726018681413",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 05:09:21 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "5WuW57P9",
                            "account_number": "725018681414",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 05:09:06 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681411",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "fb563e05-3f95-4c49-81a3-371e66c650ae",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1102",
                                    "card_status": "N"
                                },
                                {
                                    "id": "ce2ef729-2c5d-4f18-9358-36d0059e48d2",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1103",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681414",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "6deb389d-04a3-482d-b2f7-2c6e15d93d67",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1400",
                                    "card_status": "N"
                                },
                                {
                                    "id": "e0aaf50b-9121-4174-8836-e3eb2667db3c",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1401",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "clarisajermaine"
                },
                {
                    "user_id": 21167552,
                    "auth_token": "80b103d1-ed37-4b17-9eb1-a9eb1f621796",
                    "ssn": "547105170",
                    "email": "1719421690_maggie@hotmail.com",
                    "password": "password",
                    "first_name": "Pierre",
                    "last_name": "Valeri",
                    "date_of_birth": "1982-01-22",
                    "address": "823 Auer Mill",
                    "zip_code": "45440",
                    "phone": 9676386651,
                    "user_accounts": [
                        {
                            "id": "3Lu97gzn",
                            "account_number": "766018681408",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 01:08:45 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "Qqu7b8lg",
                            "account_number": "726018681409",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 01:08:45 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "mEuKlMXb",
                            "account_number": "725018681410",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 01:08:31 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681408",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b1cf13b7-d59e-4f90-8f78-05daa1ac520a",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "a8564bc4-ae2d-4c47-a21d-a6e8a15fe0b0",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0801",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681410",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "ccf25afb-8e75-41eb-924d-f03c992781eb",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1001",
                                    "card_status": "N"
                                },
                                {
                                    "id": "55f42952-12ab-46d0-af60-5ddffdee4869",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "1002",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "pierrevaleri"
                },
                {
                    "user_id": 21167549,
                    "auth_token": "87aa24e8-8a49-4fc8-9d5e-5959361a32c8",
                    "ssn": "267303500",
                    "email": "1719421656_andy@hotmail.com",
                    "password": "password",
                    "first_name": "Erik",
                    "last_name": "Buddy",
                    "date_of_birth": "1973-10-21",
                    "address": "98834 Eldon Extension",
                    "zip_code": "68004",
                    "phone": 4661428515,
                    "user_accounts": [
                        {
                            "id": "KZuZPQmq",
                            "account_number": "766018681401",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 12:08:09 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "4ouVb0Pk",
                            "account_number": "726018681405",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 12:08:09 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "zyu9z4QV",
                            "account_number": "725018681406",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:07:56 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681401",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "8a1a62cb-e41b-4f2a-b334-5bd690f378f4",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0100",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1b712c8d-3842-4ca9-8926-4aff3f331afd",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0101",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681406",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "43dee550-0e61-4091-8ae5-46a569225e3b",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0602",
                                    "card_status": "N"
                                },
                                {
                                    "id": "4ffb0088-86a3-4433-b92f-4ba6be2e324e",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0603",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "erikbuddy"
                },
                {
                    "user_id": 21167545,
                    "auth_token": "8420e0e4-e27a-4169-97de-b878fdc0055e",
                    "ssn": "434588298",
                    "email": "homer.1719421624@hotmail.com",
                    "password": "password",
                    "first_name": "Erik",
                    "last_name": "Isiah",
                    "date_of_birth": "1994-10-06",
                    "address": "156 Forest Street",
                    "zip_code": "77656",
                    "phone": 9778120729,
                    "user_accounts": [
                        {
                            "id": "VbuVZAYL",
                            "account_number": "766018681397",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 12:07:36 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "y9undBmz",
                            "account_number": "726018681399",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 12:07:36 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "qjuwMYDV",
                            "account_number": "725018681400",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:07:22 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681397",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "9729b5c0-4886-4470-84d1-d826c6938bb8",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9702",
                                    "card_status": "N"
                                },
                                {
                                    "id": "641d3a16-b5dd-4322-9101-ef6e505efc09",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "9703",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681400",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "b312f14f-b51f-4257-afbd-5c1b7ee72b70",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0000",
                                    "card_status": "N"
                                },
                                {
                                    "id": "59b628ba-bd38-423b-846e-29ce3d5955cd",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0001",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "erikisiah"
                },
                {
                    "user_id": 21167525,
                    "auth_token": "9275b366-0a60-443c-a512-3c75d26e4c8e",
                    "ssn": "320931906",
                    "email": "jamal_1719421590@hotmail.com",
                    "password": "password",
                    "first_name": "Mariella",
                    "last_name": "Chris",
                    "date_of_birth": "1988-05-09",
                    "address": "4269 Emmanuel Glen",
                    "zip_code": "08510",
                    "phone": 2221662495,
                    "user_accounts": [
                        {
                            "id": "a8umZv0A",
                            "account_number": "766018681379",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 10:07:02 AM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "AAuVE4B4",
                            "account_number": "726018681386",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 10:07:03 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "DxuYONLk",
                            "account_number": "725018681387",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 10:06:49 AM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681379",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e00415b0-bcb8-4f0d-8dda-5740a70ec185",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "7902",
                                    "card_status": "N"
                                },
                                {
                                    "id": "1ffa8c5e-c990-4ea8-abbe-e6302e2a75ed",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "7903",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681387",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "801f0b5b-05af-466c-a5e5-e24e13bf45de",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "7ec235d1-95f6-4b71-aeb6-cc40ccee3501",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "8701",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "mariellachris1"
                },
                {
                    "user_id": 21167509,
                    "auth_token": "7fa8b06a-575d-4317-ad53-b9314b2c6620",
                    "ssn": "755964928",
                    "email": "1719421557_granville@yahoo.com",
                    "password": "password",
                    "first_name": "Tana",
                    "last_name": "Elias",
                    "date_of_birth": "1985-06-07",
                    "address": "858 Tia Estate",
                    "zip_code": "03782",
                    "phone": 9676681193,
                    "user_accounts": [
                        {
                            "id": "9au9vg3a",
                            "account_number": "766018681357",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 05:06:29 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "e1uoDEAM",
                            "account_number": "726018681367",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 05:06:29 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "Qqu7b8mg",
                            "account_number": "725018681369",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 05:06:15 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681357",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "b57a3a27-790e-464e-8fc4-1ec02445a8f2",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "5700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "f600bd6f-2da8-4aee-a234-ce50da9b3ec3",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "5701",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681369",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "4828c0fa-0a66-4a54-80f7-5eebc3596a55",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "6901",
                                    "card_status": "N"
                                },
                                {
                                    "id": "cdc2cd05-bfbc-4673-9a1a-5af287274044",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "6902",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "tanaelias"
                },
                {
                    "user_id": 21167493,
                    "auth_token": "e5529e75-02cb-436e-8e99-e00f6b120e26",
                    "ssn": "404453291",
                    "email": "jerica_1719421524@yahoo.com",
                    "password": "password",
                    "first_name": "Warren",
                    "last_name": "Victorina",
                    "date_of_birth": "1988-01-14",
                    "address": "45748 Jerrell Lodge",
                    "zip_code": "53593",
                    "phone": 9445471830,
                    "user_accounts": [
                        {
                            "id": "a8umZvlA",
                            "account_number": "766018681337",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 12:05:53 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "E6uo4MZW",
                            "account_number": "726018681346",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 12:05:54 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "xguvynVz",
                            "account_number": "725018681347",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 12:05:41 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681337",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "e19ca800-03ff-49d0-a1bf-59152a46c634",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "c1fb8f1c-6191-481b-bd78-1f4505b86698",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "3701",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681347",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "e72dcdaf-e0b7-40a1-8889-8cc5d4a9469c",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4700",
                                    "card_status": "N"
                                },
                                {
                                    "id": "2ce49f6c-2d67-4270-b832-9f02325eadaa",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "4701",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "warrenvictorina"
                },
                {
                    "user_id": 21167472,
                    "auth_token": "54e5b9ed-e8d8-4bb9-8c27-412a3511fdcf",
                    "ssn": "886705439",
                    "email": "trudie.1719421492@hotmail.com",
                    "password": "password",
                    "first_name": "Rocky",
                    "last_name": "Lovetta",
                    "date_of_birth": "1970-10-06",
                    "address": "60089 Grazyna Row",
                    "zip_code": "66967",
                    "phone": 3888400687,
                    "user_accounts": [
                        {
                            "id": "KZuZPQ8w",
                            "account_number": "766018681308",
                            "account_summary": null,
                            "account_type": "checking",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1600.0,
                            "balance_updated_at": "2024-06-26 05:05:22 PM",
                            "balances": {
                                "display": 1600.0,
                                "balance": 1600.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "kAuwDANd",
                            "account_number": "726018681324",
                            "account_summary": null,
                            "account_type": "security_deposit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 1500.0,
                            "balance_updated_at": "2024-06-26 05:05:22 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 1500.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        },
                        {
                            "id": "a8umZvlO",
                            "account_number": "725018681325",
                            "account_summary": {
                                "start_at": "2024-04-29T00:00:00Z",
                                "end_at": "2024-05-28T00:00:00Z",
                                "auto_pay_date": null
                            },
                            "account_type": "secured_credit",
                            "active": true,
                            "auto_deposit": false,
                            "balance": 0.0,
                            "balance_updated_at": "2024-06-26 05:05:10 PM",
                            "balances": {
                                "display": 1500.0,
                                "balance": 0.0
                            },
                            "bank_name": "BANCORP",
                            "processor": "galileo",
                            "routing_number": "031101279"
                        }
                    ],
                    "account_cards_info": [
                        {
                            "prn": "766018681308",
                            "account_type": "checking",
                            "cards": [
                                {
                                    "id": "a600565c-2aa7-467e-ae22-d4bcf9c287fc",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0800",
                                    "card_status": "N"
                                },
                                {
                                    "id": "76ff4ce7-8a35-4d53-be77-fbb29b0367b4",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "0801",
                                    "card_status": "N"
                                }
                            ]
                        },
                        {
                            "prn": "725018681325",
                            "account_type": "secured_credit",
                            "cards": [
                                {
                                    "id": "dc3ef37f-cec7-4b11-abb4-fccc3e18c49f",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "2500",
                                    "card_status": "N"
                                },
                                {
                                    "id": "3381a6af-b1d8-4c33-a207-fde04a68f8c6",
                                    "expiry_date": "2028-06-26",
                                    "card_number": "2501",
                                    "card_status": "N"
                                }
                            ]
                        }
                    ],
                    "referral_token": "rockylovetta"
                }
            ]
        }
    },
    "datadog": "https://app.datadoghq.com/apm/trace/3689861050370928622"
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
    

