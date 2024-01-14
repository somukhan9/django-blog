from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView, FormView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib import auth

from .forms import SignUpForm, SignInForm


class SignInView(View):
    template_name = "authapp/sign-in.html"

    def get(self, request):
        form = SignInForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignInForm(request.POST)
        username_or_email = request.POST["username_or_email"]
        password = request.POST["password"]
        user = auth.authenticate(
            request, username=username_or_email, password=password)
        if user is None:
            return render(request, self.template_name, {"form": form, "form_error": "Invalid Credentials"})

        auth.login(request, user)

        return HttpResponseRedirect(reverse_lazy('blog:home'))


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "authapp/sign-up.html"
    success_url = reverse_lazy("authapp:sign-in")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as ex:
            # print(dict(ex)["field"])
            # form.errors[dict(ex)["field"][0]] = str(dict(ex)["message"][0])
            return self.form_invalid(form=form)
