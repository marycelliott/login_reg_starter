from django.shortcuts import render

# Create your views here.
def index(request):
    pass

def register(request):
    pass
    # check for post method
    # if true
        # validate the user(in models)
        # check if any errors were return
        # if true
            # hash the password
            # create the user
            # saving the user's id in session(user_id)
            # redirect to welcome/success page
        # else
            # display errors (django messages -> from django.contrib import messages)
            # redirect to "/" index route
    # else
        # redirect to "/" index route

def login(request):
    pass
    # check for post method
    # if true
        # query db with email
        # check the query
        # if query true
            # found a user
            # verify password from form data matches the password in db
            # if true
                # user is who they say they are
                # save the user_id in session
                # redirect to "/books" book index route
            # else
                # error message, invalid password/email combinations
                # redirect to "/" index route
        # else
            # email doesnt exist
            # send message to register email
            # redirect to "/" index route
    # false
        # redirect to "/" index route

def success(request):
    return render(request, 'users/success.html')