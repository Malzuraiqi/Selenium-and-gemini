from flask import Blueprint, render_template, request, flash
from amazon_list_selenium import main
import validators

def is_valid_url(url):
    return validators.url(url) == True

views = Blueprint('views', __name__)

@views.route("/", methods=['POST', 'GET'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        filterText = request.form.get('filterText')

        if url and filterText:
            if is_valid_url(url) and ('amazon' in url):
                try:
                    result = main(url, filterText)

                    if result:
                        flash(f"Successfully scraped {len(result)} items", category='success')
                    else:
                        flash("No results found or scraping failed", category='warning')

                except Exception as e:
                    flash(f"Scraping error: {str(e)}", category='danger')
                    print(f"Scraping error: {e}")

            else:
                flash("Invalid URL, please try again", category='danger')
        else:
            flash("URL and filter text are required", category='danger')

    return render_template("base.html", result=result)