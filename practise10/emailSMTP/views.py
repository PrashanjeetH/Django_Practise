from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from .models import SmtpMailModel
from .forms import smtpMailForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = smtpMailForm(request.POST, request.FILES)
        # print('collected user data')
        if form.is_valid():
            # print("valid form")
            form.save()
            mailobject = form.cleaned_data
            print(mailobject)
            try :
                send_mail(
                    mailobject['subject'],
                    mailobject['body'],
                    mailobject['sender'],
                    [mailobject['receiver']],
                    fail_silently = False,
                )
                return redirect('final')
            except Exception as e:
                print(e)

        else:
            return render(request, 'index.html', {'form': form, 'message': 'Send Mail from '})
    else:
        form = smtpMailForm()
    return render(request, 'index.html', {'form': form, 'message': 'Send Mail here'})
    # return  render(request, 'index.html', {'form': form, 'message': 'Send Mail'})


def final(request):

    return render(request, 'final.html', {'message': 'Mail Sent'})
