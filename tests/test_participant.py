def test_event(client, app):
    with app.app_context():
        # Test case for add new participant
        data = {
            "event_id" : 1,
            "full_name" : "dogypu",
            "email" : "dogypu@vomoto.com"
        }
        response = client.post('/api/participant', json=data)
        assert response.status_code == 201
        assert response.json == {
            'message': 'success add participant',
            'data' : {
                "event_id" : 1,
                "full_name" : "dogypu",
                "email" : "dogypu@vomoto.com"
            }
        }

        # Test case for missing required field
        data = {
            "event_id" : 1,
            "email" : "dogypu@vomoto.com"
        }
        response = client.post('/api/participant', json=data)
        assert response.status_code == 400
        assert response.json == {
            'message': 'Error, one of field is empty. Check your data'
        }