def test_messages(client):
    """Start with a blank database."""

    rv = client.get('/messages.json')
    json_data = rv.get_json()
    assert 'messages' in json_data.keys()
    assert len(json_data['messages']) == 0


    # Create a user
    rv = client.post('/users.json', json={"name":"John Smith", "email": 'john@gmail.com'})
    json_data = rv.get_json()
    print(json_data)

    # Create a message
    rv = client.post('/messages.json', json={"message":"Hello there!", "userId": 1})
    json_data = rv.get_json()
    print(json_data)