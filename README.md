Simple Python-based scraper to send an email alert to the specified recipients whenever the U.S. Department of Ed opens
a new investigation into one or more colleges. Email alerts include a one line summary and an in-message table of the new
investigations - including their subjects, targets, and initiation dates.

## Installation
Choose a directory to host the crawler, and run the following commands:

`git clone https://github.com/declanrjb/higher-ed-investigations-crawler.git`

Open update-and-send.ipynb and update the `recipients` list with your own email address and/or the addresses
of any other recipients.

Then, run:

`crontab -e`

Update your cron to include the following job:

`0 10 * * 2 <your-directory>/higher-ed-investigations-crawler/shell-scripts/send-weekly-update.sh`

Make sure that the header of your crontab includes your current path as output by `echo $PATH`.

Run `:x` to save and exit cron. Cron will run the update-and-send Python notebook every Tuesday morning at 10am, the day
the DoE updates [their site](https://ocrcas.ed.gov/open-investigations). If new investigations are found, they will be added
to the data/weekly-logs directory as a CSV file, and you will receive an email alert.