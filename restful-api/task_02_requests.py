#!/usr/bin/python3
"""Module compiled wth Python3"""
import requests
import json
import csv


def fetch_and_print_posts():
    """
    Function that fetches posts from an API.
    It also prints the status codes returned.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        posts = r.json()
        fetch_and_save_posts(posts)


def fetch_and_save_posts(posts):
    """
    Function that saves API posts data into a json file,
    then converted into a csv file
    """
    jsonFile = []
    for post in posts:
        post_dict = {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        }
        jsonFile.append(post_dict)

    with open('posts.json', 'w', encoding='UTF-8') as jsonf:
        json.dump(jsonFile, jsonf)

    with open('posts.json', 'r', encoding='UTF-8') as jsonf:
        posts_data = json.load(jsonf)

    with open('posts.csv', 'w', newline='', encoding='UTF-8') as csvf:
        fieldnames = ['id', 'title', 'body']
        csv_writer = csv.DictWriter(csvf, fieldnames=fieldnames)

        csv_writer.writeheader()
        for post in posts_data:
            csv_writer.writerow(post)

if __name__ == "__main__":
    fetch_and_print_posts()
