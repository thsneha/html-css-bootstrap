import json


def get_data():
    with open("movies.json","r",encoding="utf8") as file:
       return json.load(file)


class Movies:
    def get(self):
        data=get_data()
        return[movie["title"] for movie in data]

# class Movieyearfilter:
    # def get(self,startyear,endyear):
    #     data=get_data()
    #     mvs=[movie for movie in data if movie["year"] in range(startyear,(endyear+1))]
    #     return mvs
# class Movieyearfilter:
#     def get(self,**kwargs):
#         data=get_data()
#         st_year=kwargs.get("start_year")
#         end_year=kwargs.get("end_year")
#         return [movie for movie in data if movie["year"] in range(st_year,(end_year+1))]
#
#
# # movies=Movies()
# # print(movies.get())
#
# mvfilter=Movieyearfilter()
# print(mvfilter.get(startyear=2015,endyear=2016))

class MovieGenersfilter:
    def get(self,**kwargs):
        data=get_data()
        geners=kwargs.get("genres")

        return[movie for movie in data if geners in movie["genres"]]
mvf=MovieGenersfilter()
print(mvf.get(genres="Action"))

class Moviefilter:
    def get(self,**kwargs):
        data=get_data()
        year=kwargs.get("year")
        gen=kwargs.get("genres")
        return[movie for movie in data if movie["year"]==year & (gen in movie["genres"])]
mvf=Moviefilter()
print(mvf.get(year=2017,genres="Action"))





