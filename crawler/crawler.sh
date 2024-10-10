#!/bin/bash

# function to crawl a given spider
crawl_spider() {
    scrapy crawl $1
}

# list of spiders to crawl
spiders=(
    "home"
    "limited_edition"
)

# first we will be changing directory
# cd "./crawler"

# loop through the spiders and crawl as one by one
for spider in "${spiders[@]}"; do
    crawl_spider "$spider"
done