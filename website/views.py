from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
#{} = content dictionary pass from backend to front end

def home(request):
	return render(request, 'home.html',{})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			  message_name 
		    , message 
			, message_email  
			, ['thinktinkinc@gmail.com'] #to email(place its sent)
			,fail_silently=False
			)

		return render(request, 'contact.html',{'message_name': message_name})
	
	else:
		
		return render(request, 'contact.html',{})