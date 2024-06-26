import requests
# separate file for secret Key-Information
import config

print("Hello")

#API_Key and Blogger_ID is read from external file config.py
APIKEY = config.API_Key
# Blog-ID of testfuerperu
BLOGID = config.Blogger_ID
# get_blog = (f"https://www.googleapis.com/blogger/v3/blogs/{BLOGID}?key={APIKEY}")
# response = requests.get(get_blog)
get_posts = (f"https://www.googleapis.com/blogger/v3/blogs/{BLOGID}/posts?key={APIKEY}")
post_response = requests.get(get_posts)


# if response.status_code == 200:
#     blog_data = response.json()
#     print(blog_data)
# else:
#     print("No response")

if post_response.status_code == 200:
    post_data = post_response.json()
    # print(post_data)
    print("Got data sucessfully")
    if 'items' in post_data and post_data['items']:
    # Iterate over each item but reverse the order
      for item in reversed(post_data.get("items", [])):
          # Access and process each item
          print("Title:", item.get('title'))
          print("Published:", item.get('published'))
          print("Content:", item.get('content'))
          # print("URL:", item.get('url'))
          # print("Author:", item.get('author', {}).get('displayName'))
          print()  # Add a blank line for readability
    else:
      print("No 'items' found or it's not a list")
      print(type(post_data))
else:
    print("No response")

# print(response.status_code)
print(post_response.status_code)




