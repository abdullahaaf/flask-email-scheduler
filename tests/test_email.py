def test_save_emails(client, app):
    with app.app_context():
        # Test case for a successful save and schedule
        data = {
            'event_id': 1,
            'email_subject': 'Test Subject',
            'email_content': 'Test Content',
            'timestamp': '2023-02-25 10:00'
        }
        response = client.post('/save_emails', json=data)
        assert response.status_code == 201
        assert response.json == {
            'message': 'success schedule email',
            'data': {
                'email_content': 'Test Content',
                'email_subject': 'Test Subject',
                'event_id': 1,
                'timestamp': '2023-02-25 10:00'
            }
        }

        # Test case for missing required field
        data = {
            'event_id': 1,
            'email_subject': 'Test Subject',
            'timestamp': '2023-02-25 10:00'
        }
        response = client.post('/save_emails', json=data)
        assert response.status_code == 400
        assert response.json == {
            'message': 'Error, one of field is empty. Check your data'
        }