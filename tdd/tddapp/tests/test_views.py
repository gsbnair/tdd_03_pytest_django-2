import pytest
from django.http import Http404
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer
from django.core.mail import send_mail
from django.core import mail

# from mock import patch
import stripe

from .. import views

pytestmark = pytest.mark.django_db


class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get("/")
        req.user = AnonymousUser()
        resp = views.AdminView.as_view()(req)
        assert "login" in resp.url

    def test_superuser(self):
        user = mixer.blend("auth.User", is_superuser=True)
        req = RequestFactory().get("/")
        req.user = user
        resp = views.AdminView.as_view()(req)
        assert resp.status_code == 200, "Authenticated user can access"


class TestPostUpdateView:
    def test_get(self):
        req = RequestFactory().get("/")
        req.user = AnonymousUser()
        obj = mixer.blend("tddapp.Post")
        resp = views.PostUpdateView.as_view()(req, pk=obj.pk)
        assert resp.status_code == 200, "Should be callable by anyone"

    def test_post(self):
        post = mixer.blend("tddapp.Post")
        data = {"description": "New Body Text!"}
        req = RequestFactory().post("/", data=data)
        req.user = AnonymousUser()
        resp = views.PostUpdateView.as_view()(req, pk=post.pk)
        assert resp.status_code == 302, "Should redirect to success view"
        post.refresh_from_db()
        assert post.description == "New Body Text!", "Should update the post"

    def test_security(self):
        user = mixer.blend("auth.User", first_name="Martin")
        post = mixer.blend("tddapp.Post")
        req = RequestFactory().post("/", data={})
        req.user = user
        with pytest.raises(Http404):
            views.PostUpdateView.as_view()(req, pk=post.pk)


class TestPaymentView:

    """
    USING python's  MOCK version
    @patch("tddapp.views.stripe")
    def test_payment(self, mock_stripe):
        mock_stripe.Charge.return_value = {"id": "234"}
        req = RequestFactory().post("/", data={"token": "123"})
        resp = views.PaymentView.as_view()(req)
        assert resp.status_code == 302, "Should redirect to success_url"
        assert len(mail.outbox) == 1, "Should send an email"
    """

    """
    USING pytest-mock version
    """

    def test_payment(self, mocker):
        mocker.patch("stripe.Charge", return_value={"id": "234"})
        req = RequestFactory().post("/", data={"token": "123"})
        resp = views.PaymentView.as_view()(req)
        assert resp.status_code == 302, "Should redirect to success_url"
        assert len(mail.outbox) == 1, "Should send an email"
