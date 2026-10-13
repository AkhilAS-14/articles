
from django.shortcuts import render
import requests


from django.http import JsonResponse
from articles.models import article



TMDB_API_KEY = "7c502410642dceceb714db2196281bb8"


def homepage(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def movie_details(request):
    movies = []
    query = request.GET.get("q")
    error = None

    if query:
        try:
            response = requests.get(
                "https://api.themoviedb.org/3/search/movie",
                params={
                    "api_key": TMDB_API_KEY,
                    "query": query
                },
                timeout=10
            )

            print("STATUS:", response.status_code)
            print("TMDB RESPONSE:", response.text[:500])

            response.raise_for_status()

            data = response.json()
            movies = data.get("results", [])

            print("MOVIES FOUND:", len(movies))

        except requests.exceptions.RequestException as e:
            print("TMDB ERROR:", e)
            error = "Unable to connect to TMDB."

    return render(
        request,
        "movies.html",
        {
            "movies": movies,
            "query": query,
            "error": error,
        }
    )
def movies_api(request):
    Articles = list(
        article.objects.values(
            "id",
            "title",
            "date",
            "thumb"
        )
    )

    return JsonResponse(Articles, safe=False)




