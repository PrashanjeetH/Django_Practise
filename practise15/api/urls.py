from django.urls import path


from api.views import students_list
urlpatterns = [
    path('api/student_info/', students_list, name='get_student')
]         


# import json
# import requests
# def getWinnerTotalGoals(competition, year) :
#     goals = 0
#     url1 = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}"
#     response = requests.request("GET", url1, headers={}, data={})
#     winner = json.loads(response.text. encode("utf8"))["data"][0]["winner"]
#     for team in ["team1", "team2"]:
#         url2=f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&{team}={winner}&page=1"
#         response = requests.request ("GET", url2, headers={}, data={})
#         total_pages = json.loads(response. text.encode("utf8"))["total_pages"]
#         for i in range(1, total_pages+1):
#             url3 = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&{team}={winner}&page={i}"
#             response = requests.request ("GET", url3, headers={}, data={})
#             r = json. loads (response. text.encode("utf8"))
#             r_data = r["data"]
#             for record in r_data:
#                 goals += int(record[team+"goals"])
#     return goals