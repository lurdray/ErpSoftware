from django.shortcuts import render

# Create your views here.
def DashboardView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "admin_app/dashboard.html", context)