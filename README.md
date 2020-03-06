# remove-transients-wordpress
This is two simple scripts that will purge transients from your Wordpress database. Use at your own risk.
I take no responsibility for this borking out your whole system.

#################################################
##              INSTRUCTIONS                   ##
#################################################
USAGE:
python3 transients.py DB_USERNAME DB_HOST DB_NAME DB_USER_PASSWORD


transientarchive.py will automatically archive your log files. You can modify it as needed.
Modify line 3 to whatever directory you want to store logs into.

##################################################
##              CREATE A CRON JOB               ##
##################################################
Create a cron job to run the two scripts as needed. If you need help doing just search for "Create a cron job" on Google.

