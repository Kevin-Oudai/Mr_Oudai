from django.views.generic import CreateView
from emails.models import ContactMe
from django.core.mail import send_mail

class HomeView(CreateView):
    template_name = 'index.html'
    model = ContactMe
    fields = "__all__"

    def form_valid(self, form):
        name = form.instance.name
        email = form.instance.email
        phone = form.instance.phone
        subject = form.instance.subject
        message = form.instance.message
        content = ("Name: {}\nEmail: {}\nPhone: {}\nMessage: {}.".format(name, email, phone, message))
        send_mail(
            subject,
            content,
            email,
            ['kevinoudai@hotmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)

        
    
