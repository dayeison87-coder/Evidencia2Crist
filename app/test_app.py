from unittest.mock import MagicMock, patch
import pytest
from app.app import app, get_db_connection 


@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client


@patch('app.app.get_db_connection')
def test_health(mock_get_db, client):
  mock_conn = MagicMock()
  mock_conn.ping.return_value = True
  mock_get_db.return_value = mock_conn

  response = client.get('/health')

  assert response.status_code == 200
  assert response.json['status'] == 'healthy'