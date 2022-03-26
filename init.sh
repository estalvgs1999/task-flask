# run as [source ./init.sh]
#!/bin/sh
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=develop
export SECRET_KEY=36d4J0Ltp3lRtee9HDxY3K

# Create alias
alias test='flask test'
alias run='flask run'
