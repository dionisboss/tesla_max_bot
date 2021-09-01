user_test = {
    '_id': 1,  # telegram id,
    'first_name': 'Joseph',
    'last_name': 'Brown',
    'username': 'dsadsajknkdsansnuei',
    'phone_number': '89999856659',
    'date_registered': 1600425333,
    'date_last_active': 1600425333,
    'status': "start",  # started, registered, banned
    'add_last_sent': None,
    'activity': [
        {
            'text': "some_text",
            'timestamp': 1600425333,
        },
    ],
    "exhibits_visited":
        {
            "exhibit_id": {
                "time_stamp": 1600425333,
                "user_rating": 10,
                "user_response": "some text"
            },
        },
}

# test instance for admins
admin_test = {
    '_id': 1,  # telegram id,
    'admin': True,
    'first_name': 'Joseph',
    'last_name': 'Brown',
    'username': 'dsadsajknkdsansnuei',
    'phone_number': '89999856659',
    'date_registered': 1600425333,
    'date_last_active': 1600425333,
    'add_last_sent': None,
    'activity': [
        {
            'text': "some_text",
            'timestamp': 1600425333,
        },
    ],
    "visits":
        {
            "exhibition_id": "id",
            "exhibits_visited": {
                "exhibit_id": {
                    "time_stamp": 1600425333,
                    "user_rating": 10,
                    "user_response": "some text"
                },
            },
        }

}
# test instance for exhibits
exhibition_test = {
    # _id will be auto configured
    "exhibition_id": 'internal_id',
    "exhibition_name": "name",
    "status": "open",
    "time_stamp_opened": 1234560,
    "time_stamp_closed": 12344577,
    "id_creator": "tg_id",
    "exhibits": {
        "exhibit_id": {
            "internal_exhibit_id": 0,
            "name": "Смысл Жизни",
            "description": "42",
            "audio_file": {
                "path_to_file": "path",
                "tg_id": None  # or id
            },
            "video_file": {
                "path_to_file": "path",
                "tg_id": None,  # or id
            },
            "picture": {
                "path_to_file": "path",
                "tg_id": None  # or id
            },
            "statistics": {
                "user_id": {
                    "time_stamp": 1600425333,
                    "user_rating": 10,
                    "user_response": "some text",
                },
            },
        }
    }
}
