from django.shortcuts import render

from apps.message_form.models import message

# get, post method
def message_form(request):
    # 需要区别两种不同的方法： get 和 post
    message_obj = message()
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_detail = request.POST.get("message","")

        message_obj.name = name
        message_obj.email = email
        message_obj.address = address
        message_obj.message = message_detail
        message_obj.save()

    return render(request, "message_form.html")

