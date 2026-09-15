from unittest.mock import MagicMock, patch
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import app as flask_module


@pytest.fixture
def client():
  flask_module.app.config['TESTING'] = True
  with flask_module.app.test_client() as client:
    yield client


@patch.object(flask_module, 'get_db_connection')
def test_health(mock_get_db, client):
  mock_conn = MagicMock()
  mock_conn.ping.return_value = True
  mock_get_db.return_value = mock_conn

  response = client.get('/health')

  assert response.status_code == 200
  assert response.json['status'] == 'healthy'