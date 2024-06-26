#!/usr/bin/python3
"""Module compiled wth Python3"""
import requests
import csv


def fetch_and_print_posts():
    """
    Function that fetches posts from an API.
    It also prints the status codes returned.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Function that converts API posts data into a csv file
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()

        post_dicts = [
            {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
            } for post in posts
        ]

        csv_file_path = 'posts.csv'
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ['id', 'title', 'body']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for post_dict in post_dicts:
                csv_writer.writerow(post_dict)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
