from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    # html = """
    #  <html>
    #         <head>
    #             <title>注册页面</title>
    #         </head>
    #         <body>
    #             <form method='post' action='/register/'>
    #                 username：<input type='text' name='username' /><br/>
    #                 password：<input type='password' name='password' /><br/>
    #                 <input type='submit' value='注册' />
    #             </form>
    #         </body>
    #     </html>
    #     """
    # return HttpResponse(html)
    return render(request, "register.html")
