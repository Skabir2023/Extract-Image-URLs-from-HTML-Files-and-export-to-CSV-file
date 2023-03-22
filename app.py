import re
import csv

# Open the HTML file and read its contents
with open('Blogger image to WP.html', 'r') as file:
    html = file.read()

# Define the regular expression to match image URLs
pattern = re.compile(r'<img.*?src="(.*?)".*?>')

# Find all matches of the regular expression in the HTML
matches = pattern.findall(html)

# Open a CSV file for writing
with open('image_urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the URLs to the CSV file
    for url in matches:
        writer.writerow([url])
        
