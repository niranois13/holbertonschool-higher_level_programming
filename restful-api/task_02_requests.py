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
    print("Status code: {}".format(r.status_code))
    if 200 <= r.status_code <= 299:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Function that converts API posts data into a csv file
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if 200 <= r.status_code <= 299:
        posts = r.json()
        csv_file_path = 'posts.csv'
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ['id', 'title', 'body']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for post in posts:
                csv_writer.writerow({'id': post['id'], 'title': post['title'],
                                    'body': post['body']})
