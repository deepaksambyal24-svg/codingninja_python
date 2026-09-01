from numpy.ma.core import std

ratings=[5 ,4 ,3 ,4 ,5 ,1, 2 ,5, 3, 4]
import math


def analyze_ratings(ratings):
    mean = (sum(ratings) / len(ratings))
    rating_mean_dif = 0
    max_rating = max(ratings)
    min_rating = min(ratings)
    print(f'max_rating: {max_rating}')
    max_count=0
    min_count=0
    for rating in ratings:
        rating_mean_dif += (mean - rating) ** 2
        if rating ==max_rating:
            max_count = max_count+1
        elif rating ==min_rating:
            min_count = min_count+1


    std = math.sqrt(rating_mean_dif / len(ratings))
    sted = (f'{std:.2f}')

    print(f'mean_rating: {mean}')
    print(f'std_deviation: {sted}')
    print(f"highest_rating: {{'rating': {max_rating}, 'count': {max_count}}}")
    print(f"lowest_rating: {{'rating': {min_rating}, 'count': {min_count}}}")



analyze_ratings(ratings)