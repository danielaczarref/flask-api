import pytest
from app import createApp
from db import engine
from sqlalchemy import MetaData


@pytest.fixture
def app():
    app = createApp()
    app.config.update(
        {
            "TESTING": True
        }
    )
    with app.app_context():
        sql_meta = MetaData(engine)
        sql_meta.create_all(bind=engine)

    yield app


@pytest.fixture
def client(app):
    app = createApp()
    return app.test_client()
