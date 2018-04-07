# remove-transients-wordpress
This is two simple scripts that will purge transients from your Wordpress database. Use at your own risk.
I take no responsibility for this borking out your whole system.

#################################################
##              INSTRUCTIONS                   ##
#################################################
1. Open transient.py
2. Modify the specified options on line 6
3. Modify the table in line 9 if needed
4. Save and close
5. Open transientarchive.py
6. Modify line 3 to whatever directory you want to store logs into.

##################################################
##              CREATE A CRON JOB               ##
##################################################
Create a cron job to run the two scripts as needed. If you need help doing just search for "Create a cron job" on Google.

