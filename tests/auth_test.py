"""This test the homepage"""
from app import db
import logging
from app.db.models import User, Song


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200

def test_registration(client):
    """Test if a user logs in that it redirects to login page"""
    with client:
        res = client.post('/register', data=dict(email="ak298@gmail.com", password='testtest'), follow_redirects=True)
        print(res.data)
        assert res.status_code == 400


def test_dashboard_access(client):
    """Test dashboard access"""
    res = client.get("/dashboard")
    assert res.status_code == 302


def test_authenticated_user(client):
    """Test user authentication"""
    user = User("ak298@njit.edu", "testtest")
    assert user.is_authenticated() == True
