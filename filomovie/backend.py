import sys
import os

from flask import (
    Flask, Blueprint, flash, redirect, render_template, request, url_for
)
from filomovie import app

# TODO: backend processing


def process_data_example(searchedMovie):
    print("You searched: " + searchedMovie, flush=True)

    # NOTE: send to database or something
    return searchedMovie


