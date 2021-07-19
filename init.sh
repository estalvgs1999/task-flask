# run as source
#!/bin/sh
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=develop

# Run app
activate() {
    . ../venv/bin/activate
}

# Test app
alias test='flask test'
alias run='flask run'
