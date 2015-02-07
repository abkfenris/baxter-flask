"""
App error handlers
"""
from flask import render_template, request, jsonify, current_app
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    """
    Handle 403 Forbidden errors in html and json
    """
    current_app.logger.error('403')
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template('errors/403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    """
    Handle 404 Page Not Found errors in html and json
    """
    current_app.logger.error('404')
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 Internal Server errors in html and json
    """
    current_app.logger.error('500')
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('errors/500.html'), 500
