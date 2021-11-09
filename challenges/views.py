from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
months_and_challenges = {
    "january": "run 5 kms",
    "february": "jog 10 kms",
    "march": "ride cycle 50 kms",
    "april": "100 push ups",
    "may": "50 squats",
    "june": "drink 20 glass of water",
    "july": "do not eat sugar",
    "august": "get up at 5 am",
    "september": "eat oats for breakfast",
    "october": "eat eggs for dinner",
    "november": "drink carrot juice",
    "december": None,
}


def index(requests):
    # home_page_list = "<h1>Month and challenge list</h1> <ol>"
    # for i in months_and_challenges:
    #     hyperlinks = reverse("month_str_url", args=[i])
    #     home_page_list += f'<li> <h1> <a href = "{hyperlinks}" >{i}</a> </h1></li>'
    # response_data = home_page_list + "</ol>"
    # return HttpResponse(response_data)

    #     Using DTL
    context = {
        "month_list": list(months_and_challenges.keys())
    }
    return render(requests, "challenges/index.html", context=context)


def feb_challenge(requests):
    return HttpResponse("you got this")


# def monthly_challenge(requests, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "run 10 kms daily"
#     elif month == "february":
#         challenge_text = "ride cycle daily 10kms"
#     elif month == "march":
#         challenge_text = "go to gym daily"
#     else:
#         return HttpResponseNotFound(month + " is Not Supported")
#     return HttpResponse(challenge_text)

def monthly_challenge(requests, month):
    """making the function more dynamic"""
    try:
        challenge_text = months_and_challenges[month]

        # commented the below 2 commands as it was purely returning html tags in string format
        # challenge_text = f'<h1>Challenge: {challenge_text}</h1> <ol> <li>content1</li> <li>content2</li> <li>content3</li> </ol>\
        #     <a href = "https://www.w3schools.com" > Visit W3Schools.com! </a> '
        # return HttpResponse(challenge_text)

        # reads the html file and returns the html file content as string
        # response_data=render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)

        # simply return the html file
        # return render(requests, "challenges/challenges.html")

        # return the html file with context
        context = {
            "month_text": challenge_text,
            "month": month.upper(),
        }
        return render(requests, "challenges/challenges.html", context)
    except KeyError:
        # cannot use render as it returns a http success code
        # challenge_text = month + " is not a valid month"
        # return HttpResponseNotFound(challenge_text)

        # the following returns html file with 404 error
        # response_text = render_to_string("challenges/404.html")
        # return HttpResponseNotFound(response_text)

        # use Http404 class which looks for 404.html file
        # remember to set the DEBUG=False
        raise Http404()



# def monthly_challenge_num(requests, month):
#     challenge_text = None
#     print("month")
#     if month == 1:
#         challenge_text = "run 10 kms daily"
#     elif month == 2:
#         challenge_text = "ride cycle daily 10kms"
#     elif month == 3:
#         challenge_text = "go to gym daily"
#     else:
#         return HttpResponseNotFound(f"{month} is Not Supported")
#     return HttpResponse(challenge_text)

def monthly_challenge_num(requests, month):
    try:
        # challenge_text = list(months_and_challenges.values())[month - 1]
        redirect_path = reverse("month_str_url", args=[list(months_and_challenges.keys())[month - 1]])
        return HttpResponseRedirect(redirect_path)
        # return HttpResponse(challenge_text)
    except IndexError:
        challenge_text = str(month) + " is not a valid month number"
        return HttpResponseNotFound(challenge_text)
