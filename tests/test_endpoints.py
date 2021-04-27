import json

class TestEndpoints:
	testChannel = "C020RBV28P2"

	def test_non_listed_endpoints(self, app, client):
		response = client.get('/fake-endpoint')
		assert response.status_code == 404

	def test_health_endpoint(self, app, client):
		response = client.get('/health')
		assert response.status_code == 200
		expected = {"success": True}
		assert expected == json.loads(response.get_data(as_text=True))

	def test_testPost_endpoint(self, app, client):
		response = client.get('/testPost/' + self.testChannel)
		assert response.status_code == 200
		expected = {"success": True}
		assert expected == json.loads(response.get_data(as_text=True))