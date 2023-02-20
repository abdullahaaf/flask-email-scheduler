def test_event(client, app):
    with app.app_context():
        # Test case for get event
        response = client.get('/api/events')
        assert response.status_code == 200
        assert response.json == {
            'message': 'success get events',
            'data': [
            ]
        }

        # Test case for add new event
        data = {
            'event_name': 'Cooking Demo',
        }
        response = client.post('/api/event', json=data)
        assert response.status_code == 201
        assert response.json == {
            'message': 'success add event',
            'data' : {
            'event_name' : 'Cooking Demo'
            }
        }

        # Test case for missing required field
        data = {}
        response = client.post('/api/event', json=data)
        assert response.status_code == 400
        assert response.json == {
            'message': 'Error, event name is required'
        }