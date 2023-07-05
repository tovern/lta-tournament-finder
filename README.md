
# LTA Tournament finder

Finds suitable upcoming tournaments.

Due to the lack of an API and the existence of a strict cookie wall, selenium and chrome is required to crawl this data.

# Lambda deploy

mkdir package
pip -r requirements.txt --target ./package


# TODO

* UI or lambda function trigger
* ~~bug: randomly doesnt collect data~~
* Find a more efficient way of processing cohort links
* more error handling
* ~~ignore adverts~~
* ~~bug: wrong links to tournaments~~
* ~~foreach age~~
* ~~foreach cohort GS GD~~
* ~~classes~~
* ~~export pd to csv~~
* ~~export to google sheets~~
* ~~Readme
* ~~Trim distances~~
* ~~Trim/format dates~~