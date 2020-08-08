#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This code Scraps a single query from Amazon | Purpose modifed

from bs4 import BeautifulSoup as soup
import requests
import os
import csv

# vars with GLOBAL scope
bot_query = "https://www.amazon.in/s?k="  # Defualt order, no filters are being applied
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
}
PROXY = {
    "https": "138.0.207.18:58566"
}  # {"https": "https//124.107.229.210:8080", "http":"http//124.107.229.210:8080"} | Proxy Rotation is absent | pip package will be released sooner
csv_index = 0  # To keep propering indexing when adding data from different pages

## Error handling needed when image sizes mismatch
def csv_append(
    user_query="-",
    item_count="-",
    name="-",
    item_page="-",
    rating="-",
    review="-",
    is1="-",
    is15="-",
    is2="-",
    is25="-",
    is3="-",
    price="-",
):
    global is_first
    global csv_index

    csv_index += 1
    item_count = csv_index  # Overtake
    csv_name = user_query.replace("+", "-") + ".csv"
    if is_first:
        with open(csv_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "SN",
                    "Name",
                    "Link to item",
                    "Rating",
                    "Reviews",
                    "Image Download link 1x",
                    "Image Download link 1.5x",
                    "Image Download link 2x",
                    "Image Download link 2.5x",
                    "Image Download link 3x",
                    "Price",
                ]
            )
            writer.writerow(
                [
                    item_count,
                    name,
                    item_page,
                    rating,
                    review.replace(",", ""),
                    is1,
                    is15,
                    is2,
                    is25,
                    is3,
                    price,
                ]
            )
    else:
        with open(csv_name, "a+", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    item_count,
                    name,
                    item_page,
                    rating,
                    review.replace(",", ""),
                    is1,
                    is15,
                    is2,
                    is25,
                    is3,
                    price,
                ]
            )


def slugify(img_name):
    """
    Slug Generator with image format
    :param1: image-name
    :return: slugged and format typed image
    """

    sluged_name = (
        img_name.replace(" ", "-").replace('"', "").replace("(", " ").replace(")", " ")
    )
    sluged_name = (
        sluged_name.replace("|", " ").replace("&", " ").replace(":", " ")
    )  # ASCII Range can be checked instead, More info needed about how will the images \
    # be used.

    return "{}.{}".format(sluged_name, "jpg")


def img_download(url, img_name):  # img_name):
    """
    Downloads the image from given url
    :param1: url
    :param2: imgage-name
    """
    # yes change here
    global csv_index

    # img_name = slugify(img_name).encode('ascii', 'ignore')
    img_name = slugify(str(csv_index))
    img = requests.get(url, headers=HEADER)
    with open(img_name, "wb") as f:  # Put them in folder properly
        f.write(img.content)


def scrape_bundle(user_query, page_count):

    global is_first
    is_first = True
    for count in range(1, int(page_count) + 1):
        scrape_query(user_query, count)
        print(count)
        is_first = False


def scrape_query(user_query, page_count):
    """
    Scrape and store the details of first page in csv that is when we search an item on amazon. Image is also downloaded.
    :param1: Name of item
    :return: None if no item appears

    Scraped Data:: Link to item | Item Name | Review count | Item Rating | Image download links | Item Availability | Price
    """

    global is_first

    amazon_query = bot_query + user_query + "&" + "page=" + str(page_count)

    client = requests.get(amazon_query, headers=HEADER)  # proxies=PROXY | gimmeproxy
    page_html = client.text

    page_soup = soup(page_html, "html.parser")
    container = page_soup.findAll("div", {"class": "s-result-item"})

    bundled_data = []

    ## Function can be made for below code | too much arg passing
    ## Better Error Handling is needed | can be avoided by key check
    # Taking only first item | Run complete loop to get all single page results
    if len(container) > 0:
        item_count = 0
        for item in container:

            item_count += 1
            item_page = "https://www.amazon.in" + item.a["href"]

            try:
                image_srcset = [
                    (img_link.split(" ")[0], img_link.split(" ")[1])
                    for img_link in item.a.img["srcset"].split(", ")
                ]
            except:
                image_srcset = None
            try:
                img_alt = item.img["alt"]  # item-name
            except:
                img_alt = ""
            try:
                rating = item.span.find("span", {"class": "a-icon-alt"}).text
                review_count = item.span.find("span", {"class": "a-size-base"}).text
            except:
                rating = "-"
                review_count = "-"

            # Availability
            for x in item.span.find_all("span"):
                if x.text == "Currently unavailable.":
                    availability = "Currently unavailable."
            else:
                availability = "Available"

            price = item.span.find("span", {"class": "a-price-whole"})
            if price != None:
                price = price.text
            else:
                price = "-"

            # Downloading most HR image
            try:
                img_download(url=image_srcset[-1][0], img_name=img_alt)
            except Exception as e:
                print(str(e))

            try:
                is1 = image_srcset[0][0]
                is15 = image_srcset[1][0]
                is2 = image_srcset[2][0]
                is25 = image_srcset[3][0]
            except:
                is1 = "-"
                is15 = "-"
                is2 = "-"
                is25 = "-"
            try:  # Maybe 1 Image we have
                is3 = image_srcset[-1][0]
            except:
                is3 = "-"

            csv_append(
                user_query=user_query,
                item_count=item_count,
                name=img_alt,
                item_page=item_page,
                rating=rating,
                review=review_count,
                is1=is1,
                is15=is15,
                is2=is2,
                is25=is25,
                is3=is3,
                price=price,
            )
            is_first = False
    else:
        item = None
        return item


if __name__ == "__main__":

    user_query = input("Enter your Product: ").replace(
        " ", "+"
    )  # More filtering is needed | search 'mobile' to get all mobile data scraped
    page_count = input("Scrape upto how many pages: ")

    if page_count in ["0", " ", None]:
        scrape_bundle(user_query, "1")
    else:
        scrape_bundle(user_query, page_count)
