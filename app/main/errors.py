from flask import render_template, request, jsonify
from . import main

@main.app_errorhandler(404)
def page_not_found(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

@main.app_errorhandler(400)
def bad_request(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'bad request'})
        response.status_code = 400
        return response
    return render_template('400.html'), 400


@main.app_errorhandler(500)
def internal_server_error(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500

@main.app_errorhandler(301)
def moved_permanently(error):
    response = jsonify({'error': 'moved permanently'})
    response.status_code = 301
    return response
